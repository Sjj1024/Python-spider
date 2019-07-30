import js2py

# 实例化一个js的环境对象
context_js_obj = js2py.EvalJs()

js_str = """
    function Add(a, b){
        return a+b
    }
"""

# 传入js字符传，并执行js
context_js_obj.execute(js_str)

# 调用js函数
res = context_js_obj.Add(3,4)

print(res)