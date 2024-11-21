
<h1 align="center">BaseCrack-W</h1>  
<h4 align="center">A Decoder Based on Multiple Encoding Formats</h4>  
<p align="center">Original author: https://github.com/mufeedvh/basecrack</p>

**BaseCrack-W** is an upgraded Python-based encoding and decoding tool that supports a wide range of character encoding schemes. The tool extends the capabilities of conventional encoding handling and adds support for `Base45` and various improved decoding strategies. It is specifically designed for **CTF challenges**, fast, reliable, and modular!

---

## 📑 **Table of Contents**  

- [Features](#features)  
- [Supported Encoding Schemes](#supported-encoding-schemes)  
- [Installation](#installation)  
- [Usage](#usage)  
    - [Linux Usage Instructions](#linux-usage-instructions)  
    - [Windows Usage Instructions](#windows-usage-instructions)  
- [API Support](#api-support)  
- [Contributing](#contributing)  
- [License](#license)  

---

## ✨ **Features**  

- Automatically detects and decodes multiple encoding formats.  
- **New Base45 support** extends common encoding schemes.  
- Batch decode multi-layered nested encoded strings.  
- Supports multiple modes: user input mode, API call mode, image processing mode.  
- Handles encoding data with Unicode replacement characters or non-ASCII data.  
- Provides detailed decoding process output in the command line for debugging and analysis.  

---

## 🔑 **Supported Encoding Schemes**  

- Base16  
- Base32  
- Base32hex  
- Base32z  
- Base36  
- Base38  
- Base45  
- Base58  
- Base62  
- Base64 / Base64URL  
- Base85 / Ascii85  
- Base91  
- Base92  
- Base100  
- **Base128**  
- Z85  

---

## ⚙️ **Installation**  

### **1. Clone the repository**  
```bash  
git clone https://github.com/ha0/BaseCrack-W.git  
cd BaseCrack-W  
```  

### **2. Install dependencies**  
```bash  
pip install -r requirements.txt  
```  

---

## 🚀 **Usage Instructions**  

### **Linux Usage Instructions**  

1. **Decode a single string**  
    ```bash  
    python3 basecrack.py -b SGVsbG8gV29ybGQh  
    ```  

2. **Decode from a file**  
    ```bash  
    python3 basecrack.py -f encoded_file.txt  
    ```  

3. **Magic mode: Decode multi-layer nested encodings**  
    ```bash  
    python3 basecrack.py -m "multi-layer nested encoded string"  
    ```  

### **Windows Usage Instructions**  

1. **Decode a single string**  
    Open Command Prompt, navigate to the project directory, and run the following command:  
    ```cmd  
    python basecrack.py -b SGVsbG8gV29ybGQh  
    ```  

2. **Decode from a file**  
    ```cmd  
    python basecrack.py -f encoded_file.txt  
    ```  

3. **Magic mode: Decode multi-layer nested encodings**  
    ```cmd  
    python basecrack.py -m "multi-layer nested encoded string"  
    ```  

For image input in **EXIF/OCR** detection mode **(-i/--image)**:  
        (--exif/--ocr)

**EXIF Data**: Decode image EXIF data **(-e/--exif)**:  
    python basecrack.py -i image.jpg --exif  

**OCR-based encoding detection**: Use OCR to detect base encoding in images **(-c/--ocr)**:  
    python basecrack.py -i image.jpg --ocr  

**Note**: Windows users should ensure that `python` is properly installed and added to the system path. If not installed, download and install it from the [Python official website](https://www.python.org/downloads/).  

---

## 📜 **API Support**  

BaseCrack-W provides a flexible API that can be easily integrated into other projects.  

**Sample Code**:  
```python  
from decoder import DecodeBase  

encoded_str = "SGVsbG8gV29ybGQh"  # Base64 encoded string  
decoder = DecodeBase(encoded_base=encoded_str)  
types, results = decoder.decode()  

print("Decoded types:", types)  
print("Decoded results:", results)  
```  

---

## 🤝 **Contributing**  

We welcome all developers interested in the project! You can contribute by:  
- Submitting new feature suggestions or optimizations.  
- Fixing code issues and submitting a Pull Request.  
- Improving documentation.  

Before submitting a PR, please ensure all unit tests pass:  
```bash  
python -m unittest discover -v  
```  

---

## 📜 **License**  

This project is open-source under the [MIT License](./LICENSE). Please refer to the LICENSE file for more details.  

## ❤️ **Support the Author**  

If you find this project useful, please star 🌟 the repository or share it with others. Thank you for your support!  

---

Note❗  
Decoding errors may occur if the encryption itself is not base encoding but is recognized as Base36. Please use your judgment.  

---
