这是一个用于美化日志的工具包，可以让您拥有一个易于阅读的日志。日志格式为“[日期 时间][日志类型]日志内容”。

如果您的设备已安装pip,您可以打开命令行，并使用以下代码进行安装：
```
pip install colorama
pip install --trusted-host 114.115.172.126 -i http://114.115.172.126:3141/simple/ beautylog
```
以下是一些演示代码：
```python
from beautylog import *

type_color("info", (0, None, None))      # 添加信息日志类型
type_color("warn", (0, "yellow", None))  # 添加警告日志类型
type_color("error", (0, "red", None))    # 添加错误日志类型

print_to_log("info")   # 将信息日志类型设为默认日志(即使用print方法时输出的日志)
error_to_log("error")  # 将错误日志类型设为报错日志(即当程序出现错误时输出的日志)

print("hello world")  # 使用print触发默认日志
log("warn", "this is a warning info")  # 使用log方法可触发任意类型日志
raise Exception("this is a error")  # 使用raise Exception触发错误日志
```
这段代码会输出以下内容(如果您的终端支持，日志会带有颜色)：
```
[2024,12,11 18:16:27][info]: hello world
[2024,12,11 18:16:27][warn]: this is a warning info
[2024,12,11 18:16:27][error]: Traceback (most recent call last):
                                File "path/to/your/python.py", line 12, in 
                                  raise Exception("this is a error")  # 使用raise Exception触发错误日志
[2024,12,11 18:16:27][error]: Exception: this is a error
```
