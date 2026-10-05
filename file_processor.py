import pymupdf
from docx import Document

def __extract_pdf_text(file):
    text = ""
    
    pfd_content = file.getvalue()
    
    pfd_documents = pymupdf.open(
        stream=pfd_content,
        filename="pdf"
    )
    
    for page in pfd_documents:
        text += page.get_text()
        
    pfd_documents.close()
    
    return text

def __extract_doc_text(file):
    
    text=""
    
    document = Document(file)
    
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
        
    return text

def extract_text(file):
    file_name = file.name.lower()
    
    if file_name.endswith(".pdf"):
        return __extract_pdf_text(file)
    elif file_name.endswith(".docx"):
        return __extract_doc_text(file)
    else:
        raise ValueError("Unsupport file format")