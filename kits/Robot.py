import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def inquiry(puzzle):
    print('inquiries: '+puzzle)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=puzzle,

        # 控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
        temperature=0.9,

        max_tokens=4000,
        frequency_penalty=0.0,
        presence_penalty=0.0,

        # 控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
        top_p=1.0,

        # 最大长度为 4 的字符串列表，一旦生成的 tokens 包含其中的内容，将停止生成并返回结果
        stop=['#'],
    )

    print(type(response))
    print(response)

    respondMsg = response["choices"][0]["text"]
    print(respondMsg)

    return respondMsg
