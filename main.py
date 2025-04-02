from GetTest import GetTest
from SyllabusExtractor import extract_text_from_pdf
from MTE_data_extractor import extract_data
from MTE_data_extractor import get_worst


students = extract_data("test.xlsm", "MTE", [6, 176], [4, 6, 8, 10, 12, 14, 16, 18])
worst = get_worst(students)
pdf_path = "/home/dheeraj/Downloads/CAP6205 Course Handout OS.pdf"
syllabus = extract_text_from_pdf(pdf_path, "syllabus", "textbook", "text book")
type_details = extract_text_from_pdf(pdf_path, "course outcome", "program specific outcome")
type_info = ["understanding", "apply", "analyze"]
# type_num = 2

roll_no = int(input("Enter the roll no of student that you want to get test for: ")) - 1

content = {
    "contents": {
        "parts" : [
            {"text" : "Generate a test According to given syllabus and type/section of test (section a = understanding, section b = apply, section c = analyze)"},
            {"text": syllabus + type_details },
            {"text": "the type/section of text is " + type_info[worst[roll_no][0]] + "give test of only that section," },
            {"text": "the student secured " + str(worst[roll_no][1]) + " percentage in that particular section so generate test accodingly"}
        ]
    }
}



test = GetTest(content)
wtr = open("data.md", 'w')
wtr.write(test)