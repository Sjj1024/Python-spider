five_list = []
onefive_list = []
twofive_list = []
thrfive_list = []
forfive_list = []
item = {}
item['price'] = '4000.00'
if float(item['price']) <= 500:
    five_list.append(item)
elif 500 < float(item['price']) <= 1500:
    onefive_list.append(item)
elif 1500 < float(item['price']) <= 2500:
    twofive_list.append(item)
elif 2500 < float(item['price']) <= 3500:
    thrfive_list.append(item)
elif 3500 < float(item['price']):
    forfive_list.append(item)

print(five_list,'11111')
print(onefive_list,'2222')
print(twofive_list,'3333')
print(thrfive_list,'4444')
print(forfive_list,'5555')
