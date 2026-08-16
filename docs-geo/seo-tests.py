#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bateria de testes GEO + SEO do iaieu.com.

Rode SEMPRE antes de publicar:

    python3 docs-geo/seo-tests.py

Meta: 0 FAIL. Um WARN nao impede a publicacao, mas precisa ser uma decisao
consciente, nao um esquecimento.

O script le os arquivos do repositorio (nao o site no ar), entao ele valida
o que voce esta prestes a publicar.
"""

import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://iaieu.com"

# arte.html saiu desta lista em 04/08/2026, por decisao do proprietario: a galeria
# esta vazia, entao a pagina foi tirada do percurso do visitante e do sitemap.
# Ela continua no repositorio e continua sendo checada em teste_regras_da_casa.
# Quando a galeria for preenchida, devolver a linha "arte.html" aqui e no sitemap.
# Em 13/08/2026 oito paginas saíram desta lista. Elas apresentam o
# posicionamento anterior a home nova, nao foram reescritas e viraram arquivo
# historico: continuam acessiveis, mas com noindex, fora do sitemap, sem
# hreflang e sem dados estruturados. Ver ARQUIVO_HISTORICO logo abaixo.
PAGINAS = {
    "index.html": f"{BASE}/",
    "plinio/index.html": f"{BASE}/plinio/",
    "stw-daryl-lucas/index.html": f"{BASE}/stw-daryl-lucas/",
}

# As homes traduzidas. Indexaveis e no sitemap desde 13/08/2026.
TRADUZIDAS = {
    "en/index.html": f"{BASE}/en/",
    "es/index.html": f"{BASE}/es/",
}

# Arquivo historico. Acessiveis de proposito, fora do percurso.
# So voltam para PAGINAS depois de reescritas no discurso atual.
ARQUIVO_HISTORICO = [
    "o-que-vendemos.html", "caso-operacao-do-zero.html", "iaieu-evc.html",
    "iaieu-mais.html", "sobre.html", "projetos.html", "conteudos.html",
    "depoimentos.html",
]

# Fora do percurso por decisao do proprietario, cada uma na sua data.
FORA_DO_PERCURSO = ["arte.html", "iaieu-go.html", "shimanofest.html"]

# Nomes que a home nova nao vende mais. Nenhuma pagina indexavel pode
# declarar isso em dado estruturado.
SCHEMA_PROIBIDO = ["FAQPage", '"name": "IAieu+"', '"name": "IAieu eVc"']

# O acento da marca. Decisao do dono em 14/08/2026: o vermelho do site
# predomina sobre o do arquivo do logo, que era rgb(218,9,12). Todo ativo
# grafico da identidade tem que usar exatamente este tom.
ACENTO = (193, 18, 31)          # #C1121F
ATIVOS_DA_MARCA = [
    "imagens/logo-iaieu.png", "imagens/logo-iaieu-claro.png",
    "og-image.png", "og-image-en.png", "og-image-es.png",
    "favicon-32.png", "apple-touch-icon.png", "icon-512.png",
]

# Favicon P1, aprovado em 14/08/2026. Estes arquivos precisam existir na raiz
# e serem declarados nas homes. O pacote original esta em docs-geo/favicon/.
FAVICON_P1 = [
    "favicon.svg", "favicon.ico", "apple-touch-icon.png", "site.webmanifest",
    "icon-192.png", "icon-512.png", "icon-512-maskable.png",
    "favicon-16.png", "favicon-32.png", "favicon-48.png", "favicon-96.png",
    "favicon-16-dark.png", "favicon-32-dark.png",
    "favicon-48-dark.png", "favicon-96-dark.png",
]

# Arquivos que nunca podem sumir do repositorio.
INTOCAVEIS = ["CNAME", "robots.txt", "sitemap.xml", "google7279386773b5d258.html"]

PALAVRAS_PROIBIDAS = [
    "jornada", "transformação", "potencializar", "impulsionar", "alavancar",
    "agregar valor", "visão estratégica", "gerar impacto", "ecossistema",
    "protagonismo", "sinergia", "alta performance",
]

resultados = []


def ok(teste, detalhe=""):
    resultados.append(("PASS", teste, detalhe))


def falha(teste, detalhe=""):
    resultados.append(("FAIL", teste, detalhe))


def aviso(teste, detalhe=""):
    resultados.append(("WARN", teste, detalhe))


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as fh:
        return fh.read()


def texto_visivel(html):
    """Remove script, style e tags: sobra o que o leitor realmente ve."""
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html)


def blocos_jsonld(html):
    return re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.S
    )


# ---------------------------------------------------------------- arquivos
def teste_arquivos_intocaveis():
    for arq in INTOCAVEIS:
        if os.path.exists(os.path.join(RAIZ, arq)):
            ok(f"arquivo critico presente: {arq}")
        else:
            falha(f"arquivo critico SUMIU: {arq}", "nunca pode ser apagado")


# ---------------------------------------------------------------- metadata
def teste_metadata():
    titles, descriptions = {}, {}
    for arq, url in PAGINAS.items():
        html = ler(arq)

        m = re.search(r"<title>(.*?)</title>", html, flags=re.S)
        if not m or not m.group(1).strip():
            falha(f"{arq}: sem <title>")
        else:
            t = m.group(1).strip()
            titles.setdefault(t, []).append(arq)
            if len(t) > 65:
                aviso(f"{arq}: title com {len(t)} caracteres", "acima de 65 pode ser cortado")
            ok(f"{arq}: title presente")

        m = re.search(r'<meta name="description" content="(.*?)">', html, flags=re.S)
        if not m or not m.group(1).strip():
            falha(f"{arq}: sem meta description")
        else:
            d = m.group(1).strip()
            descriptions.setdefault(d, []).append(arq)
            if not (50 <= len(d) <= 165):
                aviso(f"{arq}: description com {len(d)} caracteres", "ideal entre 50 e 165")
            ok(f"{arq}: description presente")

        m = re.search(r'<link rel="canonical" href="(.*?)">', html)
        if not m:
            falha(f"{arq}: sem canonical")
        elif m.group(1) != url:
            falha(f"{arq}: canonical errado", f"achado {m.group(1)}, esperado {url}")
        else:
            ok(f"{arq}: canonical autorreferente")

        for prop, valor in [("og:site_name", "IAieu"), ("og:locale", "pt_BR")]:
            if f'property="{prop}"' in html:
                ok(f"{arq}: {prop}")
            else:
                falha(f"{arq}: sem {prop}")

        m = re.search(r'<meta property="og:image" content="(.*?)">', html)
        if not m:
            falha(f"{arq}: sem og:image")
        elif not m.group(1).startswith("https://"):
            falha(f"{arq}: og:image nao e absoluta", m.group(1))
        else:
            local = m.group(1).replace(BASE + "/", "")
            if os.path.exists(os.path.join(RAIZ, local)):
                ok(f"{arq}: og:image absoluta e o arquivo existe")
            else:
                falha(f"{arq}: og:image aponta para arquivo inexistente", local)

        if 'name="twitter:card"' in html:
            ok(f"{arq}: twitter card")
        else:
            falha(f"{arq}: sem twitter:card")

        if 'lang="pt-BR"' in html:
            ok(f"{arq}: lang pt-BR")
        else:
            falha(f"{arq}: sem lang pt-BR")

    for t, arqs in titles.items():
        if len(arqs) > 1:
            falha("title duplicado", f"{t} em {arqs}")
    for d, arqs in descriptions.items():
        if len(arqs) > 1:
            falha("description duplicada", f"em {arqs}")


# ---------------------------------------------------------------- estrutura
def teste_estrutura():
    for arq in list(PAGINAS) + list(TRADUZIDAS):
        html = ler(arq)

        h1s = re.findall(r"<h1[^>]*>", html, flags=re.I)
        if len(h1s) == 1:
            ok(f"{arq}: H1 unico")
        elif not h1s:
            falha(f"{arq}: nenhum H1")
        else:
            falha(f"{arq}: {len(h1s)} H1", "deve haver exatamente um")

        sem_alt = [t for t in re.findall(r"<img[^>]*>", html, flags=re.I)
                   if "alt=" not in t.lower()]
        if sem_alt:
            falha(f"{arq}: {len(sem_alt)} imagem sem alt")
        else:
            ok(f"{arq}: todas as imagens com alt")


# ---------------------------------------------------------------- json-ld
def teste_jsonld():
    ids_vistos = {}
    for arq, url in PAGINAS.items():
        html = ler(arq)
        blocos = blocos_jsonld(html)
        if not blocos:
            falha(f"{arq}: sem JSON-LD")
            continue
        for bruto in blocos:
            try:
                dados = json.loads(bruto)
            except json.JSONDecodeError as e:
                falha(f"{arq}: JSON-LD nao parseia", str(e))
                continue
            ok(f"{arq}: JSON-LD valido")

            grafo = dados.get("@graph", [dados])
            tipos = [n.get("@type") for n in grafo]

            for node in grafo:
                aid = node.get("@id")
                if aid:
                    tipo = node.get("@type")
                    if aid in ids_vistos and ids_vistos[aid] != tipo:
                        falha("@id com tipos divergentes", f"{aid}: {ids_vistos[aid]} e {tipo}")
                    ids_vistos[aid] = tipo
                    if not aid.startswith(BASE):
                        falha(f"{arq}: @id fora do dominio", aid)

            tem_pagina = any(
                t in ("WebPage", "AboutPage", "CollectionPage", "ItemPage")
                for t in tipos
            )
            if tem_pagina:
                ok(f"{arq}: entidade de pagina declarada")
            else:
                falha(f"{arq}: sem WebPage no grafo")

            for node in grafo:
                if node.get("@type") in ("WebPage", "AboutPage", "CollectionPage"):
                    if node.get("url") == url:
                        ok(f"{arq}: url do WebPage bate com o canonical")
                    else:
                        falha(f"{arq}: url do WebPage diferente do canonical",
                              f"{node.get('url')} vs {url}")
                    if node.get("breadcrumb"):
                        ok(f"{arq}: breadcrumb presente")
                    else:
                        aviso(f"{arq}: sem breadcrumb")

            # Regra absoluta: nunca inventar avaliacao propria.
            if re.search(r'"(aggregateRating|reviewRating|ratingValue)"', bruto):
                falha(f"{arq}: contem schema de avaliacao", "PROIBIDO criar avaliacao propria")
            else:
                ok(f"{arq}: sem aggregateRating inventado")

            # Preco nao e publico: nenhum campo de preco pode vazar.
            if re.search(r'"price"\s*:', bruto):
                falha(f"{arq}: schema declara price", "precos nao sao publicos")


def teste_entidades_da_home():
    grafo = json.loads(blocos_jsonld(ler("index.html"))[0])["@graph"]
    por_id = {n.get("@id"): n for n in grafo}
    # A home nova, aprovada em 13/08/2026, tem oito secoes e nenhuma FAQ.
    # Por isso #faq saiu daqui. Ver teste_home_sem_faq logo abaixo.
    esperados = [
        f"{BASE}/#organization",
        f"{BASE}/#person-caetano",
        f"{BASE}/#website",
        f"{BASE}/#webpage",
    ]
    for eid in esperados:
        if eid in por_id:
            ok(f"home declara {eid}")
        else:
            falha(f"home nao declara {eid}")

    org = por_id.get(f"{BASE}/#organization", {})
    pes = por_id.get(f"{BASE}/#person-caetano", {})
    if isinstance(org.get("founder"), dict) and org["founder"].get("@id") == f"{BASE}/#person-caetano":
        ok("Organization aponta founder para a Person")
    else:
        falha("Organization sem founder ligado a Person")
    if isinstance(pes.get("worksFor"), dict) and pes["worksFor"].get("@id") == f"{BASE}/#organization":
        ok("Person aponta worksFor para a Organization")
    else:
        falha("Person sem worksFor ligado a Organization")

    if "LocalBusiness" not in json.dumps(grafo):
        ok("nenhum LocalBusiness (o IAieu nao e negocio local)")
    else:
        falha("LocalBusiness encontrado", "o IAieu nao e negocio local")


def teste_arquivo_historico():
    """Trava as decisoes de 13/08/2026 sobre as oito paginas de arquivo.

    Elas ficam acessiveis, mas nao podem voltar a competir com a home nova.
    Se alguem reindexar uma delas sem reescrever o conteudo, falha aqui.
    """
    sm = ler("sitemap.xml")
    sm_ativo = re.sub(r"<!--.*?-->", "", sm, flags=re.S)

    for arq in ARQUIVO_HISTORICO:
        html = ler(arq)

        if re.search(r'<meta name="robots" content="noindex, nofollow">', html):
            ok(f"{arq}: noindex, nofollow")
        else:
            falha(f"{arq}: sem noindex, nofollow", "e arquivo historico, nao pode indexar")

        # procura a tag, nao a palavra: o comentario do topo cita "hreflang"
        if re.search(r'<link[^>]+hreflang=', html):
            falha(f"{arq}: ainda tem hreflang",
                  "as versoes /en/ e /es/ dela estao bloqueadas")
        else:
            ok(f"{arq}: sem hreflang")

        if "application/ld+json" in html:
            falha(f"{arq}: ainda tem dado estruturado",
                  "declara ao robo um IAieu que nao existe mais")
        else:
            ok(f"{arq}: sem dado estruturado antigo")

        if f"{BASE}/{arq}" in sm_ativo:
            falha(f"{arq}: de volta ao sitemap", "arquivo historico fica fora")
        else:
            ok(f"{arq}: fora do sitemap")

        # Sair do percurso nao autoriza a pagina a quebrar: ela segue no ar.
        h1s = re.findall(r"<h1[^>]*>", html, flags=re.I)
        if len(h1s) == 1:
            ok(f"{arq}: H1 unico")
        else:
            falha(f"{arq}: {len(h1s)} H1", "deve haver exatamente um")

        sem_alt = [t for t in re.findall(r"<img[^>]*>", html, flags=re.I)
                   if "alt=" not in t.lower()]
        if sem_alt:
            falha(f"{arq}: {len(sem_alt)} imagem sem alt")
        else:
            ok(f"{arq}: todas as imagens com alt")

        sem_dim = [t for t in re.findall(r"<img[^>]*>", html, flags=re.I)
                   if "width=" not in t.lower() or "height=" not in t.lower()]
        if sem_dim:
            falha(f"{arq}: {len(sem_dim)} imagem sem width ou height",
                  "sem dimensao o layout salta enquanto carrega")
        else:
            ok(f"{arq}: todas as imagens com dimensao")

        if "<title>" in html and re.search(r"<title>\s*</title>", html):
            falha(f"{arq}: title vazio")
        else:
            ok(f"{arq}: title presente")


def teste_fora_do_percurso():
    """Paginas que existem mas nao representam mais o IAieu."""
    for arq in FORA_DO_PERCURSO:
        caminho = os.path.join(RAIZ, arq)
        if not os.path.exists(caminho):
            continue
        if re.search(r'<meta name="robots" content="noindex', ler(arq)):
            ok(f"{arq}: fora do percurso, com noindex")
        else:
            falha(f"{arq}: sem noindex", "esta acessivel e indexavel sem querer")


def teste_schema_so_da_identidade_nova():
    """Nenhuma pagina indexavel pode declarar produto ou FAQ descontinuados."""
    for arq in list(PAGINAS) + list(TRADUZIDAS):
        html = ler(arq)
        achados = [p for p in SCHEMA_PROIBIDO if p in html]
        if achados:
            falha(f"{arq}: schema com identidade antiga", ", ".join(achados))
        else:
            ok(f"{arq}: schema so da identidade atual")


def teste_assinatura_visual():
    """Trava a assinatura visual da home aprovada v7, de 14/08/2026.

    O circulo, o contorno em degrade e as duas linhas sao construidos por CSS,
    de proposito. A regra do dono e expressa: nao simplificar, nao redesenhar,
    nao substituir por outra decoracao e nao transformar em imagem. Se alguem
    apagar uma dessas construcoes, ou trocar a foto da pantera, falha aqui.
    """
    html = ler("index.html")

    for trecho, oq in ((".mark i {", "o circulo da marca"),
                       ("border-radius:50%", "o circulo e redondo"),
                       (".mark b {", "a barra da marca"),
                       (".hero-signature", "a assinatura do hero"),
                       ("conic-gradient", "o contorno em degrade"),
                       ("box-shadow:34px 0", "a segunda linha, paralela")):
        if trecho in html:
            ok(f"assinatura: {oq}")
        else:
            falha(f"assinatura sem {oq}", trecho)

    for cls in ("cover-school", "cover-career", "cover-marc",
                "cover-linkedin", "cover-plinio", "cover-ultra"):
        if f".{cls} " in html or f".{cls}{{" in html:
            ok(f"capa construida por CSS: {cls}")
        else:
            falha(f"capa ausente: {cls}", "as artes sao codigo, nao imagem")

    import hashlib
    caminho = os.path.join(RAIZ, "imagens/panther-eye-ultra.jpg")
    if not os.path.exists(caminho):
        falha("a foto da pantera sumiu", "imagens/panther-eye-ultra.jpg")
    else:
        with open(caminho, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        esperado = "338cf67c3fd14faa7bd5e922d51769880dd09cc525a162f4047428a9dd104eae"
        if digest == esperado:
            ok("pantera com o SHA-256 do arquivo aprovado")
        else:
            falha("a pantera foi alterada", f"sha256 {digest[:16]}")


def teste_favicon_p1():
    """Trava o pacote de icones aprovado em 14/08/2026.

    Confere que os arquivos existem, que as tres homes os declaram, que o SVG
    faz a troca de tema e que o manifest usa o nome oficial da marca. O pacote
    original vinha com "IAieu eVc" no campo name, que e nome de oferta
    descontinuada e nao pode voltar para a tela de ninguem.
    """
    for arq in FAVICON_P1:
        if os.path.exists(os.path.join(RAIZ, arq)):
            ok(f"icone presente: {arq}")
        else:
            falha(f"icone SUMIU: {arq}", "faz parte do pacote P1 aprovado")

    svg = ler("favicon.svg")
    for trecho, oq in (("#C1121F", "vermelho da marca"),
                       ("#111111", "filete preto no tema claro"),
                       ("prefers-color-scheme: dark", "troca de tema automatica"),
                       ('cx="16" cy="12" r="10"', "geometria do circulo"),
                       ('x="6" y="26" width="20" height="4"', "geometria do filete")):
        if trecho in svg:
            ok(f"favicon.svg com {oq}")
        else:
            falha(f"favicon.svg sem {oq}", trecho)

    man = json.loads(ler("site.webmanifest"))
    if man.get("name") == "IAieu":
        ok("manifest com o nome oficial da marca")
    else:
        falha("manifest com nome errado", f'achado "{man.get("name")}", esperado "IAieu"')
    if man.get("short_name") == "IAieu":
        ok("manifest com short_name correto")
    else:
        falha("manifest sem short_name IAieu")
    if "eVc" in json.dumps(man):
        falha("manifest cita eVc", "nome de oferta descontinuada")
    else:
        ok("manifest sem eVc")

    for arq in list(PAGINAS)[:1] + list(TRADUZIDAS):
        html = ler(arq)
        for tag, oq in (('href="/favicon.ico', "favicon.ico"),
                        ('href="/favicon.svg', "favicon.svg"),
                        ('href="/apple-touch-icon.png', "apple-touch-icon"),
                        ('href="/site.webmanifest', "manifest")):
            if tag in html:
                ok(f"{arq}: declara {oq}")
            else:
                falha(f"{arq}: nao declara {oq}")
        if "favicon-192.png" in html or "?v=3" in html:
            falha(f"{arq}: ainda aponta para o icone antigo")
        else:
            ok(f"{arq}: sem resquicio do icone antigo")


def teste_um_vermelho_so():
    """Nenhum ativo da marca pode usar um vermelho diferente do acento.

    O arquivo do logo veio com rgb(218,9,12), proximo mas nao igual ao
    #C1121F do site. Os dois conviviam na mesma tela. O dono decidiu em
    14/08/2026 que o vermelho do site predomina.
    """
    try:
        from PIL import Image
    except ImportError:
        aviso("sem Pillow, nao da para conferir o vermelho dos ativos")
        return
    import collections
    for arq in ATIVOS_DA_MARCA:
        caminho = os.path.join(RAIZ, arq)
        if not os.path.exists(caminho):
            falha(f"ativo da marca sumiu: {arq}")
            continue
        cores = collections.Counter(Image.open(caminho).convert("RGBA").getdata())
        cheios = [(k, v) for k, v in cores.items()
                  if k[3] == 255 and k[0] > 150 and k[1] < 70 and k[2] < 90]
        if not cheios:
            aviso(f"{arq}: sem vermelho cheio para conferir")
            continue
        tom = max(cheios, key=lambda x: x[1])[0][:3]
        if tom == ACENTO:
            ok(f"{arq}: acento #C1121F")
        else:
            falha(f"{arq}: vermelho fora do padrao",
                  f"achado rgb{tom}, esperado rgb{ACENTO}")


def teste_home_sem_faq():
    """A home nova nao tem FAQ. Decisao do Caetano em 13/08/2026.

    O teste antigo exigia FAQ espelhada 1:1 entre schema e texto visivel. Ele
    existia porque a home antiga tinha FAQ. Agora ele trava o contrario: se
    alguem devolver uma FAQ para a home, isso aparece aqui como falha, em vez
    de entrar sem ninguem perceber.
    """
    for arq in list(PAGINAS)[:1] + list(TRADUZIDAS):
        html = ler(arq)
        grafo = json.loads(blocos_jsonld(html)[0])["@graph"]
        if any(n.get("@type") == "FAQPage" for n in grafo):
            falha(f"{arq}: FAQPage no schema", "a home aprovada em 13/08/2026 nao tem FAQ")
        else:
            ok(f"{arq}: sem FAQPage, como a home aprovada define")


# ---------------------------------------------------------------- conteudo
def teste_conteudo_no_html_bruto():
    marcadores = {
        # Marcador trocado em 14/08/2026, com a home aprovada v7.
        "index.html": "A prova vem antes da explicação",
        # As linhas abaixo sao arquivo historico. Continuam checadas porque as
        # paginas seguem acessiveis e o conteudo delas nao pode sumir por acidente.
        "o-que-vendemos.html": "em função do problema",
        "sobre.html": "Quarenta anos",
        "projetos.html": "precisava resolver",
        "conteudos.html": "operação, processo, gestão",
        "depoimentos.html": "O que dizem",
    }
    for arq, marcador in marcadores.items():
        if marcador in texto_visivel(ler(arq)):
            ok(f"{arq}: conteudo essencial no HTML bruto")
        else:
            falha(f"{arq}: conteudo essencial ausente do HTML bruto", marcador)


def teste_regras_da_casa():
    for arq in (list(PAGINAS) + list(TRADUZIDAS) + ARQUIVO_HISTORICO
                + FORA_DO_PERCURSO + ["404.html", "llms.txt"]):
        caminho = os.path.join(RAIZ, arq)
        if not os.path.exists(caminho):
            continue
        conteudo = ler(arq)
        if "—" in conteudo:
            n = conteudo.count("—")
            falha(f"{arq}: {n} travessao", "regra da casa: zero travessao")
        else:
            ok(f"{arq}: sem travessao")

    visivel = " ".join(texto_visivel(ler(a)) for a in PAGINAS).lower()
    achadas = [p for p in PALAVRAS_PROIBIDAS if p in visivel]
    if achadas:
        aviso("palavras de jargao no texto visivel", ", ".join(achadas))
    else:
        ok("nenhuma palavra proibida no texto visivel")


# ---------------------------------------------------------------- infra
def teste_sitemap():
    sm = ler("sitemap.xml")
    # URL dentro de comentario XML nao esta no sitemap: ela esta preparada e
    # desativada. As versoes /en/ e /es/ ficam assim ate a traducao chegar.
    sm = re.sub(r"<!--.*?-->", "", sm, flags=re.S)
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    if len(locs) == len(set(locs)):
        ok(f"sitemap sem URL duplicada ({len(locs)} URLs)")
    else:
        falha("sitemap com URL duplicada")

    # As homes de /en/ e /es/ entraram no sitemap em 13/08/2026, quando foram
    # traduzidas e o noindex saiu delas. As outras dezoito paginas de /en/ e
    # /es/ continuam fora, dentro do comentario, porque ainda estao em
    # portugues. Nao acrescentar nenhuma aqui sem a traducao ter chegado.
    esperadas = set(PAGINAS.values()) | set(TRADUZIDAS.values())
    faltando = esperadas - set(locs)
    sobrando = set(locs) - esperadas
    if faltando:
        falha("sitemap incompleto", ", ".join(sorted(faltando)))
    else:
        ok("sitemap cobre todas as paginas publicas")
    if sobrando:
        falha("sitemap com URL que nao deveria estar la", ", ".join(sorted(sobrando)))

    for ruim in ("admin.html", "docs-geo", "?", "#"):
        if any(ruim in loc for loc in locs):
            falha("sitemap contem lixo", ruim)
    if not re.search(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", sm):
        falha("sitemap sem lastmod valido")
    else:
        ok("sitemap com lastmod no formato certo")


def teste_robots():
    r = ler("robots.txt")
    if "Sitemap: https://iaieu.com/sitemap.xml" in r:
        ok("robots aponta o sitemap")
    else:
        falha("robots sem Sitemap")

    for bot in ["GPTBot", "OAI-SearchBot", "ClaudeBot", "Claude-User",
                "PerplexityBot", "Google-Extended", "Applebot"]:
        if bot in r:
            ok(f"robots declara {bot}")
        else:
            falha(f"robots nao declara {bot}")

    for bloqueado in ["/admin.html", "/docs-geo/"]:
        if f"Disallow: {bloqueado}" in r:
            ok(f"robots bloqueia {bloqueado}")
        else:
            falha(f"robots nao bloqueia {bloqueado}")


def teste_admin_noindex():
    if not os.path.exists(os.path.join(RAIZ, "admin.html")):
        return
    if re.search(r'<meta name="robots" content="[^"]*noindex', ler("admin.html")):
        ok("admin.html com noindex")
    else:
        falha("admin.html sem noindex", "painel interno nao pode ser indexado")


def teste_indexnow():
    chaves = [f for f in os.listdir(RAIZ)
              if re.fullmatch(r"[0-9a-f]{32}\.txt", f)]
    if not chaves:
        aviso("sem arquivo de chave IndexNow na raiz")
        return
    arq = chaves[0]
    if ler(arq).strip() == arq.replace(".txt", ""):
        ok(f"chave IndexNow consistente ({arq})")
    else:
        falha("conteudo da chave IndexNow nao bate com o nome do arquivo")


def teste_llms():
    if not os.path.exists(os.path.join(RAIZ, "llms.txt")):
        aviso("sem llms.txt")
        return
    t = ler("llms.txt")
    if "experimental" in t.lower():
        ok("llms.txt traz o aviso de formato experimental")
    else:
        aviso("llms.txt sem o aviso de que o formato e experimental")
    if re.search(r"R\$\s*\d", t):
        falha("llms.txt cita preco", "precos nao sao publicos")
    else:
        ok("llms.txt sem preco")


# ---------------------------------------------------------------- main
def main():
    for teste in (
        teste_arquivos_intocaveis,
        teste_metadata,
        teste_estrutura,
        teste_jsonld,
        teste_entidades_da_home,
        teste_home_sem_faq,
        teste_favicon_p1,
        teste_um_vermelho_so,
        teste_arquivo_historico,
        teste_fora_do_percurso,
        teste_schema_so_da_identidade_nova,
        teste_assinatura_visual,
        teste_conteudo_no_html_bruto,
        teste_regras_da_casa,
        teste_sitemap,
        teste_robots,
        teste_admin_noindex,
        teste_indexnow,
        teste_llms,
    ):
        try:
            teste()
        except Exception as e:  # um teste quebrado nao derruba a bateria
            falha(f"erro ao rodar {teste.__name__}", repr(e))

    passou = [r for r in resultados if r[0] == "PASS"]
    avisos = [r for r in resultados if r[0] == "WARN"]
    falhou = [r for r in resultados if r[0] == "FAIL"]

    if falhou:
        print("\nFALHAS (precisam ser corrigidas antes de publicar)")
        for _, teste, detalhe in falhou:
            print(f"  FAIL  {teste}" + (f"  [{detalhe}]" if detalhe else ""))
    if avisos:
        print("\nAVISOS (nao impedem publicar, mas confira)")
        for _, teste, detalhe in avisos:
            print(f"  WARN  {teste}" + (f"  [{detalhe}]" if detalhe else ""))

    print(f"\n{len(passou)} PASS · {len(avisos)} WARN · {len(falhou)} FAIL")
    if falhou:
        print("\nNAO PUBLIQUE ate zerar as falhas.")
        sys.exit(1)
    print("\nTudo certo para publicar.")
    sys.exit(0)


if __name__ == "__main__":
    main()
