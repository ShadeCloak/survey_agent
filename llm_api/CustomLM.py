from typing import List, Optional, Union
from lagent.llms.base_llm import BaseModel
from lagent.schema import ModelStatusCode

import requests
import json

class CustomLMServer(BaseModel):
    def __init__(self, api_url: str, api_token: str, model_name: str, **kwargs):
        super().__init__(path=model_name, **kwargs)
        self.api_url = api_url
        self.api_token = api_token
        self.model_name = model_name
        self.top_p = kwargs.get('top_p', 0.9)
        self.top_k = kwargs.get('top_k', 50)
        self.temperature = kwargs.get('temperature', 0.7)
        self.max_new_tokens = kwargs.get('max_new_tokens', 50)
        self.repetition_penalty = kwargs.get('repetition_penalty', 1.2)
        self.stop_words = kwargs.get('stop_words', [''])
        self.gen_params = {
            'top_p': self.top_p,
            'top_k': self.top_k,
            'temperature': self.temperature,
            'max_new_tokens': self.max_new_tokens,
            'repetition_penalty': self.repetition_penalty,
        }

    def generate(self, inputs, session_id=2967, sequence_start=True, sequence_end=True, ignore_eos=False, skip_special_tokens=False, timeout=30, **kwargs):
        if isinstance(inputs, str):
            inputs = [inputs]
            batched = False
        else:
            batched = True

        messages = [{'role': 'user', 'content': input} for input in inputs]

        payload = {
            'model': self.model_name,
            'messages': messages,
            'session_id': session_id,
            'sequence_start': sequence_start,
            'sequence_end': sequence_end,
            'ignore_eos': ignore_eos,
            'skip_special_tokens': skip_special_tokens,
            'timeout': timeout,
            'top_p': self.top_p,
            'top_k': self.top_k,
            'temperature': self.temperature,
            'max_new_tokens': self.max_new_tokens,
            'repetition_penalty': self.repetition_penalty,
            **kwargs
        }

        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }

        response = requests.post(f"{self.api_url}", json=payload, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        #print(f"Debug: Response JSON: {data}")

        if 'choices' not in data:
            raise KeyError(f"'choices' key not found in the response: {data}")

        resp = [item['message']['content'] for item in data['choices']]
        if not batched:
            return resp[0]
        return resp

    def stream_chat(self,
                    inputs: List[dict],
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
            inputs (List[dict]): 用户在本轮对话中的输入
            sequence_start (bool): 会话开始标志
            sequence_end (bool): 会话结束标志
            stream (bool): 如果启用，则以流式格式返回
            ignore_eos (bool): 忽略结束符号的指示
            skip_special_tokens (bool): 是否在解码过程中移除特殊标记，默认为 False
            timeout (int): 等待响应的最大时间

        Returns:
            tuple(Status, str, int): 状态、文本/聊天完成结果、生成的标记数量
        """
        
        # 更新生成参数
        gen_params = self.update_gen_params(**kwargs)
        max_new_tokens = gen_params.pop('max_new_tokens')
        gen_params.update(max_tokens=max_new_tokens)
        
        # 解析模板
        #print("inputs",inputs)
        prompt = self.template_parser(inputs)
        if isinstance(prompt, str):
            prompt = [prompt]
            batched = False
        else:
            batched = True

        messages = [{'role': 'user', 'content': pro} for pro in prompt]
        #print("prompt",prompt)
        # 请求头
        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }

        # 请求体
        payload = {
            'model': self.model_name,
            'messages': messages,
            'session_id': session_id,
            'sequence_start': sequence_start,
            'sequence_end': sequence_end,
            'ignore_eos': ignore_eos,
            'skip_special_tokens': skip_special_tokens,
            'timeout': timeout,
            'top_p': self.top_p,
            'top_k': self.top_k,
            'temperature': self.temperature,
            'max_new_tokens': self.max_new_tokens,
            'repetition_penalty': self.repetition_penalty,
            **gen_params
        }
        #print("1",payload)
        #print("2",headers)
        # 发起请求
        response = requests.post(f"{self.api_url}", json=payload, headers=headers, stream=True)
        #print("3",response.json())
        #print("4",response.text)
        #print("Debug: Full Response Text:", response.text)
        #print("Debug: Response Status Code:", response.status_code)
        response.raise_for_status()

        # 初始化响应字符串
        resp = ''
        # 初始化完成标志
        finished = False
        # 获取停止词
        stop_words = self.stop_words

        # 解析流式响应
        for line in response.iter_lines():
            if line:
                #print(f"Raw Streamed Line: {line.decode('utf-8')}")  # 添加这一行
                data = json.loads(line.decode('utf-8'))
                #print(f"Debug: Streamed Line Data: {data}")
                if 'choices' in data:
                    resp += data['choices'][0]['message']['content']
                if not resp:
                    continue
                for sw in stop_words:
                    if sw in resp:
                        resp = self.filter_suffix(resp, stop_words)
                        finished = True
                        break
                yield ModelStatusCode.STREAM_ING, resp, None
                if finished:
                    break
        yield ModelStatusCode.END, resp, None


    @staticmethod
    def filter_suffix(text, stop_words):
        for sw in stop_words:
            if text.endswith(sw):
                return text[: -len(sw)]
        return text
