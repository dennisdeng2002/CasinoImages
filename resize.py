from os import scandir
import subprocess

input_path = 'original'
output_paths = ['small', 'medium']
widths = [200, 600]
# convert original/ACCR.jpg -resize 600 -quality 50 medium/ACCR.webp
resize_template = 'convert {}/{}.jpg -resize {} -quality 50 {}/{}.webp'

for i, output_path in enumerate(output_paths):
    total_count = 0
    for entry in scandir(input_path):
        if entry.path.endswith('.jpg') and entry.is_file():
            total_count = total_count + 1

    counter = 1
    width = widths[i]
    print("Processing {} images".format(output_path))
    for entry in scandir(input_path):
        if entry.path.endswith('.jpg') and entry.is_file():
            name = entry.name.replace('.jpg', '')
            resize = resize_template.format(input_path, name, width, output_path, name).split()
            subprocess.run(resize)
            print("Processed {}/{}".format(counter, total_count))
            counter = counter + 1
    
    print("")