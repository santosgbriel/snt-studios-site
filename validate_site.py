"""Valida o site estático sem depender de bibliotecas externas."""

from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"
BUILDER = ROOT / "build_site.py"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.assets: set[str] = set()
        self.inline_scripts: list[tuple[str, str]] = []
        self._script_type = ""
        self._script_src = ""
        self._script_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: value or "" for key, value in attrs}
        if tag in {"img", "script", "iframe", "source"} and attr.get("src"):
            self.assets.add(attr["src"])
        if tag == "link" and attr.get("href"):
            self.assets.add(attr["href"])
        if tag == "script" and not attr.get("src"):
            self._script_type = attr.get("type", "text/javascript")
            self._script_src = ""
            self._script_parts = []

    def handle_data(self, data: str) -> None:
        if self._script_parts is not None:
            self._script_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_parts is not None:
            self.inline_scripts.append((self._script_type, "".join(self._script_parts)))
            self._script_parts = None


def site_code_do_gerador() -> str:
    arvore = ast.parse(BUILDER.read_text(encoding="utf-8"), filename=str(BUILDER))
    for node in arvore.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "site_code" for target in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError("build_site.py não define site_code")


def caminho_local(valor: str) -> Path | None:
    parsed = urlparse(valor)
    if parsed.scheme or valor.startswith(("#", "data:", "mailto:", "tel:")):
        return None
    caminho = unquote(parsed.path).lstrip("/")
    return ROOT / caminho if caminho else None


def validar_javascript(scripts: list[tuple[str, str]]) -> None:
    node = shutil.which("node")
    if not node:
        raise AssertionError("Node.js não encontrado para validar o JavaScript")

    with tempfile.TemporaryDirectory(prefix="snt-site-") as pasta:
        temporarios = Path(pasta)
        for indice, (tipo, codigo) in enumerate(scripts, start=1):
            if tipo == "application/ld+json":
                json.loads(codigo)
                continue
            arquivo = temporarios / f"inline-{indice}.js"
            arquivo.write_text(codigo, encoding="utf-8")
            subprocess.run([node, "--check", str(arquivo)], check=True, capture_output=True, text=True)


def main() -> None:
    html = INDEX.read_text(encoding="utf-8")
    assert html == site_code_do_gerador(), "index.html está diferente do conteúdo gerado por build_site.py"

    obrigatorios = (
        '<link rel="canonical" href="https://www.sntstudios.com/">',
        "63.223.844/0001-11",
        "/api/studios/public/cotacao",
        'id="resultadoCotacao"',
        "assets/og-cover.jpg",
        "assets/site.css",
        ".webp",
    )
    for trecho in obrigatorios:
        assert trecho in html, f"conteúdo obrigatório ausente: {trecho}"

    proibidos = (
        "38.650.087/0001-08",
        "snt-lavanderia-bot-production.up.railway.app/studios\"",
        "STONE_API_KEY_AQUI",
        "confirmarReservaStone",
        "cdn.tailwindcss.com",
        "assets/fotos/20251030_162521(1).jpg",
    )
    for trecho in proibidos:
        assert trecho not in html, f"conteúdo proibido encontrado: {trecho}"

    parser = SiteParser()
    parser.feed(html)
    # As fotos da galeria vivem em listas JavaScript e não aparecem como src
    # até o visitante abrir o modal. Incluí-las aqui impede publicar uma
    # galeria que só quebra depois do clique.
    parser.assets.update(re.findall(r"assets/[A-Za-z0-9_()./\-]+\.(?:webp|jpg|png)", html))
    ausentes = sorted(str(path.relative_to(ROOT)) for asset in parser.assets if (path := caminho_local(asset)) and not path.is_file())
    assert not ausentes, "arquivos referenciados não existem: " + ", ".join(ausentes)
    validar_javascript(parser.inline_scripts)

    print(f"Site válido: {len(parser.assets)} recursos e {len(parser.inline_scripts)} scripts verificados.")


if __name__ == "__main__":
    main()
