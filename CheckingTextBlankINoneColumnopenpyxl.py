import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_sheet_by_name('Age')#name  of the sheet
for i in range(1, 10):
    if sheet.cell(row=i, column=1).value in [None,'']:
        print("Blank")
    else:
        print("No blank")
