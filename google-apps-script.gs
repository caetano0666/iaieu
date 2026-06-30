/**
 * IAieu — Recebe os cadastros do site e grava na planilha do Google Sheets.
 *
 * Como usar:
 *  1. Crie uma planilha no Google Sheets.
 *  2. Menu  Extensões → Apps Script.
 *  3. Apague o conteúdo padrão e cole TODO este arquivo.
 *  4. Salve, depois Implantar → Nova implantação → tipo "App da Web":
 *        - Executar como: Eu (sua conta)
 *        - Quem pode acessar: Qualquer pessoa
 *  5. Copie a URL gerada (termina em /exec) e cole no index.html
 *     na constante SHEETS_URL.
 *
 * IMPORTANTE: ao editar este código depois, é preciso reimplantar:
 *   Implantar → Gerenciar implantações → ✏️ editar → Versão: "Nova versão" → Implantar.
 *   (a URL /exec continua a mesma)
 */

// E-mail que recebe o aviso de cada novo cadastro. Deixe vazio ('') para não notificar.
var EMAIL_NOTIFICACAO = 'czamma@gmail.com';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(30000); // evita gravações simultâneas embaralharem linhas

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Cadastros');
    if (!sheet) {
      sheet = ss.insertSheet('Cadastros');
    }

    // Cria o cabeçalho na primeira vez
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Data/Hora', 'Nome', 'E-mail', 'Cidade', 'Telefone']);
    }

    var p = e.parameter;
    sheet.appendRow([
      new Date(),
      p.nome || '',
      p.email || '',
      p.cidade || '',
      p.telefone || ''
    ]);

    // Notifica por e-mail a cada novo cadastro
    if (EMAIL_NOTIFICACAO) {
      MailApp.sendEmail({
        to: EMAIL_NOTIFICACAO,
        subject: '🔔 Novo cadastro IAieu — ' + (p.nome || 'sem nome'),
        body:
          'Um novo cadastro chegou pelo site:\n\n' +
          'Nome: ' + (p.nome || '') + '\n' +
          'E-mail: ' + (p.email || '') + '\n' +
          'Cidade: ' + (p.cidade || '') + '\n' +
          'Telefone: ' + (p.telefone || '') + '\n\n' +
          'Planilha: ' + ss.getUrl()
      });
    }

    return ContentService
      .createTextOutput(JSON.stringify({ result: 'success' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}

// Permite abrir a URL /exec no navegador só para conferir que está no ar.
function doGet() {
  return ContentService
    .createTextOutput('IAieu — endpoint de cadastro ativo.')
    .setMimeType(ContentService.MimeType.TEXT);
}
