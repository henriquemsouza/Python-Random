import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_sheet_by_name('Age')

if sheet.cell(row = 1, column=7).value == None:
    print("Blank")
else:
    print("No blank")
