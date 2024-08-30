[{'role': 'user', 'content': '<|im_start|>system\n当开启工具以及代码时，根据需求选择合适的工具进行调用<|im_end|>\n<|im_start|>system name=<|plugin|>\n你可以使用如下工具：\n[\n    {\n        "name": "BingBrowser.get_arxiv_paper_summry",\n        "description": "This is the subfunction for tool \'BingBrowser\', you can use this tool. The description of this function is: \\n",\n        "parameters": [\n            {\n                "name": "content",\n                "type": "STRING",\n                "description": ""\n            }\n        ],\n        "required": [\n         
   "content"\n        ],\n        "parameter_description": "If you call this tool, you must pass arguments in the JSON format {key: value}, where the key is the parameter name."\n    },\n    {\n        "name": "BingBrowser.search",\n        "description": "This is the subfunction for tool \'BingBrowser\', you can use this tool. The description of this function is: \\nBING search API\\nArgs:\\n    query (List[str]): list of search query strings",\n        "parameters": [\n            {\n                "name": "query",\n                "type": "STRING",\n                "description": ""\n            }\n        ],\n        "required": [\n            "query"\n        ],\n        "parameter_description": "If you call this tool, you must pass arguments in the JSON format {key: value}, where the key is the parameter name."\n    },\n    {\n        "name": "BingBrowser.select",\n        "description": "This is the subfunction for tool \'BingBrowser\', you can use this tool. The description of this function is: \\nget the detailed content on the selected pages.",\n        "parameters": [\n            {\n                "name": "select_ids",\n                "type": "NUMBER",\n                "description": "list of index to select. Max number of index to be selected is no more than 4."\n            }\n        ],\n        "required": [\n            "select_ids"\n        ],\n        "parameter_description": "If you call this tool, you must pass arguments in the JSON format {key: value}, where the key is the parameter name."\n    },\n    {\n        "name": "BingBrowser.open_url",\n        "description": "This is the subfunction for tool \'BingBrowser\', you can use this tool. The description of this function is: \\n",\n        "parameters": [\n          
  {\n                "name": "url",\n                "type": "STRING",\n                "description": ""\n            }\n        ],\n        "required": [\n            "url"\n        ],\n        "parameter_description": "If you call this tool, you must pass arguments in the JSON format {key: value}, where the key is the parameter name."\n    },\n    {\n        "name": "BingBrowser.from_github_get_arxiv_links",\n        "description": "This is the subfunction for tool \'BingBrowser\', you can use this tool. The description of this function is: \\n从给定的网页URL中提取所有指向arXiv的链接.",\n        "parameters": [\n            {\n                "name": "url",\n                "type": "STRING",\n                "description": "需要处理的网页URL."\n            }\n        ],\n        "required": [\n            "url"\n        ],\n        "parameter_description": "If you call this tool, you must pass arguments in the JSON format {key: value}, where the key is the parameter name."\n    }\n]\n如果你已经获得足够信息，请直接给出答案. 避免不必要的工具调用! 同时注意你可以使用的工具，不要随意捏造！<|im_end|>\n<|im_start|>user\n请告诉我当前纽约市的天气情况。<|im_end|>\n<|im_start|>assistant\n'}]