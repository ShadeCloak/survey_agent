# python3
# Please install OpenAI SDK first：`pip3 install openai`
from openai import OpenAI

"""
def deepseek_response(prompt):
    client = OpenAI(api_key="sk-cdd4c6ddedbb45e8b9bb8a6fc36a0145", 
    base_url="https://api.deepseek.com/chat/completions")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=True
    )

    full_response = ""  # 用于存储完整的响应

    # 逐步读取流中的每个chunk
    for chunk in response:
        content = chunk.choices[0].delta.content  # 直接访问 content 属性
        if content:  # 如果内容不为空，则追加到 full_response
            full_response += content
            #print(content, end="")  # 实时打印每个片段

    #print("\n完整的响应:", full_response)  # 最后输出完整的响应
    return full_response
"""

def deepseek_response(prompt):
    client = OpenAI(api_key="sk-cdd4c6ddedbb45e8b9bb8a6fc36a0145", 
    base_url="https://api.deepseek.com/v1")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    return response.choices[0].message.content
