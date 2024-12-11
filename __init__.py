import sys
from threading import *
from datetime import datetime
from time import *
from colorama import init
from curses import *



init(autoreset=True)  # 让彩色字符可用
type_color_dir = {}
is_repeat_input = False

old_stdout = sys.stdout
now_stdout = sys.stdout

old_stderr = sys.stderr
now_stderr = sys.stderr


class MyStdout:
    def __init__(self, _type):
        """
        用于将输出转换为日至格式的类
        :param _type: 日至类型
        """
        self.type = _type
        self.long_log_txt = ""

    def write(self, string):
        """
        输出时调用的函数
        :param string: 输出的函数
        :return: None
        """
        if string == "\n":
            log_list = self.long_log_txt.split("\n")
            log_text = log_list[0]
            log_list = [" "*(25+len(self.type))+i for i in log_list]
            log_list.pop(0)
            for i in log_list:
                log_text += "\n"+i
            log(self.type, log_text)
            self.long_log_txt = ""
        else:
            self.long_log_txt += string

    def flush(self):
        del self


def type_color(_type, font):
    """
    分类颜色
    :param _type: 输出类型
    :param font:  字体形态(style, fg, bg)
    :return: None
    """
    type_color_dir[_type] = font


def log(_type, info):
    """
    以对应的类型输出日至
    :param _type: 日至类型
    :param info:  日至内容
    :return: None
    """
    sys.stdout = old_stdout
    print(create_log(_type, info))
    sys.stdout = now_stdout


def create_log(_type, info):
    """
    创建日至格式的字符
    :param _type: 日至类型
    :param info:  日至内容
    :return: 日至格式的字符
    """
    if _type not in type_color_dir:
        raise Exception(f"do not have type: {_type}")
    if _type in type_color_dir:
        font = type_color_dir[_type]
    else:
        font = (0, None, None)
    return create_colo_text('[', datetime.now().strftime("%Y,%m,%d %H:%M:%S"), ']', '[', font, _type, ']: ', info,
                            sep='')


def print_to_log(_type):
    """
    将标准输出更改为日至格式
    :param _type: 日至类型
    :return: None
    """
    global now_stdout
    if _type not in type_color_dir:
        raise Exception(f"do not have type: {_type}")
    now_stdout = MyStdout(_type)
    sys.stdout = now_stdout


def error_to_log(_type):
    """
    将错误输出更改为日至格式
    :param _type: 日至类型
    :return: None
    """
    global now_stderr
    if _type not in type_color_dir:
        raise Exception(f"do not have type: {_type}")
    now_stderr = MyStdout(_type)
    sys.stderr = now_stderr


def colo_print(*args, sep=' ', end='\n'):
    """
    彩色输出
    :param args: 字体形态/输出内容((style, fg, bg), info)
    :param sep:  分隔
    :param end:  结尾
    :return: None
    """
    print_info = create_colo_text(sep, *args)
    print(print_info, end=end)


def unlog_print(*args, sep=' ', end='\n'):
    """
    非日至输出
    :param args: 输出内容
    :param sep:  分隔
    :param end:  结尾
    :return: None
    """
    sys.stdout = old_stdout
    print(*args, sep=sep, end=end)
    sys.stdout = now_stdout


def create_colo_text(*args, sep=' '):
    """
    创建带颜色的字符
    :param args: 字体形态/输出内容((style, fg, bg), info)
    :param sep:  分隔
    :return: 带颜色的字符
    """
    fg_dic = {'None': 0,
              'black': 30,
              'red': 31,
              'green': 32,
              'yellow': 33,
              'blue': 34,
              'pink': 35,
              'cyan': 36,
              'white': 37}
    bg_dic = {i: fg_dic[i] + 10 for i in fg_dic}
    text = ""
    for i in args:
        if type(i) == tuple:
            text += f"\033[{i[0]};{fg_dic[str(i[1])]};{bg_dic[str(i[2])]}m"
        else:
            text += f"{i}\033[0m{sep}"
    text += f"\033[0m"
    return text


if __name__ == '__main__':
    ...
