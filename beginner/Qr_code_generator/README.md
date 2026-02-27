📦 QR Code Generator
A lightweight Python utility that generates QR codes from text or URLs and saves them as image files.

📖 Description
This script creates a QR code from a given input string (e.g., URL, text, ID) and saves it as a PNG image in the current working directory.
It is minimal, configurable, and suitable for:
Automation scripts
Backend utilities
Quick QR generation tools
Integration into larger systems

✨ Features
Generate QR codes from any text input
Configurable QR parameters:
Version
Error correction level
Box size
Border size
Fill color
Saves output as PNG
Simple functional structure
Clean, reusable design

⚙️ How It Works
Initializes a QRCode object with specified configuration.
Adds input text to the QR object.
Generates the QR matrix.
Creates an image with chosen colors.
Saves the image to the specified file name.

🚀 Installation
1️⃣ Clone the repository
git clone (https://github.com/Sankethhhhhhh/Mini-project.git)
cd Mini-project/beginner/Qr_code_generator
2️⃣ Install dependencies
pip install qrcode[pil]
3️⃣ Verify Python version
python --version

Python 3.x required.

▶️ Usage
Basic Usage
Modify the input text and file name inside main.py:
text = "https://example.com"
file_name = "qr_code.png"

Run:
python main.py
The generated QR image will be saved in the same directory where the script is executed.

📦 Requirements
Python 3.x
qrcode library
Pillow (installed automatically with qrcode[pil])

🧪 Example
Input
text = "https://www.linkedin.com/in/sanketh-s-57a152293/"
file_name = "qr_code.png"
Output
qr_code.png
The file will contain a QR code encoding the specified URL.

📁 Project Structure
qr_code_gen/
├── main.py
└── README.md
🔧 Customization Options

You can adjust:

version=1
error_correction=qrcode.constants.ERROR_CORRECT_L
box_size=10
border=4
fill_color="#6aff9b"
back_color="white"

For higher data capacity or resilience, increase version or use:

ERROR_CORRECT_M
ERROR_CORRECT_Q
ERROR_CORRECT_H

📜 License

This project is licensed under the MIT License.