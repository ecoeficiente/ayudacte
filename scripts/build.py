"""Genera exclusivamente el sitio publicable, sin depender del repositorio del programa."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'


def main():
    quarto = shutil.which('quarto')
    if not quarto:
        raise SystemExit('Instala Quarto 1.10.18 y añade quarto a PATH.')
    # Únicamente se reemplaza esta salida generada; nunca fuentes ni directorios externos.
    if SITE.is_symlink() or SITE.resolve().parent != ROOT:
        raise SystemExit('Destino de compilación no seguro.')
    if SITE.exists():
        shutil.rmtree(SITE)
    shutil.copytree(ROOT / 'site', SITE)
    work = ROOT / '_work'
    work.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=work) as temporary:
        for guide in ('aplicacion', 'plugin'):
            stage = Path(temporary) / guide
            shutil.copytree(ROOT / guide, stage, ignore=shutil.ignore_patterns('_build', '.quarto'))
            subprocess.run([quarto, 'render', str(stage), '--to', 'html'], check=True)
            output = stage / '_build'
            target = SITE / guide
            shutil.copytree(output, target)
            # Quarto trata cada libro como raíz. Normalizar solo los enlaces
            # entre libros para que funcionen también en el servidor local.
            for html in target.rglob('*.html'):
                content = html.read_text(encoding='utf-8')
                for route in ('/', '/plugin/', '/aplicacion/'):
                    content = content.replace(
                        f'href="https://ayudacte.ecoeficiente.es{route}"',
                        f'href="{route}"')
                html.write_text(content, encoding='utf-8')
            for pdf in (ROOT / guide).glob('*.pdf'):
                shutil.copy2(pdf, target / pdf.name)
    (SITE / '.nojekyll').touch()
    subprocess.run([sys.executable, str(ROOT / 'scripts/check.py')], check=True)


if __name__ == '__main__':
    main()
