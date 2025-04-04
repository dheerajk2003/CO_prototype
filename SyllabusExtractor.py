import PyPDF2

def extract_text_from_pdf(pdf_path, start, end, s_end=""):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'

    end_idx = 0
    start_idx = 0
    try:
        start_idx = text.lower().index(start)
        end_idx = text.lower().index(end)
    except ValueError:
        try:
            end_idx = text.lower().index(s_end)
        except:
            end_idx = len(text)

    text = text[start_idx:end_idx]
    return text


