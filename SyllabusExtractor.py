import PyPDF2

def extract_text_from_pdf(pdf_path):
    wt = open("data.txt", 'w')
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'

    end_idx = 0
    start_idx = 0
    try:
        start_idx = text.lower().index("syllabus")
        end_idx = text.lower().index("textbook")
    except ValueError:
        try:
            end_idx = text.lower().index("text book")
        except:
            end_idx = len(text)

    text = text[start_idx:end_idx]
    wt.write(text)
    wt.close()
    return text

pdf_path = '/home/dheeraj/Downloads/CAP6206 HANDOUTS-Student.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
# print(pdf_text)  # Print the first 500 characters
