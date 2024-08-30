
from lagent.llms.base_llm import BaseModel
from lagent.schema import AgentStatusCode
from lagent.schema import ModelStatusCode
import requests
import json
from typing import List, Dict, Optional
from openai import OpenAI

class DeepseekLM(BaseModel):
    def __init__(self, api_url: str, api_token: str, model_name: str, **kwargs):
        super().__init__(path=model_name, **kwargs)
        self.api_url = api_url
        self.api_token = api_token
        self.model_name = model_name
        self.stop_words = kwargs.get('stop_words', [''])

    def generate(self, inputs: List[str], session_id=0, **kwargs) -> List[str]:
        if isinstance(inputs, str):
            inputs = [inputs]

        messages = [{'role': 'user', 'content': input} for input in inputs]

        payload = {
            'model': self.model_name,
            'messages': messages,
            'session_id': session_id,
            **kwargs
        }

        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }

        response = requests.post(f"{self.api_url}/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        
        data = response.json()

        if 'choices' not in data:
            raise KeyError(f"'choices' key not found in the response: {data}")

        return [item['message']['content'] for item in data['choices']]

    def stream_chat(self,
                    inputs: List[str],
                    session_id=0,
                    sequence_start: bool = True,
                    sequence_end: bool = True,
                    stream: bool = True,
                    ignore_eos: bool = False,
                    skip_special_tokens: Optional[bool] = False,
                    timeout: int = 30,
                    **kwargs):
        """
        开始一个对话回合的新轮次。以流式模式返回聊天完成结果。

        Args:
            session_id (int): 会话的唯一标识符
            inputs (List[str]): 用户在本轮对话中的输入
            sequence_start (bool): 会话开始标志
            sequence_end (bool): 会话结束标志
            ignore_eos (bool): 忽略结束符号的指示
            skip_special_tokens (bool): 是否在解码过程中移除特殊标记，默认为 False
            timeout (int): 等待响应的最大时间

        Returns:
            tuple(Status, str, int): 状态、文本/聊天完成结果、生成的标记数量
        """
        prompt = self.template_parser(inputs)
        if isinstance(prompt, str):
            prompt = [prompt]
            batched = False
        else:
            batched = True
        print("333333",prompt)
        messages = [{'role': 'user', 'content': pro} for pro in prompt]
        print("2222222",messages)
        client = OpenAI(api_key="sk-cdd4c6ddedbb45e8b9bb8a6fc36a0145", 
        base_url="https://api.deepseek.com/v1")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=True
        )
        #response.raise_for_status()
        
        # 初始化响应字符串
        resp = ''
        # 初始化完成标志
        finished = False
        # 获取停止词
        stop_words = self.stop_words
        

        # 解析流式响应
        for chunk in response:
            # 直接访问chunk对象的delta属性
            if chunk.choices and hasattr(chunk.choices[0], 'delta'):
                content = chunk.choices[0].delta.content  # 直接访问 content 属性
                resp += content if content else ""
                if not resp:
                    continue
                for sw in stop_words:
                    if sw in resp:
                        print("111")
                        resp = self.filter_suffix(resp, stop_words)
                        finished = True
                        break
                yield ModelStatusCode.STREAM_ING, resp, None
                #print(finished)
                if finished:
                    break
        print("33333333",resp)
        #resp = """
        #好的，我需要调用工具获取天气信息，稍等一下<|action_start|><|plugin|>\n{"name": "BingBrowser.open_url", "parameters": {"url": "https://www.bing.com/weather/location/new york, ny"}}
        #"""
        yield ModelStatusCode.END, resp, None

    @staticmethod
    def filter_suffix(text: str, stop_words: List[str]) -> str:
        for sw in stop_words:
            if text.endswith(sw):
                return text[: -len(sw)]
        return text
