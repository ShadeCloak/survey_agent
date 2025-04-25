## 8.30

#### survey agent：

目录的进度，之前搞不清多少篇论文和一批次挤在一块或者一篇一篇分开已解决



多批次+浓缩摘要，目前一次10篇，效果稳定良好

- 整体的辅助信息产生负面信息

  > 最后给一个更新迭代的目录和整体辅助信息

- few-shot产生负面影响：模型不会自己取标题了，直接拿例子里面的标题

  > 可能是例子不太好？没给sentence，只有更新前后目录示例

- 目前是不用few-shot,



GPT和deepseek都有单独分论文成子标题的大概率现象，但是也就一两篇，之前没有过

- 我猜确实是这样的？

  > 这种论文直接丢？还是怎么消除？



生成了多次，整体上title下面的section分类大差不差，再往下的subsection每次出入还是很明显

- section分类和轮次很相关，deepseek很明显，GPT还好一些

- 怎么判断目录质量

  > 1.每次更新说明理由，这个理由不仅可以迭代到下一轮，是不是可以每一轮对目录和理由打分？
  >
  > 2.最后整体打分，不合格推翻重来，或者积累出经验再推翻重来，直到达到阈值



刚想到一个点，可不可以先按之前的所有论文+title给一个粗目录，然后再多批次+浓缩摘要一步一步优化更新，这样打分也相对好打一些，给理由也好给，section分布也稳定，因为之前的辅助信息证明是副作用之后，就没有所有论文的整体视野了



#### error：

- [x] 大批量数据构造生成

- [ ] deepseek和lagent的接口

- lagent的模板deepseek好像follow的不是很好，给不出正确调用工具的格式，就一直进不去工具里面

  > 要不直接用InternLM



internlm：

> 好的，我需要调用工具获取天气信息，稍等一下<|action_start|><|plugin|>
> {"name": "BingBrowser.open_url", "parameters": {"url": "https://www.bing.com/weather/location/new york, ny"}}



deepseek：

> 为了获取当前纽约市的天气情况，我将使用BingBrowser.search工具进行搜索。以下是我将执行的步骤：
>
> 1. 使用BingBrowser.search工具搜索当前纽约市的天气情况。
>
> ```json
> {
>     "query": "current weather in New York City"
> }
> ```
>
> 请稍等，我将进行搜索并返回结果。



## 8.27

#### survey agent：

多批次：每次6篇，不加整体辅助信息

- 每一轮次，要么6篇挤在一块，要么6篇一篇一篇分开（GPT）

  > 多批次+浓缩摘要；few-shot



浓缩摘要

- 效果提升不明显，甚至搞不清有多少篇论文



## 8.23

#### survey agent：

创建目录的api：现在是使用GPT

- internlm效果说实话有点很差，deepseek和kimi合格率也很低

- GPT，稍微好一点，有时候也要多轮强调来改进

  > 这个多轮提要求强调我觉得可以设计成用户交互，多轮对话一步一步确定目录



创建目录，现在是prompt+示例+所有的title

- 信息量不足，误差太大，仅凭title分组太勉强

  > 1.分步骤创建目录，一次6-7篇进行分组 -> 只试了试internlm，效果不好，有时候多有时候少
  >
  > 2.有一个想法是llm对每一篇根据摘要再浓缩一下，根据浓缩的摘要，title分组
  >
  > 3.还有个想法就是引入一个 llm judger，每次提供几篇论文摘要，来评价这几篇的目录位置是否合理，给出修改建议，可以修改建议全部汇总之后作为辅助信息优化目录，或者也可以每给出修改建议就进行优化，甚至可以重复评价几篇优化达到分数或者次数，但这样时间有点长 



写摘要，instruction，conclution，现在是GPT生成目录完prompt引导直接生成

- 还是那个问题：只看得见title和目录，水平低

  > 最后生成？但是太长了



写section的时候，

- 风格不统一，这个风格指总体风格学术化了，但细节上有出入

  > 估计是每次单独输出？不知道多轮对话输出怎么样

- 之前在这里引入一个 llm judger，效果有提升，但是根据feedback信息，优化的时候两次输出差不多

  > 目前是理由+修改意见+上一轮section=这一轮section？会不会每次单独输出好一点

- 现在是对于不满意，或者llm judger漏掉的或者次数达上限的secion，可以单独指定重新生成

  > 这个我觉得也可以设计成用户交互



严格意义来说不算是Agent，只能说是prompt工程

> 所以是不是分组的时候，llm可以随时打开summary.json找信息？
>
> 还有总体结构的图和对比的表格



还有这个其他领域的综述，还没测试过，估计会出现新问题













调用GPT得到的可能的目录：

