from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    return "\n".join((page.extract_text() or "") for page in reader.pages)

def split_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
