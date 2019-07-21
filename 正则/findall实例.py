# findall实例详解
import re

html1 = """
https://apic.douyu
<img src="https://apic.douyucdn.cn/upload/avatar_v3/201903/d9fa1bce979e4e83b945a3b9c1b42491_big.jpg" 
<img src="https://apic.douyucdn.cn/upload/avatar_v3/201902/3fb06c678e9e44488d761b60974af47b_big.jpg" 
<img src="https://apic.douyucdn.cn/upload/avatar_v3/201904/3c05cb56dc864cc68dd3946aea6b4388_big.jpg"

"""

file_jpg = re.findall(r"https://.*\.jpg", html1)
print(file_jpg)