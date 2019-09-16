filter_name = {'name': ['song']}

if "song" in filter_name:
    filter_name["name"].append("11111")
else:
    filter_name["name"] = ["name"]

print(filter_name)
