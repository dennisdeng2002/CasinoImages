import os

def rename_jpeg_to_jpg_in_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_name, file_extension = os.path.splitext(filename)
                if file_extension.lower() == '.jpeg':
                    new_file_path = os.path.join(folder_path, file_name + '.jpg')
                    os.rename(file_path, new_file_path)
                    print(f'File renamed from {file_path} to {new_file_path}')

folder_path = 'original'
rename_jpeg_to_jpg_in_folder(folder_path)