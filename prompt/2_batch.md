
你是一个写综述的科研人员，你需要仔细理解所提供的很多篇特定主题的论文摘要,
自主一步一步逐渐设计一个目录，来根据论文们的主要研究方向对这些论文进行分组。
考虑到一次性将所有论文摘要全部输入太长，所以分批处理，每一次会向你提供：本次需要处理的论文批次、之前批次论文组成的临时目录。
你需要根据本次提供的论文摘要将本次提供的论文ID添加到目录里面，你可能需要新建新的标题对目录进行完善。

要求：
1.每一个分组只需要有三部分：\section{}、%IDs:[]、%[over]。
2.论文编号汇总到注释%[]里面,格式为：%IDs:['1','2']。
5.每一组以%[over]结尾，方便后续操作。

目录结构参考示例：
\title{Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey}

\section{Paradigm 1: Pre-Train then Fine-Tune}

\subsection{The Beginnings of the Paradigm Shift}
%IDs:[]
%[over]

\subsection{Modern Pre-Trained Language Models}
%IDs:[]
%[over]

\subsection{Pre-Training Corpora} 
%IDs:[]
%[over]

\subsection{Fine-Tuning: Applying PLMs to NLP Tasks}
%IDs:[]
%[over]

\section{Paradigm 2: Prompt-based Learning} 

\subsection{Learning from Instructions and Demonstrations}
%IDs:[]
%[over]

\subsection{Template-based Learning} 
%IDs:[]
%[over]
,以下是第3批次的论文ID，题目,和摘要：ID: 13
Title: MuMath-Code: Combining Tool-Use Large Language Models with Multi-perspective Data Augmentation for Mathematical Reasoning
Abstract: The tool-use Large Language Models (LLMs) that integrate with external Python
interpreters have significantly enhanced mathematical reasoning capabilities
for open-source LLMs, while tool-free methods chose another track: augmenting
math reasoning data. However, a great method to integrate the above two
research paths and combine their advantages remains to be explored. In this
work, we firstly include new math questions via multi-perspective data
augmenting methods and then synthesize code-nested solutions to them. The open
LLMs (i.e., Llama-2) are finetuned on the augmented dataset to get the
resulting models, MuMath-Code ($\mu$-Math-Code). During the inference phase,
our MuMath-Code generates code and interacts with the external python
interpreter to get the execution results. Therefore, MuMath-Code leverages the
advantages of both the external tool and data augmentation. To fully leverage
the advantages of our augmented data, we propose a two-stage training strategy:
In Stage-1, we finetune Llama-2 on pure CoT data to get an intermediate model,
which then is trained on the code-nested data in Stage-2 to get the resulting
MuMath-Code. Our MuMath-Code-7B achieves 83.8 on GSM8K and 52.4 on MATH, while
MuMath-Code-70B model achieves new state-of-the-art performance among open
methods -- achieving 90.7% on GSM8K and 55.1% on MATH. Extensive experiments
validate the combination of tool use and data augmentation, as well as our
two-stage training strategy. We release the proposed dataset along with the
associated code for public use.
URL: https://arxiv.org/abs/2405.07551

