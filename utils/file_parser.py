from PyPDF2 import PdfReader
from docx import Document
import os

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def parse_uploaded_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()
    text = ""
    original_pdf_path = os.path.join(CACHE_DIR, "original_resume.pdf")

    try:
        if file_type == "pdf":
            with open(original_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

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

        return text.strip() or "无法解析文件内容"
    except Exception as e:
        return f"文件解析失败：{str(e)}"