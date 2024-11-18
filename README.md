<h1 align="center">BaseCrack-W</h1>  
<h4 align="center">基于多种编码格式的解码器</h4>  

**BaseCrack-W** 是一个基于 Python 的升级版编码解码工具，支持广泛的字符编码方案。该工具扩展了常规编码的处理能力，新增支持 `Base45` 和多种改进解码策略。专为**CTF 挑战**设计，快速、可靠、模块化！  

---  

## 📑 **目录**  

- [功能](#功能)  
- [支持的编码方案](#支持的编码方案)  
- [安装](#安装)  
- [使用方法](#使用方法)  
    - [Linux 使用说明](#linux-使用说明)  
    - [Windows 使用说明](#windows-使用说明)  
- [API 支持](#api-支持)  
- [贡献](#贡献)  
- [许可证](#许可证)  

---  

## ✨ **功能**  

- 自动检测并解码多种编码格式。  
- **新增 Base45 支持**，扩展常见编码方案。  
- 可批量解码多重嵌套的编码字符串。  
- 支持多种模式：用户输入模式、API 调用模式、图像处理模式。  
- 处理包含 Unicode 替换字符或非 ASCII 数据的编码数据。  
- 在命令行输出详细的解码过程，便于调试和分析。  

---  

## 🔑 **支持的编码方案**  

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

## ⚙️ **安装**  

### **1. 克隆仓库**  
```bash  
git clone https://github.com/ha0/BaseCrack-W.git  
cd BaseCrack-W  
```  

### **2. 安装依赖**  
```bash  
pip install -r requirements.txt  
```  

---  

## 🚀 **使用方法**  

### **Linux 使用说明**  

1. **解码单个字符串**  
    ```bash  
    python3 basecrack.py -b SGVsbG8gV29ybGQh  
    ```  

2. **从文件解码**  
    ```bash  
    python3 basecrack.py -f encoded_file.txt  
    ```  

3. **魔法模式：多层嵌套编码解码**  
    ```bash  
    python3 basecrack.py -m "多层嵌套编码字符串"  
    ```  

### **Windows 使用说明**  

1. **解码单个字符串**  
    打开命令提示符，进入项目目录，运行以下命令：  
    ```cmd  
    python basecrack.py -b SGVsbG8gV29ybGQh  
    ```  

2. **从文件解码**  
    ```cmd  
    python basecrack.py -f encoded_file.txt  
    ```  

3. **魔法模式：多层嵌套编码解码**  
    ```cmd  
    python basecrack.py -m "多层嵌套编码字符串"  
    ```  

输入图片为 **EXIF/OCR** 检测模式 **(-i/--image)**：

        (--exif/--ocr)

**EXIF 数据**：解码图像 EXIF 数据 **(-e/--exif)**：

    python basecrack.py -i image.jpg --exif

**OCR 基编码检测**：使用 OCR 检测图像中的基编码 **(-c/--ocr)**：

    python basecrack.py -i image.jpg --ocr


**注意：** Windows 用户需要确保 `python` 已正确安装并配置到系统路径中。如果没有安装，请从 [Python 官方网站](https://www.python.org/downloads/) 下载并安装。  

---  

## 📜 **API 支持**  

BaseCrack-W 提供灵活的 API，可以轻松集成到其他项目中。  

**示例代码：**  
```python  
from decoder import DecodeBase  

encoded_str = "SGVsbG8gV29ybGQh"  # Base64 编码字符串  
decoder = DecodeBase(encoded_base=encoded_str)  
types, results = decoder.decode()  

print("解码类型:", types)  
print("解码结果:", results)  
```  

---  

## 🤝 **贡献**  

我们欢迎所有对项目感兴趣的开发者！您可以通过以下方式贡献：  
- 提交新功能建议或优化。  
- 修复代码问题并提交 Pull Request。  
- 改进文档。  

提交 PR 前，请确保所有单元测试通过：  
```bash  
python -m unittest discover -v  
```  

---  

## 📜 **许可证**  

本项目基于 [MIT 许可证](./LICENSE) 开源，详情参阅许可证文件。  

## ❤️ **支持作者**  

如果觉得本项目对您有帮助，请点亮 🌟 Star 或分享给更多人。感谢支持！  
---  
注意❗
解码可能出现错误，比如加密本身不为base但是会被识别为base36，请自行判断。
---  
