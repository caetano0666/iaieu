/**
 * IAieu — Recebe do site os cadastros (curso IAieu GO) e os depoimentos,
 * gravando cada tipo em uma aba da planilha do Google Sheets.
 *
 * Como usar:
 *  1. Crie uma planilha no Google Sheets.
 *  2. Menu  Extensões -> Apps Script.
 *  3. Apague o conteúdo padrão e cole TODO este arquivo.
 *  4. Salve, depois Implantar -> Nova implantação -> tipo "App da Web":
 *        - Executar como: Eu (sua conta)
 *        - Quem pode acessar: Qualquer pessoa
 *  5. Copie a URL gerada (termina em /exec) e cole nas páginas do site
 *     (iaieu-go.html e depoimentos.html) na constante SHEETS_URL.
 *
 * IMPORTANTE: ao editar este código depois, é preciso reimplantar:
 *   Implantar -> Gerenciar implantações -> editar (lápis) -> Versão: "Nova versão" -> Implantar.
 *   (a URL /exec continua a mesma)
 */

// E-mail que recebe o aviso de cada novo envio. Deixe vazio ('') para não notificar.
var EMAIL_NOTIFICACAO = 'czamma@gmail.com';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(30000); // evita gravações simultâneas embaralharem linhas

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var p = e.parameter;

    // Diferencia depoimento de cadastro pelo campo "tipo"
    if (p.tipo === 'depoimento') {
      gravarDepoimento(ss, p);
    } else {
      gravarCadastro(ss, p);
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

// ---- Cadastro do curso IAieu GO -> aba "Cadastros" ----
function gravarCadastro(ss, p) {
  var sheet = ss.getSheetByName('Cadastros');
  if (!sheet) { sheet = ss.insertSheet('Cadastros'); }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Data/Hora', 'Nome', 'E-mail', 'Cidade', 'Telefone']);
  }
  sheet.appendRow([new Date(), p.nome || '', p.email || '', p.cidade || '', p.telefone || '']);

  notificar('Novo cadastro IAieu GO - ' + (p.nome || 'sem nome'),
    'Nome: ' + (p.nome || '') + '\n' +
    'E-mail: ' + (p.email || '') + '\n' +
    'Cidade: ' + (p.cidade || '') + '\n' +
    'Telefone: ' + (p.telefone || '') + '\n\n' +
    'Planilha: ' + ss.getUrl());
}

// ---- Depoimento -> aba "Depoimentos" ----
function gravarDepoimento(ss, p) {
  var sheet = ss.getSheetByName('Depoimentos');
  if (!sheet) { sheet = ss.insertSheet('Depoimentos'); }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Data/Hora', 'Nome', 'Profissão', 'Depoimento', 'Status']);
  }
  sheet.appendRow([new Date(), p.nome || '', p.profissao || '', p.depoimento || '', 'pendente']);

  notificar('Novo depoimento IAieu - ' + (p.nome || 'sem nome'),
    'Nome: ' + (p.nome || '') + '\n' +
    'Profissão: ' + (p.profissao || '') + '\n\n' +
    'Depoimento:\n' + (p.depoimento || '') + '\n\n' +
    'Para publicar: adicione no admin do site (aba Depoimentos).\n' +
    'Planilha: ' + ss.getUrl());
}

// ---- Envia o aviso por e-mail (se configurado) ----
function notificar(assunto, corpo) {
  if (EMAIL_NOTIFICACAO) {
    MailApp.sendEmail({ to: EMAIL_NOTIFICACAO, subject: '🔔 ' + assunto, body: corpo });
  }
}

// Permite abrir a URL /exec no navegador só para conferir que está no ar.
function doGet() {
  return ContentService
    .createTextOutput('IAieu — endpoint ativo (cadastros e depoimentos).')
    .setMimeType(ContentService.MimeType.TEXT);
}

// Rode esta função UMA vez no editor para autorizar o envio de e-mail.
function autorizarEmail() {
  MailApp.sendEmail(
    EMAIL_NOTIFICACAO,
    'Teste de autorização — IAieu',
    'Se você recebeu este e-mail, a notificação de novos envios está funcionando! ✅'
  );
}
