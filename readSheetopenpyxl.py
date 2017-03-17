from openpyxl import load_workbook

wb = load_workbook(filename='example.xlsx', read_only=True)
ws = wb['Age']#name  of  the sheet

for row in ws.rows:
    for cell in row:
        print(cell.value)