\title{Recent Advances in Code Reasoning and Generation with Large Language Models: A Survey}

\section{Program-Aided Language Models for Reasoning}

\subsection{Mathematical and Numerical Reasoning via Code}
%IDs:['1', '2', '3', '4', '13', '14', '17']
%[over]

\subsection{Program Generation and Execution for Enhanced Reasoning}
%IDs:['5', '6', '11', '12', '15', '16', '18']
%[over]

\section{Code Integration and Structural Reasoning}

\subsection{Leveraging Code for Structured Reasoning and Generalization}
%IDs:['7', '9', '8', '19', '22', '23', '24']
%[over]

\subsection{Evaluation and Challenges in Code Reasoning with LLMs}
%IDs:['10', '25', '26', '20', '21', '27', '28']
%[over]

\section{Interactive and Autonomous Code Generation}

\subsection{Interactive and Multi-Agent Code Generation Systems}
%IDs:['29', '30', '31', '32', '33', '34', '38']
%[over]

\subsection{Autonomous Code Generation and Self-Improvement}
%IDs:['35', '36', '37', '39', '40', '41', '42', '43']
%[over]

\section{Refinement, Optimization, and Benchmarking in Code Generation}

\subsection{Iterative Refinement and Self-Optimization}
%IDs:['53', '54', '55', '57', '59', '60', '61', '63']
%[over]

\subsection{Benchmarking and Evaluation of LLM-Based Code Generation}
%IDs:['58', '62', '44', '45', '46', '47', '48', '49']
%[over]

\subsection{Advanced Techniques in Code Repair and Generation}
%IDs:['64', '65', '66', '67', '50', '51', '52', '56', '68']
%[over]

——

\title{Advances in Code-based Reasoning and Execution with Large Language Models: A Survey}

\section{Code Integration and Mathematical Reasoning}

\subsection{Mathematical Reasoning with Code Support}
%IDs:['1','2','3','4','5','13','15','17']
%[over]

\subsection{Program Abstractions and Code Integration}
%IDs:['6','7','8','9','10','11','12','14']
%[over]

\section{Challenges and Techniques in Code Generation}

\subsection{Challenges in Code Reasoning and Simulation}
%IDs:['16','22','23','24','25','26','27','28']
%[over]

\subsection{Techniques for Enhanced Code Generation}
%IDs:['18','19','20','21','32','33','41','43']
%[over]

\section{Interactive and Self-Improving Code Systems}

\subsection{Interactive Program Synthesis and Refinement}
%IDs:['29','30','31','50','51','58','62','68']
%[over]

\subsection{Iterative Refinement and Self-Debugging}
%IDs:['34','35','36','37','38','39','40','42']
%[over]

\subsection{Self-Repair and Optimization Strategies}
%IDs:['44','45','46','47','48','49','53','54']
%[over]

\subsection{Advanced Techniques for Code Debugging}
%IDs:['55','56','57','59','60','61','63','64','65','66','67']
%[over]



______________________________

