from ai.handleAI import handleAI
from SyllabusExtractor import extract_text_from_pdf
from MTE_data_extractor import extract_data
from MTE_data_extractor import get_worst
from MTE_data_extractor import get_CO_Cluster
from MTE_data_extractor import CO_paper_read


aiHandler = handleAI()

students = extract_data(
    "data/test.xlsm", "MTE", [6, 176], [4, 6, 8, 10, 12, 14, 16, 18]
)

mapping = CO_paper_read("data/CA2106_OS__MTE-24.pdf")
performance = get_worst(students, co_map)

performance = get_worst(students)
CO_Cluster = get_CO_Cluster(performance)
pdf_path = "data/CAP6205 Course Handout OS.pdf"
syllabus = extract_text_from_pdf(pdf_path, "syllabus", "textbook", "text book")
type_details = extract_text_from_pdf(
    pdf_path, "course outcome", "program specific outcome"
)
type_info = ["understanding", "apply", "analyze"]


roll_no = int(input("Enter the roll no of student that you want to get test for: ")) - 1

content = (
    "Generate a test According to given syllabus and type/section of test "
    + syllabus
    + type_details
)
content += (
    "(percentage of co1 is "
    + str(performance[roll_no][0])
    + "percentage of co2 is"
    + str(performance[roll_no][1])
    + "percentage of co3 is"
    + str(performance[roll_no][2])
    + ")"
)
content += "add questions of only that co in which the student has secured less than 65 percentage"
content += "there should be total 8 question divided between diffent sections according to co percentage, there should be more questions of co in which student has performed worst."
content += "The Questions must either be MCQ or Writting Questions with Keywords."
content += "The Response must be in JSON format where MCQ and Writting Questions will be two seperate array as root properties."
content += "Every MCQ object must include the question, 4 options and correct answer as properties. "
content += "Every Writting Question object must include the question and the list of keywords that will need to be included in the correct answers."

if (
    performance[roll_no][0] > 65
    and performance[roll_no][1] > 65
    and performance[roll_no][2] > 65
):
    print("no need to generate test for this student, this student has good grades")

else:
    print(
        "co1 = "
        + str(performance[roll_no][0])
        + " co2 = "
        + str(performance[roll_no][1])
        + " co3 = "
        + str(performance[roll_no][2])
    )
    aiHandler.GenerateResponses(content)
