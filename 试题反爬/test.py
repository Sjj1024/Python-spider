filter_name = [{"name":"xiao", "age":"19"},{"name":"xiao", "age":"13"},{"name":"xiao", "age":"21"},]
filter_name.sort(key=lambda x:int(x["age"]))
print(filter_name)