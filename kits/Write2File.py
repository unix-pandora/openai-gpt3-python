def write_by_pattern(filepath, content, pattern):
    # pattern: a:追加写入, w: 覆盖写入
    with open(filepath, pattern) as f:
        f.write(content)
        print('成功写入, 模式: '+pattern)
