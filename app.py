import kits

submit_file_path = './txt/ask-question.txt'
answer_file_path = './txt/receive-result.txt'
last_submit_path = './txt/last-ask-question.txt'
separate = '\n---------------------------------'
content_list = []


def getPuzzleStr(path):
    # 从文件中读取问题内容
    content_list = kits.ReadFileContent.open_file(path)
    print(str(content_list))

    # 转为string
    puzzle_str = "".join(content_list)
    return puzzle_str


def verifyRepeat(puzzle_str):
    repeatFlag = True
    lastQuestion = getPuzzleStr(last_submit_path)
    print("lastQuestion: "+lastQuestion)

    # 验证2个字符串是否一致
    if lastQuestion.strip() == puzzle_str.strip():
        print("这个问题与上一个一致,为了避免浪费资源,请输入另外的问题")
        repeatFlag = False

    print("repeatFlag: "+str(repeatFlag))
    return repeatFlag


def checkStrEmpty(puzzle_str):
    lengthFlag = True

    strLen = len(puzzle_str.strip())
    verifySpace = puzzle_str.isspace()
    print("strLen: " + str(strLen)+" , verifySpace: " + str(verifySpace))

    if strLen < 3 or verifySpace == True:
        print("问题内容不足,无法提交,请重新输入问题")
        lengthFlag = False

    return lengthFlag


def detectOverLimitLen(puzzle_str):
    sizeFlag = True

    stringLength = len(puzzle_str.strip())
    print("stringLength: " + str(stringLength))

    if stringLength > 1024:
        print('问题的长度不可超过1024个字符,请精简后再提交')
        sizeFlag = False

    return sizeFlag


def writeResp2File(puzzle_str):
    # 向openai提问,并获取回答
    answerText = kits.Robot.inquiry(puzzle_str)

    # 将答案追加写入另一个文件
    kits.Write2File.write_by_pattern(
        answer_file_path, answerText+separate, 'a')

    # 将问答完毕中的提问覆盖写入备份记录
    kits.Write2File.write_by_pattern(last_submit_path, puzzle_str, 'w')


def index():
    while True:
        x = input('请输入y或n,决定是否进行提问: ')

        if x == 'y':
            puzzle = getPuzzleStr(submit_file_path)
            empty_flag = checkStrEmpty(puzzle)
            repeat_flag = verifyRepeat(puzzle)
            size_flag = detectOverLimitLen(puzzle)

            if empty_flag == False:
                continue
            elif repeat_flag == False:
                continue
            elif size_flag == False:
                continue
            else:
                writeResp2File(puzzle.strip())
                continue

        elif x == 'n':
            print('程序终止运行')
            break

        else:
            print('请输入正确的选项(y/n)')
            continue


index()
