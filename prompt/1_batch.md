
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
,以下是第2批次的论文ID，题目,和摘要：ID: 7
Title: Executable Code Actions Elicit Better LLM Agents
Abstract: Large Language Model (LLM) agents, capable of performing a broad range of
actions, such as invoking tools and controlling robots, show great potential in
tackling real-world challenges. LLM agents are typically prompted to produce
actions by generating JSON or text in a pre-defined format, which is usually
limited by constrained action space (e.g., the scope of pre-defined tools) and
restricted flexibility (e.g., inability to compose multiple tools). This work
proposes to use executable Python code to consolidate LLM agents' actions into
a unified action space (CodeAct). Integrated with a Python interpreter, CodeAct
can execute code actions and dynamically revise prior actions or emit new
actions upon new observations through multi-turn interactions. Our extensive
analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that
CodeAct outperforms widely used alternatives (up to 20% higher success rate).
The encouraging performance of CodeAct motivates us to build an open-source LLM
agent that interacts with environments by executing interpretable code and
collaborates with users using natural language. To this end, we collect an
instruction-tuning dataset CodeActInstruct that consists of 7k multi-turn
interactions using CodeAct. We show that it can be used with existing data to
improve models in agent-oriented tasks without compromising their general
capability. CodeActAgent, finetuned from Llama2 and Mistral, is integrated with
Python interpreter and uniquely tailored to perform sophisticated tasks (e.g.,
model training) using existing libraries and autonomously self-debug.
URL: https://arxiv.org/abs/2402.01030

ID: 8
Title: Exploring Hybrid Question Answering via Program-based Prompting
Abstract: Question answering over heterogeneous data requires reasoning over diverse
sources of data, which is challenging due to the large scale of information and
organic coupling of heterogeneous data. Various approaches have been proposed
to address these challenges. One approach involves training specialized
retrievers to select relevant information, thereby reducing the input length.
Another approach is to transform diverse modalities of data into a single
modality, simplifying the task difficulty and enabling more straightforward
processing. In this paper, we propose HProPro, a novel program-based prompting
framework for the hybrid question answering task. HProPro follows the code
generation and execution paradigm. In addition, HProPro integrates various
functions to tackle the hybrid reasoning scenario. Specifically, HProPro
contains function declaration and function implementation to perform hybrid
information-seeking over data from various sources and modalities, which
enables reasoning over such data without training specialized retrievers or
performing modal transformations. Experimental results on two typical hybrid
question answering benchmarks HybridQA and MultiModalQA demonstrate the
effectiveness of HProPro: it surpasses all baseline systems and achieves the
best performances in the few-shot settings on both datasets.
URL: https://arxiv.org/abs/2402.10812

ID: 9
Title: Eliciting Better Multilingual Structured Reasoning from LLMs through Code
Abstract: The development of large language models (LLM) has shown progress on
reasoning, though studies have largely considered either English or simple
reasoning tasks. To address this, we introduce a multilingual structured
reasoning and explanation dataset, termed xSTREET, that covers four tasks
across six languages. xSTREET exposes a gap in base LLM performance between
English and non-English reasoning tasks.
  We then propose two methods to remedy this gap, building on the insight that
LLMs trained on code are better reasoners. First, at training time, we augment
a code dataset with multilingual comments using machine translation while
keeping program code as-is. Second, at inference time, we bridge the gap
between training and inference by employing a prompt structure that
incorporates step-by-step code primitives to derive new facts and find a
solution. Our methods show improved multilingual performance on xSTREET, most
notably on the scientific commonsense reasoning subtask. Furthermore, the
models show no regression on non-reasoning tasks, thus demonstrating our
techniques maintain general-purpose abilities.
URL: https://arxiv.org/abs/2403.02567

ID: 10
Title: FlowMind: Automatic Workflow Generation with LLMs
Abstract: The rapidly evolving field of Robotic Process Automation (RPA) has made
significant strides in automating repetitive processes, yet its effectiveness
diminishes in scenarios requiring spontaneous or unpredictable tasks demanded
by users. This paper introduces a novel approach, FlowMind, leveraging the
capabilities of Large Language Models (LLMs) such as Generative Pretrained
Transformer (GPT), to address this limitation and create an automatic workflow
generation system. In FlowMind, we propose a generic prompt recipe for a
lecture that helps ground LLM reasoning with reliable Application Programming
Interfaces (APIs). With this, FlowMind not only mitigates the common issue of
hallucinations in LLMs, but also eliminates direct interaction between LLMs and
proprietary data or code, thus ensuring the integrity and confidentiality of
information - a cornerstone in financial services. FlowMind further simplifies
user interaction by presenting high-level descriptions of auto-generated
workflows, enabling users to inspect and provide feedback effectively. We also
introduce NCEN-QA, a new dataset in finance for benchmarking question-answering
tasks from N-CEN reports on funds. We used NCEN-QA to evaluate the performance
of workflows generated by FlowMind against baseline and ablation variants of
FlowMind. We demonstrate the success of FlowMind, the importance of each
component in the proposed lecture recipe, and the effectiveness of user
interaction and feedback in FlowMind.
URL: https://arxiv.org/abs/2404.13050

