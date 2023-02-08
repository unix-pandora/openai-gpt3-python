# -*- coding: utf-8 -*-

# 定义一个函数，用于读取指定目录下的文件
def open_file(filename):
    file = open(filename, 'r', encoding='utf-8')  # 打开文件
    contents = file.readlines()  # 读取所有行
    file.close()  # 关闭文件
    return contents  # 返回读取到的内容
