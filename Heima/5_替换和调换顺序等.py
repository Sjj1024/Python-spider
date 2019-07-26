import re

if __name__ == '__main__':
    # sub替换
    str1 = "wo shi ni da ye"
    sub_re = re.compile(r" ")
    result = sub_re.sub("", str1)

    # 调换顺序


    # split 分割


    # 汉字--unicode字符[u4e00-u9fa5]，python3中\w可以匹配到中文
    print(result)