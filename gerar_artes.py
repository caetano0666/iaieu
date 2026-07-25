#!/usr/bin/env python3
"""
Gerador do manifesto da galeria de arte do IAieu.
Varre a pasta /artes/ e escreve /artes/artes.json.

Regras:
  - Arquivo de imagem solto em /artes/  -> item "single" (abre em modal).
  - Subpasta em /artes/ (ex: serie-01/) -> item "carousel" (abre com anterior/proximo).
  - Ignora nomes que comecam com "_" ou "." e o proprio artes.json.
  - Ordena por nome. Numere os arquivos (01, 02...) para controlar a ordem.

Uso: python3 gerar_artes.py   (rode a cada vez que adicionar/remover arte)
"""
import os, json, re

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "artes")
EXT = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")

def eh_imagem(nome):
    return nome.lower().endswith(EXT)

def ignorar(nome):
    return nome.startswith(("_", ".")) or nome == "artes.json"

def titulo(nome):
    base = re.sub(r"\.[^.]+$", "", nome)          # tira extensao
    base = re.sub(r"^\d+[-_\s]*", "", base)         # tira numero da frente
    base = base.replace("-", " ").replace("_", " ").strip()
    return base[:1].upper() + base[1:] if base else nome

def listar_imagens(pasta):
    itens = [n for n in os.listdir(pasta) if eh_imagem(n) and not ignorar(n)]
    return sorted(itens, key=str.lower)

def main():
    if not os.path.isdir(RAIZ):
        os.makedirs(RAIZ, exist_ok=True)
    entradas = sorted([n for n in os.listdir(RAIZ) if not ignorar(n)], key=str.lower)
    itens = []
    for nome in entradas:
        caminho = os.path.join(RAIZ, nome)
        if os.path.isdir(caminho):
            slides = listar_imagens(caminho)
            if not slides:
                continue
            itens.append({
                "tipo": "carousel",
                "titulo": titulo(nome),
                "capa": f"artes/{nome}/{slides[0]}",
                "slides": [f"artes/{nome}/{s}" for s in slides],
                "total": len(slides),
            })
        elif eh_imagem(nome):
            itens.append({
                "tipo": "single",
                "titulo": titulo(nome),
                "src": f"artes/{nome}",
            })
    saida = {"itens": itens, "total": len(itens)}
    with open(os.path.join(RAIZ, "artes.json"), "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False, indent=2)
    print(f"artes.json gerado: {len(itens)} itens "
          f"({sum(1 for i in itens if i['tipo']=='single')} avulsas, "
          f"{sum(1 for i in itens if i['tipo']=='carousel')} carrosseis)")

if __name__ == "__main__":
    main()
