import openpyxl

book = openpyxl.load_workbook('example.xlsx')

sheet = book.active

cells = sheet['A1': 'B6']

for c1, c2 in cells:
    print("{0:6} {1:6}".format(c1.value, c2.value))
