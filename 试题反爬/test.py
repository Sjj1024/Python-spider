from openpyxl import Workbook,load_workbook

wb = load_workbook("sample.xlsx")

ws = wb.active

for i in ws.rows:
  for j in i:
    print(j.value)



