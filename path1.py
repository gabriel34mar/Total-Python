from pathlib import Path

base = Path(__file__).parent      # carpeta donde está el script
guide = base / 'Europe'           # subcarpeta Europe

for txt in guide.glob('**/*.txt'):
    print(txt)
