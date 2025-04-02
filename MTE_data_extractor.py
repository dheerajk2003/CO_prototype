from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string

# data_only=true returns calculated value if formula is applied on that particular cell
workbook = load_workbook("sample.xlsm", data_only=True)
worksheet = workbook["MTE"]
students = [[]]
rollNo_col = column_index_from_string("B")
N_value_col = [4, 6, 8, 10, 12, 14, 16, 18]

for row_index in range(6, 7):  # worksheet.max_row + 1):
    i = 0
    rollNo = worksheet.cell(row=row_index, column=rollNo_col).value
    N_value = [worksheet.cell(row=row_index, column=col).value for col in N_value_col]

    students[i].append(N_value)
    print(students)
    i += 1
    # var = [rollNo, N_value]
    # print(f"N value of Roll no  {var[0]}  = {var[1]}")
