"""Comprueba páginas, recursos, anclas y búsqueda local antes de publicar."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

SITE = Path(__file__).resolve().parents[1] / '_site'
HOST = 'ayudacte.ecoeficiente.es'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])


def main():
    errors = []
    pages = {p.resolve(): Page(p) for p in SITE.rglob('*.html')}
    checked = 0

    def check_link(origin, link):
        nonlocal checked
        url = urlsplit(link)
        if url.scheme == 'file' or url.hostname in ('localhost', '127.0.0.1'):
            errors.append(f'Ruta local publicada: {origin.name}: {link}')
            return
        if (url.scheme or url.netloc) and url.hostname != HOST:
            return
        path = unquote(url.path)
        target = (SITE / path.lstrip('/') if path.startswith('/') else origin.parent / path).resolve() if path else origin
        if target.is_dir():
            target = target / 'index.html'
        checked += 1
        if not target.is_relative_to(SITE.resolve()) or not target.is_file():
            errors.append(f'Destino ausente: {origin.relative_to(SITE)}: {link}')
        elif url.fragment and target.suffix == '.html':
            if target not in pages:
                pages[target] = Page(target)
            if unquote(url.fragment) not in pages[target].ids:
                errors.append(f'Ancla ausente: {origin.name}: {link}')

    for path, page in list(pages.items()):
        for link in page.links:
            check_link(path, link)
    for guide, expected in (('aplicacion', 13), ('plugin', 5)):
        folder = SITE / guide
        content = [folder / 'index.html', *sorted((folder / 'capitulos').glob('*.html'))]
        if len(content) != expected or not all(p.is_file() for p in content):
            errors.append(f'{guide}: se esperan {expected} páginas de contenido')
        search = folder / 'search.json'
        entries = json.loads(search.read_text(encoding='utf-8')) if search.exists() else []
        if not entries:
            errors.append(f'{guide}: falta índice de búsqueda')
        for entry in entries:
            check_link(folder / 'index.html', entry['href'])
        print(f'{guide}: {len(content)} páginas, {len(entries)} entradas de búsqueda')
    for p in SITE.rglob('*'):
        if p.is_file() and (p.suffix.lower() in {'.qmd', '.md', '.py', '.yml', '.typ', '.docx', '.scss'} or p.name.startswith('.git')):
            errors.append('Archivo interno publicado: ' + str(p.relative_to(SITE)))
    if not (SITE / 'index.html').is_file():
        errors.append('Falta la portada')
    if (SITE / 'CNAME').read_text(encoding='utf-8').strip() != HOST:
        errors.append('Dominio incorrecto')
    print(f'{checked} referencias locales comprobadas; {len(errors)} errores')
    for error in sorted(set(errors)):
        print(error)
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
