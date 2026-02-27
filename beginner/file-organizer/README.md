📂 File Organizer
A simple Python script that automatically organizes files in a directory by sorting them into categorized folders based on file extensions.

📖 Description
This script scans a specified directory (file_organizer folder in the current working directory) and moves files into appropriate subfolders based on their type. It helps maintain a clean and structured file system.

✨ Features
Automatic file organization
Supports multiple file types
Prevents duplicate overwriting (auto-renames files)
Creates category folders dynamically
Uses only Python standard library modules

📁 Supported File Types
Category	Extensions
Images	png, jpg, jpeg, gif
PDFs	pdf
Documents	doc, docx, txt
Data	csv, xlsx
Archives	zip, rar
Executables	exe
Music	mp3, wav
Videos	mp4, avi, flv, wmv

⚙️ How It Works
Targets the file_organizer folder inside the current working directory.
Iterates through all files in the folder.
Extracts each file’s extension.
Matches the extension to a predefined category.
Creates the category folder if it does not exist.
Moves the file into the correct folder.
Renames the file if a duplicate exists.

🚀 Installation
Clone the repository:
git clone (https://github.com/Sankethhhhhhh/Mini-project.git)
cd Mini-project/beginner/file-organiser

Ensure Python 3 is installed:
python --version

▶️ Usage
Place files you want to organize inside the file_organizer folder.

Run the script:
python main.py

Check the file_organizer directory to see organized files.

📦 Requirements
Python 3.x
No external libraries required

Uses only:
-os
-shutil

🧪 Example
Before Running:
file_organizer/
├── document.pdf
├── photo.jpg
├── song.mp3
├── data.csv
└── video.mp4

After Running:
file_organizer/
├── PDFs/
│   └── document.pdf
├── Images/
│   └── photo.jpg
├── Music/
│   └── song.mp3
├── Data/
│   └── data.csv
└── Videos/
    └── video.mp4


📜 License
This project is licensed under the MIT License.