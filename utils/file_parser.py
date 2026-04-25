from PyPDF2 import PdfReader
from docx import Document
import markdown

def parse_uploaded_file(uploaded_file):
    """解析上传的文件，返回纯文本"""
    file_type = uploaded_file.name.split('.')[-1].lower()
    text = ""

    try:
        if file_type == 'pdf':
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text() + "\n"

        elif file_type == 'docx':
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"

        elif file_type in ['md', 'txt']:
            text = uploaded_file.read().decode('utf-8')

        return text.strip() if text else "无法解析文件内容"
    except Exception as e:
        return f"文件解析失败：{str(e)}"