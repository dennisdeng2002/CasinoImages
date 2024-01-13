import json
from os import scandir

ids = set()

with open('casinos.txt', 'r') as file:
    for line in file:
        ids.add(line.split(',')[0])

for entry in scandir('original'):
    if entry.path.endswith('.jpg') and entry.is_file():
        id = entry.name.replace('.jpg', '')
        if id not in ids:
            print(id)