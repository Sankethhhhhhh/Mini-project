import os
import shutil

directory = os.path.join(os.getcwd(), "file_organizer")

file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos'
}

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isdir(file_path):
        continue

    extension = filename.split('.')[-1].lower()

    if extension in file_extensions:
        folder_name = file_extensions[extension]
        folder_path = os.path.join(directory, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        destination = os.path.join(folder_path, filename)

        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(folder_path, f"{base}_{counter}{ext}")):
                counter += 1
            destination = os.path.join(folder_path, f"{base}_{counter}{ext}")

       
        shutil.move(file_path, destination)

print("Files organized successfully.")