ID: 14
Title: Learning to Reason via Program Generation, Emulation, and Search
Abstract: Program synthesis with language models (LMs) has unlocked a large set of
reasoning abilities; code-tuned LMs have proven adept at generating programs
that solve a wide variety of algorithmic symbolic manipulation tasks (e.g. word
concatenation). However, not all reasoning tasks are easily expressible as
code, e.g. tasks involving commonsense reasoning, moral decision-making, and
sarcasm understanding. Our goal is to extend an LM's program synthesis skills
to such tasks and evaluate the results via pseudo-programs, namely Python
programs where some leaf function calls are left undefined. To that end, we
propose, Code Generation and Emulated EXecution (CoGEX). CoGEX works by (1)
training LMs to generate their own pseudo-programs, (2) teaching them to
emulate their generated program's execution, including those leaf functions,
allowing the LM's knowledge to fill in the execution gaps; and (3) using them
to search over many programs to find an optimal one. To adapt the CoGEX model
to a new task, we introduce a method for performing program search to find a
single program whose pseudo-execution yields optimal performance when applied
to all the instances of a given dataset. We show that our approach yields large
improvements compared to standard in-context learning approaches on a battery
of tasks, both algorithmic and soft reasoning. This result thus demonstrates
that code synthesis can be applied to a much broader class of problems than
previously considered. Our released dataset, fine-tuned models, and
implementation can be found at \url{https://github.com/nweir127/CoGEX}.
URL: https://arxiv.org/abs/2405.16337

ID: 15
Title: Arithmetic Reasoning with LLM: Prolog Generation & Permutation
Abstract: Instructing large language models (LLMs) to solve elementary school math
problems has shown great success using Chain of Thought (CoT). However, the CoT
approach relies on an LLM to generate a sequence of arithmetic calculations
which can be prone to cascaded calculation errors. We hypothesize that an LLM
should focus on extracting predicates and generating symbolic formulas from the
math problem description so that the underlying calculation can be done via an
external code interpreter. We investigate using LLM to generate Prolog programs
to solve mathematical questions. Experimental results show that our
Prolog-based arithmetic problem-solving outperforms CoT generation in the GSM8K
benchmark across three distinct LLMs. In addition, given the insensitive
ordering of predicates and symbolic formulas in Prolog, we propose to permute
the ground truth predicates for more robust LLM training via data augmentation.
URL: https://arxiv.org/abs/2405.17893

ID: 16
Title: Can LLMs Reason in the Wild with Programs?
Abstract: Large Language Models (LLMs) have shown superior capability to solve
reasoning problems with programs. While being a promising direction, most of
such frameworks are trained and evaluated in settings with a prior knowledge of
task requirements. However, as LLMs become more capable, it is necessary to
assess their reasoning abilities in more realistic scenarios where many
real-world problems are open-ended with ambiguous scope, and often require
multiple formalisms to solve. To investigate this, we introduce the task of
reasoning in the wild, where an LLM is tasked to solve a reasoning problem of
unknown type by identifying the subproblems and their corresponding formalisms,
and writing a program to solve each subproblem, guided by a tactic. We create a
large tactic-guided trajectory dataset containing detailed solutions to a
diverse set of reasoning problems, ranging from well-defined single-form
reasoning (e.g., math, logic), to ambiguous and hybrid ones (e.g., commonsense,
combined math and logic). This allows us to test various aspects of LLMs
reasoning at the fine-grained level such as the selection and execution of
tactics, and the tendency to take undesired shortcuts. In experiments, we
highlight that existing LLMs fail significantly on problems with ambiguous and
mixed scope, revealing critical limitations and overfitting issues (e.g.
accuracy on GSM8K drops by at least 50\%). We further show the potential of
finetuning a local LLM on the tactic-guided trajectories in achieving better
performance. Project repo is available at
github.com/gblackout/Reason-in-the-Wild
URL: https://arxiv.org/abs/2406.13764

ID: 17
Title: DotaMath: Decomposition of Thought with Code Assistance and Self-correction for Mathematical Reasoning
Abstract: Large language models (LLMs) have made impressive progress in handling simple
math problems, yet they still struggle with more challenging and complex
mathematical tasks. In this paper, we introduce a series of LLMs that employs
the Decomposition of thought with code assistance and self-correction for
mathematical reasoning, dubbed as DotaMath. DotaMath models tackle complex
mathematical tasks by decomposing them into simpler logical subtasks,
leveraging code to solve these subtasks, obtaining fine-grained feedback from
the code interpreter, and engaging in self-reflection and correction. By
annotating diverse interactive tool-use trajectories and employing query
evolution on GSM8K and MATH datasets, we generate an instruction fine-tuning
dataset called DotaMathQA with 574K query-response pairs. We train a series of
base LLMs using imitation learning on DotaMathQA, resulting in DotaMath models
that achieve remarkable performance compared to open-source LLMs across various
in-domain and out-of-domain benchmarks. Notably, DotaMath-deepseek-7B showcases
an outstanding performance of 64.8% on the competitive MATH dataset and 86.7%
on GSM8K. Besides, DotaMath-deepseek-7B maintains strong competitiveness on a
series of in-domain and out-of-domain benchmarks (Avg. 80.1%). Looking forward,
we anticipate that the DotaMath paradigm will open new pathways for addressing
intricate mathematical problems. Our code is publicly available at
https://github.com/ChengpengLi1003/DotaMath.
URL: https://arxiv.org/abs/2407.04078

ID: 18
Title: CIBench: Evaluating Your LLMs with a Code Interpreter Plugin
Abstract: While LLM-Based agents, which use external tools to solve complex problems,
have made significant progress, benchmarking their ability is challenging,
thereby hindering a clear understanding of their limitations. In this paper, we
propose an interactive evaluation framework, named CIBench, to comprehensively
assess LLMs' ability to utilize code interpreters for data science tasks. Our
evaluation framework includes an evaluation dataset and two evaluation modes.
The evaluation dataset is constructed using an LLM-human cooperative approach
and simulates an authentic workflow by leveraging consecutive and interactive
IPython sessions. The two evaluation modes assess LLMs' ability with and
without human assistance. We conduct extensive experiments to analyze the
ability of 24 LLMs on CIBench and provide valuable insights for future LLMs in
code interpreter utilization.
URL: https://arxiv.org/abs/2407.10499

辅助信息：ID: 1
Title: PAL: Program-aided Language Models
ID: 2
Title: Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks
ID: 3
Title: Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification
ID: 4
Title: MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning
ID: 5
Title: Chain of Code: Reasoning with a Language Model-Augmented Code Emulator
ID: 6
Title: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
ID: 7
Title: Executable Code Actions Elicit Better LLM Agents
ID: 8
Title: Exploring Hybrid Question Answering via Program-based Prompting
ID: 9
Title: Eliciting Better Multilingual Structured Reasoning from LLMs through Code
ID: 10
Title: FlowMind: Automatic Workflow Generation with LLMs
ID: 11
Title: Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models
ID: 12
Title: AIOS Compiler: LLM as Interpreter for Natural Language Programming and Flow Programming of AI Agents
ID: 13
Title: MuMath-Code: Combining Tool-Use Large Language Models with Multi-perspective Data Augmentation for Mathematical Reasoning
ID: 14
Title: Learning to Reason via Program Generation, Emulation, and Search
ID: 15
Title: Arithmetic Reasoning with LLM: Prolog Generation & Permutation
ID: 16
Title: Can LLMs Reason in the Wild with Programs?
ID: 17
Title: DotaMath: Decomposition of Thought with Code Assistance and Self-correction for Mathematical Reasoning
ID: 18
Title: CIBench: Evaluating Your LLMs with a Code Interpreter Plugin
ID: 19
Title: PyBench: Evaluating LLM Agent on various real-world coding tasks
ID: 20
Title: AdaCoder: Adaptive Prompt Compression for Programmatic Visual Question Answering
ID: 21
Title: Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering
ID: 22
Title: Code Simulation Challenges for Large Language Models
ID: 23
Title: CodeMind: A Framework to Challenge Large Language Models for Code Reasoning
ID: 24
Title: Executing Natural Language-Described Algorithms with Large Language Models: An Investigation
ID: 25
Title: Can Language Models Pretend Solvers? Logic Code Simulation with LLMs
ID: 26
Title: Reasoning Runtime Behavior of a Program with LLM: How Far Are We?
ID: 27
Title: NExT: Teaching Large Language Models to Reason about Code Execution
ID: 28
Title: SelfPiCo: Self-Guided Partial Code Execution with LLMs
ID: 29
Title: Self-collaboration Code Generation via ChatGPT
ID: 30
Title: ChatDev: Communicative Agents for Software Development
ID: 31
Title: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
ID: 32
Title: CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules
ID: 33
Title: CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges
ID: 34
Title: CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing
ID: 35
Title: When LLM-based Code Generation Meets the Software Development Process
ID: 36
Title: RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
ID: 37
Title: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution
ID: 38
Title: Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization
ID: 39
Title: AutoCodeRover: Autonomous Program Improvement
ID: 40
Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
ID: 41
Title: MapCoder: Multi-Agent Code Generation for Competitive Problem Solving
ID: 42
Title: Fight Fire with Fire: How Much Can We Trust ChatGPT on Source Code-Related Tasks?
ID: 43
Title: Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation
ID: 44
Title: Multi-Agent Software Development through Cross-Team Collaboration
ID: 45
Title: MASAI: Modular Architecture for Software-engineering AI Agents
ID: 46
Title: AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology
ID: 47
Title: CodeNav: Beyond tool-use to using real-world codebases with LLM agents
ID: 48
Title: INDICT: Code Generation with Internal Dialogues of Critiques for Both Security and Helpfulness
ID: 49
Title: AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents
ID: 50
Title: Interactive Program Synthesis
ID: 51
Title: Interactive Code Generation via Test-Driven User-Intent Formalization
ID: 52
Title: Improving Code Generation by Training with Natural Language Feedback
ID: 53
Title: Self-Refine: Iterative Refinement with Self-Feedback
ID: 54
Title: Teaching Large Language Models to Self-Debug
ID: 55
Title: Self-Edit: Fault-Aware Code Editor for Code Generation
ID: 56
Title: LeTI: Learning to Generate from Textual Interactions
ID: 57
Title: Is Self-Repair a Silver Bullet for Code Generation?
ID: 58
Title: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback
ID: 59
Title: OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement
ID: 60
Title: Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback
ID: 61
Title: CYCLE: Learning to Self-Refine the Code Generation
ID: 62
Title: LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation
ID: 63
Title: SOAP: Enhancing Efficiency of Generated Code via Self-Optimization
ID: 64
Title: Code Repair with LLMs gives an Exploration-Exploitation Tradeoff
ID: 65
Title: ReflectionCoder: Learning from Reflection Sequence for Enhanced One-off Code Generation
ID: 66
Title: Training LLMs to Better Self-Debug and Explain Code
ID: 67
Title: Requirements are All You Need: From Requirements to Code with LLMs
ID: 68
Title: I Need Help! Evaluating LLM's Ability to Ask for Users' Support: A Case Study on Text-to-SQL Generation
之前所有批次的临时目录：
你是一个写综述的科研人员，你需要仔细理解所提供的很多篇特定主题的论文题目和所给一句话文章描述,
自主一步一步逐渐设计一个目录，来根据论文们的主要研究方向对这些论文进行分组。
考虑到一次性将所有论文摘要全部输入太长，所以分批处理，每一次会向你提供：本次需要处理的论文批次、之前批次论文组成的临时目录。
你需要根据本次提供的论文摘要将本次提供的论文ID添加到目录里面，你可能需要新建新的标题对目录进行完善。
另外有辅助信息：所有论文的ID和标题。
要求：
1.每一个分组只需要有三部分：\section{}、%IDs:[]、%[over]。
2.论文编号汇总到注释%[]里面,格式为：%IDs:['1','2']。
5.每一组以%[over]结尾，方便后续操作。

目录结构参考示例：
\title{Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey}

\section{Paradigm 1: Pre-Train then Fine-Tune}

\subsection{The Beginnings of the Paradigm Shift}
%IDs:[]
%[over]

\subsection{Modern Pre-Trained Language Models}
%IDs:[]
%[over]

\subsection{Pre-Training Corpora} 
%IDs:[]
%[over]

\subsection{Fine-Tuning: Applying PLMs to NLP Tasks}
%IDs:[]
%[over]

\section{Paradigm 2: Prompt-based Learning} 

\subsection{Learning from Instructions and Demonstrations}
%IDs:[]
%[over]

\subsection{Template-based Learning} 
%IDs:[]
%[over]
,以下是第3批次的论文ID，题目,和一句话描述：ID: 21
Title: Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering
Sentence: Introducing PyramidCoder: A hierarchical code generation framework for PVQA, improving accuracy by at least 0.5%, 1.4%, and 2.9% on GQA, VQAv2, and NLVR2 datasets, respectively.

ID: 22
Title: Code Simulation Challenges for Large Language Models
Sentence: This study assesses Large Language Models' coding and algorithmic task simulation capability, proposing a novel Chain of Simulation prompting method to reduce memorization and enhance simulation performance.

ID: 23
Title: CodeMind: A Framework to Challenge Large Language Models for Code Reasoning
Sentence: CodeMind gauges LLMs' reasoning through tasks like Independent and Dependent Execution Reasoning, and Specification Reasoning, showing better understanding of simpler programs but struggling with complex code.

ID: 24
Title: Executing Natural Language-Described Algorithms with Large Language Models: An Investigation
Sentence: This study investigates the ability of large language models to understand and execute algorithms described in natural language, finding mixed results but encouraging further exploration of LLM computation capacities.

ID: 25
Title: Can Language Models Pretend Solvers? Logic Code Simulation with LLMs
Sentence: This study explores the capability of large language models to simulate logic code execution, proposing the Dual Chains of Logic technique to improve accuracy.

ID: 26
Title: Reasoning Runtime Behavior of a Program with LLM: How Far Are We?
Sentence: This study proposes an REval framework to evaluate runtime behavior and logical consistency in code reasoning, revealing poor performance in LLMs with an average accuracy of 44.4% and IC score of 10.3, highlighting the need for improved code reasoning capabilities in LLMs.

ID: 27
Title: NExT: Teaching Large Language Models to Reason about Code Execution
Sentence: We teach LLMs to understand and reason about code execution by inspecting traces and using CoT rationales, improving task-solving and generalizing to absent traces.

ID: 28
Title: SelfPiCo: Self-Guided Partial Code Execution with LLMs
Sentence: SelfPiCo dynamically enhances partial code execution using LLMs, outperforming baseline models by significantly improving the execution success rate and uncovering runtime errors in open-source software and Stack Overflow snippets.

ID: 29
Title: Self-collaboration Code Generation via ChatGPT
Sentence: This study proposes a self-collaboration framework using LLMs like ChatGPT to generate code, where multiple LLM agents act as experts and collaborate on complex tasks without human intervention.

ID: 30
Title: ChatDev: Communicative Agents for Software Development
Sentence: ChatDev uses LLM-powered agents for unified, language-based software development across design, coding, and testing phases.

辅助信息：ID: 1
Title: PAL: Program-aided Language Models
ID: 2
Title: Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks
ID: 3
Title: Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification
ID: 4
Title: MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning
ID: 5
Title: Chain of Code: Reasoning with a Language Model-Augmented Code Emulator
ID: 6
Title: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
ID: 7
Title: Executable Code Actions Elicit Better LLM Agents
ID: 8
Title: Exploring Hybrid Question Answering via Program-based Prompting
ID: 9
Title: Eliciting Better Multilingual Structured Reasoning from LLMs through Code
ID: 10
Title: FlowMind: Automatic Workflow Generation with LLMs
ID: 11
Title: Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models
ID: 12
Title: AIOS Compiler: LLM as Interpreter for Natural Language Programming and Flow Programming of AI Agents
ID: 13
Title: MuMath-Code: Combining Tool-Use Large Language Models with Multi-perspective Data Augmentation for Mathematical Reasoning
ID: 14
Title: Learning to Reason via Program Generation, Emulation, and Search
ID: 15
Title: Arithmetic Reasoning with LLM: Prolog Generation & Permutation
ID: 16
Title: Can LLMs Reason in the Wild with Programs?
ID: 17
Title: DotaMath: Decomposition of Thought with Code Assistance and Self-correction for Mathematical Reasoning
ID: 18
Title: CIBench: Evaluating Your LLMs with a Code Interpreter Plugin
ID: 19
Title: PyBench: Evaluating LLM Agent on various real-world coding tasks
ID: 20
Title: AdaCoder: Adaptive Prompt Compression for Programmatic Visual Question Answering
ID: 21
Title: Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering
ID: 22
Title: Code Simulation Challenges for Large Language Models
ID: 23
Title: CodeMind: A Framework to Challenge Large Language Models for Code Reasoning
ID: 24
Title: Executing Natural Language-Described Algorithms with Large Language Models: An Investigation
ID: 25
Title: Can Language Models Pretend Solvers? Logic Code Simulation with LLMs
ID: 26
Title: Reasoning Runtime Behavior of a Program with LLM: How Far Are We?
ID: 27
Title: NExT: Teaching Large Language Models to Reason about Code Execution
ID: 28
Title: SelfPiCo: Self-Guided Partial Code Execution with LLMs
ID: 29
Title: Self-collaboration Code Generation via ChatGPT
ID: 30
Title: ChatDev: Communicative Agents for Software Development
ID: 31
Title: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
ID: 32
Title: CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules
ID: 33
Title: CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges
ID: 34
Title: CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing
ID: 35
Title: When LLM-based Code Generation Meets the Software Development Process
ID: 36
Title: RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
ID: 37
Title: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution
ID: 38
Title: Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization
ID: 39
Title: AutoCodeRover: Autonomous Program Improvement
ID: 40
Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
ID: 41
Title: MapCoder: Multi-Agent Code Generation for Competitive Problem Solving
ID: 42
Title: Fight Fire with Fire: How Much Can We Trust ChatGPT on Source Code-Related Tasks?
ID: 43
Title: Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation
ID: 44
Title: Multi-Agent Software Development through Cross-Team Collaboration
ID: 45
Title: MASAI: Modular Architecture for Software-engineering AI Agents
ID: 46
Title: AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology
ID: 47
Title: CodeNav: Beyond tool-use to using real-world codebases with LLM agents
ID: 48
Title: INDICT: Code Generation with Internal Dialogues of Critiques for Both Security and Helpfulness
ID: 49
Title: AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents
ID: 50
Title: Interactive Program Synthesis
ID: 51
Title: Interactive Code Generation via Test-Driven User-Intent Formalization
ID: 52
Title: Improving Code Generation by Training with Natural Language Feedback
ID: 53
Title: Self-Refine: Iterative Refinement with Self-Feedback
ID: 54
Title: Teaching Large Language Models to Self-Debug
ID: 55
Title: Self-Edit: Fault-Aware Code Editor for Code Generation
ID: 56
Title: LeTI: Learning to Generate from Textual Interactions
ID: 57
Title: Is Self-Repair a Silver Bullet for Code Generation?
ID: 58
Title: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback
ID: 59
Title: OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement
ID: 60
Title: Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback
ID: 61
Title: CYCLE: Learning to Self-Refine the Code Generation
ID: 62
Title: LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation
ID: 63
Title: SOAP: Enhancing Efficiency of Generated Code via Self-Optimization
ID: 64
Title: Code Repair with LLMs gives an Exploration-Exploitation Tradeoff
ID: 65
Title: ReflectionCoder: Learning from Reflection Sequence for Enhanced One-off Code Generation
ID: 66
Title: Training LLMs to Better Self-Debug and Explain Code
ID: 67
Title: Requirements are All You Need: From Requirements to Code with LLMs
ID: 68
Title: I Need Help! Evaluating LLM's Ability to Ask for Users' Support: A Case Study on Text-to-SQL Generation
之前所有批次的临时目录：