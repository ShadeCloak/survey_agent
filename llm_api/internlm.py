# -*- coding: utf-8 -*-

from llm_api.CustomLM import CustomLMServer

from datetime import datetime

from lagent.agents.internlm2_agent import (
    INTERPRETER_CN, META_CN, PLUGIN_CN, Internlm2Agent, 
    Internlm2Protocol)
from lagent.actions import ActionExecutor, BingBrowser
from lagent.llms import INTERNLM2_META

from lagent.schema import AgentStatusCode
import time

import asyncio

#from action import AbstractSearch

lang = 'cn'
url = 'https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions'
model = 'internlm2.5-latest'
api = 'eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDIxMjE0NyIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyMzk2MjU0MywiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTc3NjIwNzU2NDAiLCJ1dWlkIjoiNDdiYjUwMWItNDdiZi00ZWI4LTljZGQtYWI1MzBjNjY5YTIxIiwiZW1haWwiOiIiLCJleHAiOjE3Mzk1MTQ1NDN9.x_tYOlgTpFe0UkkPiIbqMAADq2ME_qGGPy8dKTiCkvSZkly_RVIQYlTkmnGFK0W3fQQwREO7m157kq4VLLxvtg'


llm = CustomLMServer(
    api_url=url, 
    model_name=model,
    api_token=api,
    meta_template=INTERNLM2_META,
    top_p=1,
    top_k=50,
    temperature=1,
    max_new_tokens=8192,
    repetition_penalty=1.02,
    stop_words=['<|im_end|>']
)

plugin_executor = ActionExecutor(BingBrowser(searcher_type='DuckDuckGoSearch', topk=3))

agent = Internlm2Agent(
    llm=llm,
    plugin_executor=None,
    protocol=Internlm2Protocol(
        meta_prompt=META_CN,
        plugin_prompt=PLUGIN_CN, 
        tool=dict( 
            begin='{start_token}{name}\n', 
            start_token='<|action_start|>', 
            name_map=dict(plugin='<|plugin|>', interpreter='<|interpreter|>'),
            belong='assistant',
            end='<|action_end|>\n',
        ),
    ),
)

def get_response(prompt):
    # 将用户输入的 prompt 添加到 history 中
    #history = []
    #history.append(dict(role='user', content=prompt))
    prompt = dict(role='user', content=prompt)
    # 初始化变量
    current_length = 0
    last_status = None
    
    # 遍历 agent 的 stream_chat 方法返回的结果
    for agent_return in agent.stream_chat(prompt):
        status = agent_return.state
        
        # 如果状态不是 STREAM_ING, CODING 或 PLUGIN_START,则跳过当前循环
        if status not in [
                AgentStatusCode.STREAM_ING, AgentStatusCode.CODING,
                AgentStatusCode.PLUGIN_START
        ]:
            continue
        
        # 如果状态改变,重置 current_length 并换行
        if status != last_status:
            current_length = 0
            print('')

        # 处理返回的响应
        if isinstance(agent_return.response, dict):
            # 如果响应是字典,提取 action 和 action_input
            action = f"\n\n {agent_return.response['name']}: \n\n"
            action_input = agent_return.response['parameters']
            # 如果 action 是 IPythonInterpreter,提取其中的 command
            if agent_return.response['name'] == 'IPythonInterpreter':
                action_input = action_input['command']
            response = action + action_input
        else:
            # 如果响应是字符串,直接添加到 response 中
            response = agent_return.response
        
        # 更新 last_status 为当前状态
        last_status = status
    #history = []
    # 返回最终的 response
    loop = asyncio.get_event_loop()
    loop.close()
    return response




