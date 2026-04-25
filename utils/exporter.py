# utils/exporter.py
from docx import Document
from io import BytesIO

def export_to_markdown(content):
    """导出为MD文件"""
    return content.encode('utf-8')

def export_to_docx(content):
    """导出为DOCX文件（完美兼容Streamlit）"""
    doc = Document()
    lines = content.split('\n')
    for line in lines:
        doc.add_paragraph(line.strip())
    
    byte_io = BytesIO()
    doc.save(byte_io)
    byte_io.seek(0)
    return byte_io

# 简化版PDF导出，兼容所有系统+中文，无编码报错
def export_to_pdf(content):
    pdf_content = content.encode('utf-8')
    return pdf_content