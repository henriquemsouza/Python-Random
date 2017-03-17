from openpyxl import load_workbook

wb212 = load_workbook('example.xlsx')

print( wb212.get_sheet_names())

