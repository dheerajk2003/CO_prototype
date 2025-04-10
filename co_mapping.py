from ai.GetTest import Gemini
from SyllabusExtractor import extract_text_from_pdf

class CO_mapping:
    def __init__(self):
        self.mapping = []
        self.gemini = Gemini()

    def getMapping(self, examPaper):

        context = "From the given test "+examPaper+" extract the CO number from every question"
        context += "And return only the co numbers without (CO) as a string "
        context += "eg:- 1 1 1 2 2 1 2 3 "

        cos = self.gemini.GetTest(context)
        map = cos.strip().split(" ")
        mapping = [int(x) for x in map]
        return mapping


test = extract_text_from_pdf("data/CA2106_OS__MTE-24.pdf")
com = CO_mapping()
cos = com.getMapping(test)
print(cos)
