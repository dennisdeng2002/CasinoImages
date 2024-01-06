# convert originals/NHRB.jpg -resize 400 resized/NHRB.jpg

from os import scandir
import subprocess

input_paths = ['large']
output_paths = ['small']
widths = [300]
resize_template = 'convert {}/{} -resize {} {}/{}'

for i, input_path in enumerate(input_paths):
    total_count = 0
    for entry in scandir(input_path):
        if entry.path.endswith('.jpg') and entry.is_file():
            total_count = total_count + 1

    counter = 1
    output_path, width = output_paths[i], widths[i]
    for entry in scandir(input_path):
        if entry.path.endswith('.jpg') and entry.is_file():
            name = entry.name
            resize = resize_template.format(input_path, name, width, output_path, name).split()
            subprocess.run(resize)
            print("Processed {}/{}".format(counter, total_count))
            counter = counter + 1