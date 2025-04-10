from ai.handleAI import handleAI
from SyllabusExtractor import extract_text_from_pdf
from MTE_data_extractor import extract_data
from MTE_data_extractor import get_worst

#modificatoin
from ai.GetTest import Gemini
from Clustering import Clustering
c = Clustering()
gemini = Gemini()

# aiHandler = handleAI()


# data form excel
students = extract_data("data/test.xlsm", "MTE", [6, 176], [4, 6, 8, 10, 12, 14, 16, 18])
#data form exam paper for co mapping
paper = extract_text_from_pdf("data/CA2106_OS__MTE-24.pdf")

co_map = gemini.getMapping(paper)
print(co_map)
performance = get_worst(students, co_map)

# data from handout
pdf_path = "data/CAP6205 Course Handout OS.pdf"
syllabus = extract_text_from_pdf(pdf_path, "syllabus", "textbook", "text book")
type_details = extract_text_from_pdf(pdf_path, "course outcome", "program specific outcome")
type_info = ["understanding", "apply", "analyze"]

# clustering
print(c.clustering(performance))

roll_no = int(input("Enter the roll no of student that you want to get test for: ")) - 1

content = "Generate a test According to given syllabus and type/section of test " + syllabus + type_details
content += "(percentage of co1 is "+str(performance[roll_no][0])+"percentage of co2 is"+str(performance[roll_no][1])+"percentage of co3 is"+str(performance[roll_no][2])+")"
content += "add questions of only that co in which the student has secured less than 65 percentage"
content += "there should be total 8 question divided between diffent sections according to co percentage, there should be more questions of co in which student has performed worst."

if(performance[roll_no][0] > 65 and performance[roll_no][1] > 65 and performance[roll_no][2] > 65):
    print("no need to generate test for this student, this student has good grades")
    
else:
    print("co1 = "+str(performance[roll_no][0]) + " co2 = " + str(performance[roll_no][1]) + " co3 = " + str(performance[roll_no][2]))
    # aiHandler.GenerateResponses(content)
    print(gemini.GetTest(content))
