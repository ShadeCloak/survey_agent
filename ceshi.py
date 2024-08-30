from llm_api.deepseek_lagent import get_response
#from llm_api.internlm import get_response

# 使用非流式输出
result = get_response("请告诉我当前纽约市的天气情况。")
print("最终输出:", result)