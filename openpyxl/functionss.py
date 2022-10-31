from openpyxl import Workbook
import datetime

wb = Workbook()

ws = wb.active

ws.append([5, 6, 7])

#ws['B6'] = 47
#ws['B5'] = datetime.datetime.now()

wb.save("abc_dados.xlsx")

print(ws.max_row)
print(ws.max_column)