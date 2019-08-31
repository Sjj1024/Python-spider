import openpyxl

# 创建工作簿
f = openpyxl.Workbook()

# 创建工作表
sheet1 = f.create_sheet('测试')

# 设置单元格里面的值
for jkey in range(3):
    jk = 1
    for cT in range(3):
        jk = jkey + 1
        if cT == 0:
            sheet1.cell(row=jk, column=cT + 1).value = '1'
        elif cT == 1:
            sheet1.cell(row=jk, column=cT + 1).value = '2'
        else:
            sheet1.cell(row=jk, column=cT + 1).value = '3'

# 保存单元格
f.save("test.xlsx")
