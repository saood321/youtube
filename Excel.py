import xlwings
wb = xlwings.Book("random1.xls")
Sheet1 = wb.sheets[1]
#Then update as you want it
Sheet1.range(2, 4).value = 4 #This will change the cell(2,4) to 4
wb.save()
wb.close()