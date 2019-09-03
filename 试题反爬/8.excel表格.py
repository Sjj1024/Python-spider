import openpyxl

# 创建工作簿
f = openpyxl.Workbook()

# 创建工作表
sheet1 = f.create_sheet('测试')

# 设置单元格里面的值
sheet1.append({"A": "姓名", "B": "年龄"})
sheet1.append({"A": "老王", "B": "16"})

# 保存单元格
f.save("test.xlsx")
