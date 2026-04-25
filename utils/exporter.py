from docx import Document
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 内置中文字体，零配置无乱码
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
FONT_NAME = 'STSong-Light'

def export_to_markdown(content):
    return content.encode('utf-8')

def export_to_docx(content):
    doc = Document()
    for line in content.split("\n"):
        doc.add_paragraph(line.strip())
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def export_to_pdf(content):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont(FONT_NAME, 12)
    y = 800
    line_height = 18
    for line in content.split("\n"):
        if y < 40:
            c.showPage()
            c.setFont(FONT_NAME, 12)
            y = 800
        c.drawString(40, y, line.strip())
        y -= line_height
    c.save()
    buffer.seek(0)
    return buffer