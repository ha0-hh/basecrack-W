<h1 align="center">BaseCrack-W</h1>  
<h4 align="center">Decoder for Multiple Encoding Formats</h4>  
<p align="center">Original author: https://github.com/mufeedvh/basecrack</p>
**BaseCrack-W** is an enhanced version of the Python-based encoding and decoding tool that supports a wide range of character encoding schemes. This tool expands the handling capabilities of conventional encodings and adds support for `Base45` and various improved decoding strategies. It is specifically designed for **CTF challenges**, fast, reliable, and modular!

---  

## 📑 **Table of Contents**  

- [Features](#features)  
- [Supported Encoding Schemes](#supported-encoding-schemes)  
- [Installation](#installation)  
- [Usage](#usage)  
    - [Linux Usage](#linux-usage)  
    - [Windows Usage](#windows-usage)  
- [API Support](#api-support)  
- [Contributions](#contributions)  
- [License](#license)  

---  

## ✨ **Features**  

- Automatically detects and decodes multiple encoding formats.  
- **New Base45 support** extending common encoding schemes.  
- Supports batch decoding of multi-layer nested encoded strings.  
- Supports various modes: user input mode, API calling mode, and image processing mode.  
- Handles encoded data with Unicode replacement characters or non-ASCII data.  
- Outputs detailed decoding processes in the command line for debugging and analysis.  

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
