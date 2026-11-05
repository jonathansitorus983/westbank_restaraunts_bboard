"""Package only explicit application source files; never include hosting state."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
files = ['package.json', 'package-lock.json', 'index.html', 'vite.config.js',
         'LICENSE', 'README.md', 'THIRD_PARTY_NOTICES.md',
         'src/main.jsx', 'src/style.css', 'scripts/package-source.py']
out = root / 'public' / 'west-bank-table-source.zip'
out.parent.mkdir(exist_ok=True)
with ZipFile(out, 'w', ZIP_DEFLATED) as archive:
    for name in files:
        archive.write(root / name, 'west-bank-table/' + name)
print(out)
