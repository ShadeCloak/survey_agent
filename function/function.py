import requests
from bs4 import BeautifulSoup
import re
import json
import arxiv

def from_github_get_arxiv_links(url: str) -> list:
    """
    从给定的网页URL中提取所有指向arXiv的链接.

    Args:
        url (str): 需要处理的网页URL.

    Returns:
        list: 包含论文标题和arXiv链接的字典列表.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    papers = []

    for link in soup.find_all('a'):
        arxiv_url = link.get('href')
        if arxiv_url and 'arxiv.org/abs/' in arxiv_url:
            title = link.text.strip()

            # 检查文本是否为占位符，例如 "paper"
            if title.lower() == 'paper' or not title:
                previous = link.find_previous(string=True)
                if previous:
                    title = previous.strip()

                if not title:
                    title = "Unknown Title"

            full_url = arxiv_url if arxiv_url.startswith('http') else f'https://arxiv.org{arxiv_url}'
            papers.append({"title": title, "url": full_url})

    return papers

def get_arxiv_paper_summary(links: list) -> list:
    """获取arXiv论文的摘要并构建包含编号的字典列表.
    
    Args:
        links (list): 包含论文标题和arXiv链接的字典列表.
    
    Returns:
        list: 包含编号的摘要信息的字典列表.
    """
    client = arxiv.Client()
    summaries = []

    for idx, paper in enumerate(links, start=1):
        arxiv_url = paper['url']
        arxiv_id = arxiv_url.split('/')[-1]
        search = arxiv.Search(id_list=[arxiv_id])
        result = next(client.results(search), None)
        
        if result:
            paper_summary = {
                "id": idx,
                "title": result.title,
                "abstract": result.summary,
                "url": arxiv_url
            }
            summaries.append(paper_summary)
    
    return summaries

def get_arxiv_paper_summary_2(links: list) -> list:
    """获取arXiv论文的摘要，并构建包含编号、作者和年份的字典列表.
    
    Args:
        links (list): 包含论文标题和arXiv链接的字典列表.
    
    Returns:
        list: 包含编号、标题、摘要、作者和年份信息的字典列表.
    """
    client = arxiv.Client()
    summaries = []

    for idx, paper in enumerate(links, start=1):
        arxiv_url = paper['url']
        arxiv_id = arxiv_url.split('/')[-1]
        search = arxiv.Search(id_list=[arxiv_id])
        result = next(client.results(search), None)
        
        if result:
            paper_summary = {
                "id": idx,
                "title": result.title,
                "abstract": result.summary,
                "authors": [author.name for author in result.authors],  # 获取作者列表
                "year": result.published.year,  # 获取出版年份
                "url": arxiv_url
            }
            summaries.append(paper_summary)
    
    return summaries

def save_summary_to_json(summaries: list, output_file: str) -> None:
    """将摘要保存为JSON格式.
    
    Args:
        summaries (list): 包含编号的摘要信息的字典列表.
        output_file (str): 要保存的文件名.
    """
    summary_content = {
        "number": len(summaries),
        "content": summaries
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary_content, f, ensure_ascii=False, indent=4)

def extract_title_as_string(json_file: str) -> str:
    """
    从给定的JSON文件中提取所有title，并将其合并成一个字符串，包括每个论文的编号.

    Args:
        json_file (str): 包含摘要信息的JSON文件路径.

    Returns:
        str: 合并后的字符串.
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    summaries = data.get("content", [])
    combined_string = ""

    for summary in summaries:
        paper_id = summary.get("id", "No ID")
        title = summary.get("title", "No Title")
        
        summary_text = f"ID: {paper_id}\nTitle: {title}\n"
        combined_string += summary_text

    return combined_string

def paragraphing(text: str, marker: str) -> list:
    """
    根据指定的标记 [marker] 从文本中提取多个段落。

    参数:
    text (str): 包含多个段落的原始文本。
    marker (str): 用作分隔段落的标记。

    返回:
    list: 提取出的段落列表。
    """
    parts = text.split(marker)
    
    prompts = [part.strip() for part in parts if part.strip()]
    
    return prompts

