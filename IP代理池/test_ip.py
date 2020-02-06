import re

ip_str = "<td>119.2.54.204:44860</td>"
res = re.findall(r"\d*\.\d*\.\d*\.\d*:\d*", ip_str)
print(res)