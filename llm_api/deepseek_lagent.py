from llm_api.DeepseekLM import DeepseekLM

from datetime import datetime

from lagent.agents.internlm2_agent import (
    INTERPRETER_CN, META_CN, PLUGIN_CN, Internlm2Agent, 
    Internlm2Protocol)
from lagent.actions import ActionExecutor, BingBrowser
from lagent.llms import INTERNLM2_META

from lagent.schema import AgentStatusCode
import time

import asyncio
"""
# 初始化 DeepseekLM 实例
deepseek_llm = DeepseekLM(
    api_key="sk-cdd4c6ddedbb45e8b9bb8a6fc36a0145", 
    base_url="https://api.deepseek.com/v1"
)

# 初始化 Internlm2Agent 实例
agent = Internlm2Agent(
    llm=deepseek_llm,
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
    current_length = 0
    last_status = None
    
    for agent_return in agent.stream_chat(prompt):
        status = agent_return.state
        
        if status not in [
                AgentStatusCode.STREAM_ING, AgentStatusCode.CODING,
                AgentStatusCode.PLUGIN_START
        ]:
            continue
        
        if status != last_status:
            current_length = 0
            print('')

        if isinstance(agent_return.response, dict):
            action = f"\n\n {agent_return.response['name']}: \n\n"
            action_input = agent_return.response['parameters']
            if agent_return.response['name'] == 'IPythonInterpreter':
                action_input = action_input['command']
            response = action + action_input
        else:
            response = agent_return.response
        
        last_status = status
    
    return response

"""
# 初始化 DeepseekLM 实例
deepseek_llm = DeepseekLM(
    api_url="https://api.deepseek.com/v1",
    api_token="sk-cdd4c6ddedbb45e8b9bb8a6fc36a0145",
    model_name="deepseek-chat",
    meta_template=INTERNLM2_META,
    stop_words=['<|im_end|>']
)

plugin_executor = ActionExecutor(BingBrowser(searcher_type='DuckDuckGoSearch', topk=3))

# 初始化 Internlm2Agent 实例
agent = Internlm2Agent(
    llm=deepseek_llm,
    plugin_executor=ActionExecutor(
        BingBrowser(searcher_type='DuckDuckGoSearch', topk=6)
    ),
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
"""
# 获取响应的函数
def get_response(prompt):
    prompt = dict(role='user', content=prompt)
    last_status = None

    for agent_return in agent.stream_chat(prompt):
        status = agent_return.get('state', None)

        if status and status != last_status:
            print('')

        response = agent_return.get('response', '')

        # 实时输出流式响应
        print(response, end='', flush=True)
        last_status = status

    return response

# 使用流式输出
result = get_response("你好")
print("\n最终输出:", result)
"""
# 获取非流式响应的函数
def get_response(prompt):
    # 将用户输入的 prompt 添加到 history 中
    #history = []
    #history.append(dict(role='user', content=prompt))
    prompt = dict(role='user', content=prompt)
    # 初始化变量
    current_length = 0
    last_status = None
    print("6666666666",prompt)
    
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
        #print(agent_return.response)
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


