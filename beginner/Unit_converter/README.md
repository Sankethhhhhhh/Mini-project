🔄 Unit Converter
A Python-based command-line application that converts values between different units across multiple categories such as length, weight, and temperature.

📖 Description
This project provides a modular unit conversion system implemented in Python.
It allows users to select a category, input a value, specify source and target units, and receive the converted result.
The application uses base-unit normalization for accurate and scalable conversions.

✨ Features
Supports multiple unit categories
Modular conversion functions
Base-unit normalization approach
Temperature conversion with proper formula handling
Lightweight and dependency-free
Easy to extend with additional units

📁 Supported Categories
📏 Length
m (meter)
km (kilometer)
cm (centimeter)
mm (millimeter)
inch
foot

⚖️ Weight
kg (kilogram)
g (gram)
lb (pound)
🌡 Temperature
C (Celsius)
F (Fahrenheit)
K (Kelvin)

⚙️ How It Works
User selects a conversion category.
User enters a numeric value.
User specifies source and target units.
The program converts the value using:
Base-unit normalization (for length & weight)
Formula-based conversion (for temperature)
The result is displayed in the terminal.

🚀 Installation

Clone the repository:
git clone https://github.com/yourusername/Mini-project.git
cd Mini-project/beginner/unit_converter

Make sure Python 3 is installed:
python --version

▶️ Usage
Run the script:
python main.py

Example input:
Enter category: length
Enter value: 5
From unit: km
To unit: m

Output:
Result: 5000.0

🧪 Example
Input
Category: temperature
Value: 100
From unit: C
To unit: F
Output
Result: 212.0

📦 Requirements
Python 3.x
No external libraries required

Uses only:
os
Standard Python functions

📜 License
This project is licensed under the MIT License.