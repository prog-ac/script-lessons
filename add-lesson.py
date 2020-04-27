import sys
from pathlib import Path
import shutil

lesson = sys.argv[1]
Path(lesson).mkdir(exist_ok=True)
files = ['main.rb', 'main.php', 'main.py', 'main.js','README.md']

for file in files:
  print(file)
  Path('{}/{}'.format(lesson,file)).touch(exist_ok=True)

shutil.copy(Path('templates/README.md'), Path('{}/README.md'.format(lesson)))