ID: 11
Title: Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models
Abstract: Algorithmic reasoning refers to the ability to understand the complex
patterns behind the problem and decompose them into a sequence of reasoning
steps towards the solution. Such nature of algorithmic reasoning makes it a
challenge for large language models (LLMs), even though they have demonstrated
promising performance in other reasoning tasks. Within this context, some
recent studies use programming languages (e.g., Python) to express the
necessary logic for solving a given instance/question (e.g.,
Program-of-Thought) as inspired by their strict and precise syntaxes. However,
it is non-trivial to write an executable code that expresses the correct logic
on the fly within a single inference call. Also, the code generated
specifically for an instance cannot be reused for others, even if they are from
the same task and might require identical logic to solve. This paper presents
Think-and-Execute, a novel framework that decomposes the reasoning process of
language models into two steps. (1) In Think, we discover a task-level logic
that is shared across all instances for solving a given task and then express
the logic with pseudocode; (2) In Execute, we further tailor the generated
pseudocode to each instance and simulate the execution of the code. With
extensive experiments on seven algorithmic reasoning tasks, we demonstrate the
effectiveness of Think-and-Execute. Our approach better improves LMs' reasoning
compared to several strong baselines performing instance-specific reasoning
(e.g., CoT and PoT), suggesting the helpfulness of discovering task-level
logic. Also, we show that compared to natural language, pseudocode can better
guide the reasoning of LMs, even though they are trained to follow natural
language instructions.
URL: https://arxiv.org/abs/2404.02575

ID: 12
Title: AIOS Compiler: LLM as Interpreter for Natural Language Programming and Flow Programming of AI Agents
Abstract: Since their inception, programming languages have trended towards greater
readability and lower barriers for programmers. Following this trend, natural
language can be a promising type of programming language that provides great
flexibility and usability and helps towards the democracy of programming.
However, the inherent vagueness, ambiguity, and verbosity of natural language
pose significant challenges in developing an interpreter that can accurately
understand the programming logic and execute instructions written in natural
language. Fortunately, recent advancements in Large Language Models (LLMs) have
demonstrated remarkable proficiency in interpreting complex natural language.
Inspired by this, we develop a novel system for Code Representation and
Execution (CoRE), which employs LLM as interpreter to interpret and execute
natural language instructions. The proposed system unifies natural language
programming, pseudo-code programming, and flow programming under the same
representation for constructing language agents, while LLM serves as the
interpreter to interpret and execute the agent programs. In this paper, we
begin with defining the programming syntax that structures natural language
instructions logically. During the execution, we incorporate external memory to
minimize redundancy. Furthermore, we equip the designed interpreter with the
capability to invoke external tools, compensating for the limitations of LLM in
specialized domains or when accessing real-time information. This work is
open-source at https://github.com/agiresearch/CoRE,
https://github.com/agiresearch/OpenAGI, and
https://github.com/agiresearch/AIOS.
URL: https://arxiv.org/abs/2405.06907

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
,以下是第2批次的论文ID，题目,和一句话描述：ID: 11
Title: Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models
Sentence: Language models enhance algorithmic reasoning by simulating pseudocode execution, improving task-level logic.

ID: 12
Title: AIOS Compiler: LLM as Interpreter for Natural Language Programming and Flow Programming of AI Agents
Sentence: AIOS Compiler uses LLM to interpret and execute natural language programming and flow programming, facilitating programming language evolution.

ID: 13
Title: MuMath-Code: Combining Tool-Use Large Language Models with Multi-perspective Data Augmentation for Mathematical Reasoning
Sentence: MuMath-Code combines tool-using LLMs with multi-perspective data augmentation, achieving state-of-the-art mathematical reasoning performance.

ID: 14
Title: Learning to Reason via Program Generation, Emulation, and Search
Sentence: This paper proposes CoGEX, a method that leverages language models to generate and emulate pseudo-programs for reasoning tasks beyond code-based tasks, improving performance on both algorithmic and soft reasoning tasks.

ID: 15
Title: Arithmetic Reasoning with LLM: Prolog Generation & Permutation
Sentence: We propose a method for instructing LLMs to solve arithmetic problems by generating Prolog code, which outperforms existing methods in the GSM8K benchmark and improves training robustness through data augmentation.

ID: 16
Title: Can LLMs Reason in the Wild with Programs?
Sentence: Large Language Models (LLMs) can reason unknown-type problems as they are trained on various formalisms to select tactics and write programs effectively for diverse open-ended reasoning tasks.


ID: 17
Title: DotaMath: Decomposition of Thought with Code Assistance and Self-correction for Mathematical Reasoning
Sentence: This paper proposes DotaMath, a series of LLMs that decompose complex mathematical problems using code and self-correction.

ID: 18
Title: CIBench: Evaluating Your LLMs with a Code Interpreter Plugin
Sentence: CIBench evaluates LLMs' capacity for data science tasks via a code interpreter plugin, employing an LLM-human cooperative approach.

ID: 19
Title: PyBench: Evaluating LLM Agent on various real-world coding tasks
Sentence: "PyBench assesses an LLM's Python coding capabilities across diverse real-world applications, highlighting limited open-source model proficiency and offering a superior, fine-tuned PyLlama3 model."



ID: 20
Title: AdaCoder: Adaptive Prompt Compression for Programmatic Visual Question Answering
Sentence: AdaCoder is an adaptive prompt compression framework that enhances visual programmatic models for question answering by generating efficient compressed prompts, without needing additional training for LLMs.

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