def get_required_summary(output, summary_file):
    # 从输出中提取需要查找的论文编号
    ids_to_find = output.split("IDs:['")[1].split("']")[0].split("', '")
    
    # 读取 summary.json 文件内容
    with open(summary_file, 'r', encoding='utf-8') as file:
        summary_data = json.load(file)
    
    # 初始化一个列表来存储每篇论文的完整内容
    papers_content = []
    
    # 查找与编号对应的论文内容并拼接成字符串
    for paper in summary_data["content"]:
        if str(paper["id"]) in ids_to_find:
            paper_str = f"Title: {paper['title']}\nAbstract: {paper['abstract']}\nURL: {paper['url']}\n"
            papers_content.append(paper_str)
    
    # 将所有内容拼接成一个字符串
    return "\n".join(papers_content)

def get_required_summary_2(output, summary_file):
    # 从输出中提取需要查找的论文编号
    ids_to_find = output.split("IDs:['")[1].split("']")[0].split("', '")
    
    # 读取 summary.json 文件内容
    with open(summary_file, 'r', encoding='utf-8') as file:
        summary_data = json.load(file)
    
    # 初始化一个列表来存储每篇论文的完整内容
    papers_content = []
    
    # 查找与编号对应的论文内容并拼接成字符串
    for paper in summary_data["content"]:
        if str(paper["id"]) in ids_to_find:
            # 构建包含标题、摘要、作者、年份和URL的字符串
            paper_str = (
                f"Title: {paper['title']}\n"
                f"Abstract: {paper['abstract']}\n"
                f"Authors: {', '.join(paper['authors'])}\n"  # 拼接作者列表
                f"Year: {paper['year']}\n"  # 添加年份
                f"URL: {paper['url']}\n"
            )
            papers_content.append(paper_str)
    
    # 将所有内容拼接成一个字符串
    return "\n".join(papers_content)

def get_bib(output, summary_file):
    # 从输出中提取需要查找的论文编号
    ids_to_find = output.split("IDs:['")[1].split("']")[0].split("', '")
    
    # 读取 summary.json 文件内容
    with open(summary_file, 'r', encoding='utf-8') as file:
        summary_data = json.load(file)
    
    # 初始化一个列表来存储每篇论文的完整内容
    papers_content = []
    
    # 查找与编号对应的论文内容并拼接成字符串
    for paper in summary_data["content"]:
        if str(paper["id"]) in ids_to_find:
            # 构建包含标题、摘要、作者、年份和URL的字符串
            paper_str = (
                f"Title: {paper['title']}\n"
                f"Authors: {', '.join(paper['authors'])}\n"  # 拼接作者列表
                f"Year: {paper['year']}\n"  # 添加年份
                f"URL: {paper['url']}\n"
            )
            papers_content.append(paper_str)
    
    # 将所有内容拼接成一个字符串
    return "\n".join(papers_content)

def save_markdown(content, filename):
    """
    将Markdown格式的字符串保存为.md文件。

    参数：
    content (str): 要保存的Markdown内容。
    filename (str): 保存的文件名，需包含.md扩展名。

    示例：
    save_markdown("# 这是一个标题\n这是内容。", "example.md")
    """

    # 打开指定的文件，并以写模式保存内容
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content)

    print(f"文件已成功保存为 {filename}")

def extract_and_combine(text):
    # 使用正则表达式提取分数
    score_match = re.search(r'\((\d{1,3})\)', text)
    score = score_match.group(1) if score_match else None

    # 提取理由和改进建议
    reason_match = re.search(r'理由：(.*?)(改进建议：)', text, re.DOTALL)
    suggestion_match = re.search(r'改进建议：(.*)\)', text, re.DOTALL)
    
    reason = reason_match.group(1).strip() if reason_match else ""
    suggestion = suggestion_match.group(1).strip() if suggestion_match else ""
    
    combined_text = reason + " " + suggestion
    
    return score, combined_text


























