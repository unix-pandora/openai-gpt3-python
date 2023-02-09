# -*- coding: utf-8 -*-

# 定义一个函数，用于读取指定目录下的文件
def open_file(filename):
    file = open(filename, 'r', encoding='utf-8')  # 打开文件
    cont = file.readlines()  # 读取所有行
    print(type(cont))

    contStr = "".join(cont)
    print(type(contStr))

    # 除去开头和末尾的空格,以及回车行,空白行
    purityContent = "".join(
        [line.strip() for line in contStr.strip().split("\n") if line.strip()])

    print('open_file()-purityContent: '+purityContent)

    file.close()  # 关闭文件
    return purityContent  # 返回读取到的内容
