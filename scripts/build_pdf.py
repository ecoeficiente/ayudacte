"""Regenera los PDF desde las fuentes actuales; revisar visualmente antes de publicar."""
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
work = ROOT / '_work'
work.mkdir(exist_ok=True)
for guide, name in [('aplicacion', 'Manual-de-usuario-DesignBuilder-CTE-v3.pdf'),
                    ('plugin', 'Guia-del-plugin-DesignBuilder-CTE.pdf')]:
    with tempfile.TemporaryDirectory(dir=work) as temporary:
        stage = Path(temporary) / guide
        shutil.copytree(ROOT / guide, stage, ignore=shutil.ignore_patterns('_build', '.quarto', '*.pdf'))
        subprocess.run(['quarto', 'render', '--to', 'typst'], cwd=stage, check=True)
        pdfs = list((stage / '_build').glob('*.pdf'))
        if len(pdfs) != 1:
            raise RuntimeError(f'Se esperaba un PDF para {guide}: {pdfs}')
        shutil.copy2(pdfs[0], ROOT / guide / name)
