from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string

# data_only=true returns calculated value if formula is applied on that particular cell

def extract_data(file_path, worksheet_name, rowList, colList, ):
    workbook = load_workbook(file_path, data_only=True)
    worksheet = workbook[worksheet_name]
    students = []
    rollNo_col = column_index_from_string("B")
    N_value_col = colList

    for row_index in range(rowList[0], rowList[1]):
        # extracts individual cell values
        rollNo = worksheet.cell(row=row_index, column=rollNo_col).value
        # for loop helps getting all the values mentioned in the list above
        N_value = [worksheet.cell(row=row_index, column=col).value for col in N_value_col]

        students.append(N_value)  # to insert data in a 2d list
        # print(students)

    return students


def get_worst(students):
    performance = []
    for i in range(len(students)):
        performance.append([0, 0, 0])
        performance[i][0] = round(sum(students[i][0:3]) / 30 * 100, 2)
        performance[i][1] = round(sum(students[i][3:7]) / 40 * 100, 2)
        performance[i][2] = (students[i][7]) * 10

    return performance