from ai.GetTest import Gemini
from SyllabusExtractor import extract_text_from_pdf
from collections import defaultdict

class Clustering:

    def clustering(self, performance):
        student_wise_CO_cluster = {}
        for i, j in enumerate(performance):
            temp2 = []
            for a, b in enumerate(j):
                if b < 65:
                    temp2.append(1)
                else:
                    temp2.append(0)
            str1 = int(("".join(str(x) for x in temp2)), 2)

            student_wise_CO_cluster[i] = str1

        cluster = defaultdict(list)

        for i in student_wise_CO_cluster:
            match student_wise_CO_cluster[i]:
                case 0:
                    cluster[0].append(i)
                case 1:
                    cluster[1].append(i)
                case 2:
                    cluster[2].append(i)
                case 3:
                    cluster[3].append(i)
                case 4:
                    cluster[4].append(i)
                case 5:
                    cluster[5].append(i)
                case 6:
                    cluster[6].append(i)
                case 7:
                    cluster[7].append(i)

        CO_cluster = {k: cluster[k] for k in sorted(cluster)}


        for i in CO_cluster:
            print(f"{i} = {CO_cluster[i]}")

        return CO_cluster


