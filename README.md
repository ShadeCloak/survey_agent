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




