import pdfplumber
from docx import Document

def extract_text_from_file(content, filename):
    if filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(content)
        with pdfplumber.open("temp.pdf") as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif filename.endswith(".docx"):
        with open("temp.docx", "wb") as f:
            f.write(content)
        doc = Document("temp.docx")
        return "\n".join(p.text for p in doc.paragraphs)
    elif filename.endswith(".txt"):
        return content.decode("utf-8")
    else:
        return "Unsupported file format."
