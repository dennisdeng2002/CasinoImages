from os import scandir

input_path = 'original'
sqlite_template = 'INSERT INTO casino_image (id) VALUES (\'{}\');\n'

ids = []
for entry in scandir(input_path):
	if entry.path.endswith('.jpg') and entry.is_file():
		id = entry.name.replace('.jpg', '')
		ids.append(id)

f = open('casino_image.sql', 'w')
for id in sorted(ids):
	sqlite = sqlite_template.format(id)
	f.write(sqlite)