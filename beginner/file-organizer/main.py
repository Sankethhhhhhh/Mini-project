import os
import shutil

# Specify the directory to organize
directory = os.path.join(os.getcwd(), "file_organizer")

# Create a dictionary to hold file extensions
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

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Organize files
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = filename.split('.')[-1].lower()

    if extension in file_extensions:
        folder_name = file_extensions[extension]
        folder_path = os.path.join(directory, folder_name)

        # Create folder if not exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        destination = os.path.join(folder_path, filename)

        # Handle duplicate file names
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(folder_path, f"{base}_{counter}{ext}")):
                counter += 1
            destination = os.path.join(folder_path, f"{base}_{counter}{ext}")

        # Move file
        shutil.move(file_path, destination)

print("Files organized successfully.")