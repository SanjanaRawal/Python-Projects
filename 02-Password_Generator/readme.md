# 🔐 Password Generator
This is a simple Python script that generates a secure password of user-defined length using a combination of uppercase and lowercase letters, digits and special characters.

## 📋 Features
* User inputs desired password length 
* Password includes:
1. [ ] Uppercase letters (A-Z)
2. [ ] Lowercase letters (a-z)
3. [ ] Numbers (0-9)
4. [ ] Special characters (e.g. !@#$%^&*)

## 🧑‍💻 Requirements
* Python 3.10.6
* No external libraries are required—only Python's built-in random and string modules are used.

## 🚀 How to Use
1. Clone or download this repository.
2. Run the script :  
python Password_Generator.py
3. Enter the desired password length when prompted. 
4. The generated password will be displayed in the console.

### Example 1
Enter password length : 10  
Your password is: eol;fVz<jv

### Example 2
Enter password length : 2  
Password length must be greater than 3

## ⚠️ Note
* The generated password is printed to the console and not stored or saved.
* This script generates a completely random password without guaranteed inclusion of each character type (e.g., it might generate a password without digits, though rarely)

## 🚀 Future Improvements
* Ensure character variety (at least one uppercase, lowercase, digit and symbol)
* Password strength indicator
* Customizable options (e.g., include/exclude symbols or similar characters)
* Save to file or clipboard