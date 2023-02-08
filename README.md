# openai-gpt3-python

<hr>
<hr>

# Introduction

Call the GPT-3 official model interface based on python to realize the effect of question and answer with AI

<hr>

# Dependency

```
#Temporarily install the specified dependency from the image source
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# or
pip install -r requirements.txt

```

<hr>

# Key

- First copy `env. example` to `. env` in the same level directory

- Next, paste the key manually generated by your OpenAI account into `. env` and assign it to `OPENAI_API_KEY`

<hr>

# Carrying interactive records

Create the 'txt' folder under the project root directory, and create `ask-question.txt`, `receive-result.txt`, and `last-ask-question.txt` under this folder respectively

```
mkdir txt;
#Enter the question here
touch txt/ask-question.txt;

#The returned answer will be written here
touch txt/receive-result.txt;

#The questions in the last round of Q&A will be temporarily stored here
touch last-ask-question.txt;
```

<hr>

# Installation dependency

```
pip install -r requirements.txt
```

<hr>

# Operation

- Step 1: When starting the project for the first time, enter the question in 'txt/ask-question. txt'

- The second step is as execute startup:

```
python3 app.py

```

<hr>

# Notice

- After the project is started and the first question and answer is completed, it will continue to confirm whether to continue to ask questions. y represents to continue, n represents to terminate the program operation, and other characters are invalid

- If you ask the same question twice in a row, you will be judged as a violation

- The question content cannot be empty and cannot exceed 1024 characters

<hr>
<hr>

# 简介

基于 python 调用 GPT-3 官方模型接口,实现与人工智能进行问答的效果

<hr>

# 依赖

```

# 临时从镜像源安装指定依赖
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 或者
pip install -r requirements.txt

```

<hr>

# 密钥

- 首先把`env.example`复制成同一级目录下的`.env`

- 接着,将你 OpenAI 账户手动生成的密钥粘贴到`.env`,赋值给`OPENAI_API_KEY`

<hr>

# 承载互动记录

在项目根目录下创建 `txt` 文件夹,又在此文件夹下分别创建 `ask-question.txt` , `receive-result.txt` , `last-ask-question.txt`

```
mkdir txt;

# 在这里输入问题
touch txt/ask-question.txt;

# 返还的答案会写入此处
touch txt/receive-result.txt;

# 上一轮问答完毕中的提问会暂存在此处
touch last-ask-question.txt;

```

<hr>

# 安装依赖

```
pip install -r requirements.txt
```

<hr>

# 操作

- 第一步,首次启动项目时,先在`txt/ask-question.txt`中输入问题

- 第二步,执行启动:

```
python3 app.py

```

<hr>

# 须知

- 项目启动,并且第一次问答完成后,会一直向你循环确认是否继续提问,y 代表继续下去,n 代表终止程序运行,其它字符无效

- 连续两次提出同样的问题,会被判定为违规

- 问题内容不能为空,不能超过 1024 个字符

<hr>