import re

with open("数据库练习1.sql", "r", encoding="utf-8") as file:
    count = file.read()

# print(count)
res = re.findall(r"-- \d{1,2}、.+?\n", count)
# print(res)
with open("quest.sql", "w", encoding="utf-8") as q:
    for question in res:
        q.write(question)  # 默认写的时候用的也是utf8格式
        q.write("\n\n")