示例一：
@inproceedings{2022InstructGPT,
  author       = {Long Ouyang and
                  Jeffrey Wu and
                  Xu Jiang and
                  Diogo Almeida and
                  Carroll L. Wainwright and
                  Pamela Mishkin and
                  Chong Zhang and
                  Sandhini Agarwal and
                  Katarina Slama and
                  Alex Ray and
                  John Schulman and
                  Jacob Hilton and
                  Fraser Kelton and
                  Luke Miller and
                  Maddie Simens and
                  Amanda Askell and
                  Peter Welinder and
                  Paul F. Christiano and
                  Jan Leike and
                  Ryan Lowe},
  title        = {Training language models to follow instructions with human feedback},
  booktitle    = {NeurIPS},
  year         = {2022},
  url          = {http://papers.nips.cc/paper\_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html}
}

@article{2022FLAN,
  author    = {Hyung Won Chung and
               Le Hou and
               Shayne Longpre and
               Barret Zoph and
               Yi Tay and
               William Fedus and
               Eric Li and
               Xuezhi Wang and
               Mostafa Dehghani and
               Siddhartha Brahma and
               Albert Webson and
               Shixiang Shane Gu and
               Zhuyun Dai and
               Mirac Suzgun and
               Xinyun Chen and
               Aakanksha Chowdhery and
               Sharan Narang and
               Gaurav Mishra and
               Adams Yu and
               Vincent Y. Zhao and
               Yanping Huang and
               Andrew M. Dai and
               Hongkun Yu and
               Slav Petrov and
               Ed H. Chi and
               Jeff Dean and
               Jacob Devlin and
               Adam Roberts and
               Denny Zhou and
               Quoc V. Le and
               Jason Wei},
  title     = {Scaling Instruction-Finetuned Language Models},
  journal   = {CoRR},
  volume    = {abs/2210.11416},
  year      = {2022},
  url       = {https://doi.org/10.48550/arXiv.2210.11416},
  doi       = {10.48550/arXiv.2210.11416},
  eprinttype = {arXiv},
  eprint    = {2210.11416}
}




示例二：

@inproceedings{ribeiro2016why,
  author    = {Ribeiro, Marco T{\'{u}}lio and
               Singh, Sameer and
               Guestrin, Carlos},
  title     = {"Why Should {I} Trust You?": Explaining the Predictions of Any Classifier},
  booktitle = {Proceedings of the Demonstrations Session of 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)},
  year      = {2016},
  url       = {https://doi.org/10.18653/v1/n16-3020},
  doi       = {10.18653/v1/n16-3020},
}

@inproceedings{lundberg2017aunified,
  author    = {Lundberg, Scott M. and
               Lee, Su{-}In},
  title     = {A Unified Approach to Interpreting Model Predictions},
  booktitle = {Advances in Neural Information Processing Systems (NIPS)},
  year      = {2017},
  url       = {https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html}
}

@inproceedings{chen2018learning,
  author    = {Chen, Jianbo and
               Song, Le and
               Wainwright, Martin J. and
               Jordan, Michael I.},
  title     = {Learning to Explain: An Information-Theoretic Perspective on Model
               Interpretation},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
  year      = {2018},
  url       = {http://proceedings.mlr.press/v80/chen18j.html}
}

@inproceedings{park18multimodal,
  author    = {Park, Dong Huk and
               Hendricks, Lisa Anne and
               Akata, Zeynep and
               Rohrbach, Anna and
               Schiele, Bernt and
               Darrell, Trevor and
               Rohrbach, Marcus},
  title     = {Multimodal Explanations: Justifying Decisions and Pointing to the
               Evidence},
  booktitle = {Proceedings of 2018 {IEEE} Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2018},
  url       = {http://openaccess.thecvf.com/content\_cvpr\_2018/html/Park\_Multimodal\_Explanations\_Justifying\_CVPR\_2018\_paper.html},
  doi       = {10.1109/CVPR.2018.00915}
}

@inproceedings{kim2018textual,
  author    = {Kim, Jinkyu and
               Rohrbach, Anna and
               Darrell, Trevor and
               Canny, John F. and
               Akata, Zeynep},
  title     = {Textual Explanations for Self-Driving Vehicles},
  booktitle = {In Proceedings of the European conference on computer vision (ECCV)},
  year      = {2018},
}

@inproceedings{ling2017program,
    title = "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems",
    author = "Ling, Wang  and
      Yogatama, Dani  and
      Dyer, Chris  and
      Blunsom, Phil",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (ACL)",
    year = "2017",
    url = "https://aclanthology.org/P17-1015",
    doi = "10.18653/v1/P17-1015",
}

示例三：

@inproceedings{rafailov2023direct,
  title = {Direct {{Preference Optimization}}: {{Your Language Model}} Is {{Secretly}} a {{Reward Model}}},
  shorttitle = {Direct {{Preference Optimization}}},
  booktitle = {Advances in {{Neural Information Processing Systems}} ({{NeurIPS}})},
  author = {Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Manning, Christopher D. and Ermon, Stefano and Finn, Chelsea},
  year = {2023},
  volume = {36},
  url = {https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html},
  urldate = {2024-04-02}
}

@misc{zhao2023slichf,
  title = {{{SLiC-HF}}: {{Sequence Likelihood Calibration}} with {{Human Feedback}}},
  shorttitle = {{{SLiC-HF}}},
  author = {Zhao, Yao and Joshi, Rishabh and Liu, Tianqi and Khalman, Misha and Saleh, Mohammad and Liu, Peter J.},
  year = {2023},
  number = {arXiv:2305.10425},
  eprint = {2305.10425},
  publisher = {arXiv},
  urldate = {2023-05-22},
  archiveprefix = {arxiv},
  note = {arXiv: \href{https://arxiv.org/abs/2305.10425}{2305.10425}. preprint}
}

@inproceedings{kang2023reward,
  title = {Beyond {{Reward}}: {{Offline Preference-guided Policy Optimization}}},
  shorttitle = {Beyond {{Reward}}},
  booktitle = {Proceedings of the {{International Conference}} on {{Machine Learning}} ({{ICML}})},
  author = {Kang, Yachen and Shi, Diyuan and Liu, Jinxin and He, Li and Wang, Donglin},
  year = {2023},
  publisher = {PMLR},
  issn = {2640-3498},
  url = {https://proceedings.mlr.press/v202/kang23b.html},
  urldate = {2023-12-21}
}




