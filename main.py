import time

from llm_api.deepseek import deepseek_response
from llm_api.kimi import Kimi_response
from llm_api.internlm import get_response

from prompt.prompt import (
    prompt_to_catalogue,
    prompt_abs_ins,
    prompt_con,
    prompt_to_section,
    prompt_get_score,
    catalogue,
    prompt_to_bib
)

from function.function import (
    from_github_get_arxiv_links, 
    get_arxiv_paper_summary, 
    save_summary_to_json,
    extract_title_as_string,
    paragraphing,
    get_required_summary,
    save_markdown,
    extract_and_combine,
    get_arxiv_paper_summary_2,
    get_required_summary_2,
    get_bib
)

"""
# 1.新建summary.json
github_url = 'https://github.com/hollowknightone/survey/blob/main/README.md'
links = from_github_get_arxiv_links(github_url)
#summaries = get_arxiv_paper_summary(links)
summaries = get_arxiv_paper_summary_2(links)
save_summary_to_json(summaries, 'summary.json')
"""
#2.根据摘要进行分组
"""
# 只使用summary_title来写目录，但internlm效果不好，用GPT
summary_title = extract_title_as_string('summary.json')
prompt = f"{prompt_to_catalogue}以下是几篇相关研究方向论文的ID和题目：{summary_title}"
print(prompt)
#catalogue = deepseek_response(prompt) 用GPT
# 多轮对话：在创建完成目录之后，要求写出abs，ins，con,用GPT
#
"""


# 3.分组写段落
i=1
final = ""
bibs = ""
catalogue_sections = paragraphing(catalogue, "[over]")
for x in catalogue_sections:
    #print(x)
    """
    if i < 5:
        i = i+1
        continue
    # 对哪一段不满意，进行针对更改
    if i not in {8}:
        i = i+1
        continue
    """
    required_summary = get_required_summary(x, 'summary.json')
    prompt_section = f"{prompt_to_section}英文回答。该段涉及的论文和对应的摘要如下：{required_summary}"
    #print(prompt_section)
    #print(i,"组总结完成")
    section = get_response(prompt_section)
    #print(section)
    
    # todo：引入一个 llm judger 评价style是否符合 如果不符合就重新生成
    prompt = f"{prompt_get_score}需要打分的片段如下：{section}"
    score, combined_text = extract_and_combine(get_response(prompt))
    #print(score)
    #print("combined_text",combined_text)
    t = 1
    score = int(score)
    while score < 86 and t < 5 :
        print(i,"组总结不通过，修改第",t,"次")
        prompt_section = f"对于llm生成的综述片段：{section}评价为不合格,理由和改进意见如下：{combined_text}请在prompt下重新生成结果，prompt：{prompt_section}"
        section = get_response(prompt_section)
        prompt = f"{prompt_get_score}需要打分的片段如下：{section}"
        score, combined_text = extract_and_combine(get_response(prompt))
        score = int(score)
        #print(score)
        t = t+1
    require_to_bib = get_bib(x, 'summary.json')
    prompt = f"{prompt_to_bib}需要写论文格式的片段如下：{section}所需要的论文信息如下：{require_to_bib}"
    bib = get_response(prompt)
    prompt_section = f"{prompt_to_section}英文回答。该段涉及的论文和对应的摘要如下：{required_summary}论文引用如下：{bib},根据论文引用对综述片段修改：{section}"
    section = get_response(prompt_section)
    
    save_markdown(x,"result\ex_section.md")
    save_markdown(section,"result\ex_section.md")
    save_markdown(i,"result\ex_bib.md")
    save_markdown(bib,"result\ex_bib.md")
    """
    # 对哪一段不满意，进行针对保存
    number = str(i)
    save_markdown(x, f"result\\{number}ex_again_section.md")
    save_markdown(section, f"result\\{number}ex_again_section.md")
    save_markdown(bib, f"result\\{number}ex_again_bib.md")
    """
    print(i,"组总结完成")
    bibs = bibs + bib + "\n"
    i = i+1
    final = final  + "\n" + section + "\n"
    #api调用有限制
    #if i==2:
    #    exit()
    if i==3 or i==5 or i==7 or i==9:
        time.sleep(60)


save_markdown(final, "result\example822_latex.md")
save_markdown(bibs, "result\example822_bib.md")
""""""



































































































