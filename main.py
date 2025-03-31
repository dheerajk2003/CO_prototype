from GetTest import GetTest
from SyllabusExtractor import extract_text_from_pdf

pdf_path = "/home/dheeraj/Downloads/CAP6206 HANDOUTS-Student.pdf"
syllabus = extract_text_from_pdf(pdf_path, "syllabus", "textbook", "text book")
type_details = extract_text_from_pdf(pdf_path, "course outcome", "program specific outcome")
type_info = ["understanding", "apply", "analyze"]
type_num = 0

content = {
    "contents": {
        "parts" : [
            {"text" : "Generate a test According to given syllabus and type/section of test (section a = understanding, section b = apply, section c = analyze)"},
            {"text": syllabus + type_details },
            {"text": "the type/section of text is " + type_info[type_num] + "give test of only that section" }
        ]
    }
}



test = GetTest(content)
wtr = open("data.txt", 'w')
wtr.write(test)