import PyPDF2

def extract_text_from_pdf(pdf_path, start, end, s_end=""):
    wt = open("data.txt", 'w')
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
    wt.write(text)
    wt.close()
    return text

pdf_path = '/home/dheeraj/Downloads/CAP6206 HANDOUTS-Student.pdf'
pdf_text = extract_text_from_pdf(pdf_path, "syllabus", "textbook", "text book")
print(pdf_text)
pdf_text = extract_text_from_pdf(pdf_path, "course outcome", "program specific outcome")
print(pdf_text)
