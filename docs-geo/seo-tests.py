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

PAGINAS = {
    "index.html": f"{BASE}/",
    "o-que-vendemos.html": f"{BASE}/o-que-vendemos.html",
    "iaieu-evc.html": f"{BASE}/iaieu-evc.html",
    "iaieu-mais.html": f"{BASE}/iaieu-mais.html",
    "iaieu-go.html": f"{BASE}/iaieu-go.html",
    "sobre.html": f"{BASE}/sobre.html",
    "projetos.html": f"{BASE}/projetos.html",
    "conteudos.html": f"{BASE}/conteudos.html",
    "arte.html": f"{BASE}/arte.html",
    "depoimentos.html": f"{BASE}/depoimentos.html",
    "plinio/index.html": f"{BASE}/plinio/",
    "stw-daryl-lucas/index.html": f"{BASE}/stw-daryl-lucas/",
}

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
    for arq in PAGINAS:
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
    esperados = [
        f"{BASE}/#organization",
        f"{BASE}/#person-caetano",
        f"{BASE}/#website",
        f"{BASE}/#faq",
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


def teste_faq_espelhada():
    html = ler("index.html")
    grafo = json.loads(blocos_jsonld(html)[0])["@graph"]
    faq = next((n for n in grafo if n.get("@type") == "FAQPage"), None)
    if not faq:
        falha("home sem FAQPage")
        return

    visivel = texto_visivel(html)
    perguntas = [q["name"] for q in faq.get("mainEntity", [])]
    respostas = [q["acceptedAnswer"]["text"] for q in faq.get("mainEntity", [])]

    if not perguntas:
        falha("FAQPage sem perguntas")
        return

    faltando = [p for p in perguntas if p not in visivel]
    if faltando:
        falha("FAQ do schema nao esta visivel na pagina",
              f"{len(faltando)} pergunta(s): {faltando[:2]}")
    else:
        ok(f"FAQ espelhada 1:1 ({len(perguntas)} perguntas visiveis)")

    resp_faltando = [r for r in respostas if r[:60] not in visivel]
    if resp_faltando:
        falha("resposta do schema nao esta visivel", f"{len(resp_faltando)} resposta(s)")
    else:
        ok("todas as respostas do schema estao visiveis")


# ---------------------------------------------------------------- conteudo
def teste_conteudo_no_html_bruto():
    marcadores = {
        "index.html": "Está sem direção",
        "o-que-vendemos.html": "Vendo direção",
        "sobre.html": "O que o IAieu faz",
        "projetos.html": "construí",
        "conteudos.html": "quem sabe usar",
        "depoimentos.html": "Nomes reais",
    }
    for arq, marcador in marcadores.items():
        if marcador in texto_visivel(ler(arq)):
            ok(f"{arq}: conteudo essencial no HTML bruto")
        else:
            falha(f"{arq}: conteudo essencial ausente do HTML bruto", marcador)


def teste_regras_da_casa():
    for arq in list(PAGINAS) + ["404.html", "llms.txt"]:
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
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    if len(locs) == len(set(locs)):
        ok(f"sitemap sem URL duplicada ({len(locs)} URLs)")
    else:
        falha("sitemap com URL duplicada")

    esperadas = set(PAGINAS.values())
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
        teste_faq_espelhada,
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
