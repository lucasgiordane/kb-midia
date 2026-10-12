"""Gera os PNGs de um post a partir do slides.html dele.

Uso:
    python3 gerador/render.py posts/2026-10-14_pre-treino-mounjaro

Cada elemento .kb-arte do slides.html vira um PNG. A pasta de saída vem do
atributo data-tipo do <body> (carrossel, reels, stories ou capas) e do mês do
nome do post: carrossel/2026-10/2026-10-14_pre-treino-mounjaro_01.png
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
TIPOS = {"carrossel", "reels", "stories", "capas"}


def render(pasta_post: Path) -> list[Path]:
    slides = pasta_post / "slides.html"
    if not slides.exists():
        sys.exit(f"Não achei {slides}")
    nome = pasta_post.name
    mes = nome[:7]  # AAAA-MM
    saidas = []
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pagina.goto(slides.resolve().as_uri())
        pagina.evaluate("document.fonts.ready")
        tipo = pagina.get_attribute("body", "data-tipo") or "carrossel"
        if tipo not in TIPOS:
            sys.exit(f"data-tipo inválido: {tipo}")
        destino = RAIZ / tipo / mes
        destino.mkdir(parents=True, exist_ok=True)
        for antigo in destino.glob(f"{nome}_*.png"):
            antigo.unlink()
        artes = pagina.query_selector_all(".kb-arte")
        for i, arte in enumerate(artes, start=1):
            arquivo = destino / f"{nome}_{i:02d}.png"
            arte.screenshot(path=str(arquivo))
            saidas.append(arquivo)
        navegador.close()
    return saidas


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    for arquivo in render(Path(sys.argv[1])):
        print(arquivo.relative_to(RAIZ))
