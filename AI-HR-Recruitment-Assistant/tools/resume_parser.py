import re
from pypdf import PdfReader

def extract_resume_text(file_path):
    reader = PdfReader(file_path)
    return "\n".join((page.extract_text() or "") for page in reader.pages)

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r'\+?\d[\d\s-]{8,15}', text)
    return match.group(0) if match else "Not found"

def parse_resume(file_path):
    text = extract_resume_text(file_path)
    return {"text": text, "email": extract_email(text), "phone": extract_phone(text)}
