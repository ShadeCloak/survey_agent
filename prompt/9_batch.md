
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
,以下是第10批次的论文ID，题目,和摘要：ID: 55
Title: Self-Edit: Fault-Aware Code Editor for Code Generation
Abstract: Large language models (LLMs) have demonstrated an impressive ability to
generate codes on competitive programming tasks. However, with limited sample
numbers, LLMs still suffer from poor accuracy. Inspired by the process of human
programming, we propose a generate-and-edit approach named Self-Edit that
utilizes execution results of the generated code from LLMs to improve the code
quality on the competitive programming task. We execute the generated code on
the example test case provided in the question and wrap execution results into
a supplementary comment. Utilizing this comment as guidance, our fault-aware
code editor is employed to correct errors in the generated code. We perform
extensive evaluations across two competitive programming datasets with nine
different LLMs. Compared to directly generating from LLMs, our approach can
improve the average of pass@1 by 89\% on APPS-dev, 31\% on APPS-test, and 48\%
on HumanEval over nine popular code generation LLMs with parameter sizes
ranging from 110M to 175B. Compared to other post-processing methods, our
method demonstrates superior accuracy and efficiency.
URL: https://arxiv.org/abs/2305.04087

ID: 56
Title: LeTI: Learning to Generate from Textual Interactions
Abstract: Fine-tuning pre-trained language models (LMs) is essential for enhancing
their capabilities. Existing techniques commonly fine-tune on input-output
pairs (e.g., instruction tuning) or with numerical rewards that gauge the
output quality (e.g., RLHF). We explore LMs' potential to learn from textual
interactions (LETI) that not only check their correctness with binary labels
but also pinpoint and explain errors in their outputs through textual feedback.
Our focus is the code generation task, where the model produces code based on
natural language instructions. This setting invites a natural and scalable way
to acquire textual feedback: the error messages and stack traces from code
execution using a Python interpreter. LETI iteratively fine-tunes the model,
using the LM objective, on a concatenation of natural language instructions,
LM-generated programs, and textual feedback. Prepended to this fine-tuning
text, a binary reward token is used to differentiate correct and buggy
solutions. LETI requires no ground-truth outputs for training and even
outperforms a fine-tuned baseline that does. LETI not only improves the
performance of LMs on a code generation dataset MBPP, but also generalizes to
other datasets. Trained on MBPP, it achieves comparable or better performance
than the base LMs on unseen problems in HumanEval. Furthermore, compared to
binary feedback, we observe that textual feedback leads to improved generation
quality and sample efficiency, achieving the same performance with fewer than
half of the gradient steps. LETI is equally applicable in natural language
tasks when they can be formulated as code generation, which we empirically
verified on event argument extraction.
URL: https://arxiv.org/abs/2305.10314

ID: 57
Title: Is Self-Repair a Silver Bullet for Code Generation?
Abstract: Large language models have shown remarkable aptitude in code generation, but
still struggle to perform complex tasks. Self-repair -- in which the model
debugs and repairs its own code -- has recently become a popular way to boost
performance in these settings. However, despite its increasing popularity,
existing studies of self-repair have been limited in scope; in many settings,
its efficacy thus remains poorly understood. In this paper, we analyze Code
Llama, GPT-3.5 and GPT-4's ability to perform self-repair on problems taken
from HumanEval and APPS. We find that when the cost of carrying out repair is
taken into account, performance gains are often modest, vary a lot between
subsets of the data, and are sometimes not present at all. We hypothesize that
this is because self-repair is bottlenecked by the model's ability to provide
feedback on its own code; using a stronger model to artificially boost the
quality of the feedback, we observe substantially larger performance gains.
Similarly, a small-scale study in which we provide GPT-4 with feedback from
human participants suggests that even for the strongest models, self-repair
still lags far behind what can be achieved with human-level debugging.
URL: https://arxiv.org/abs/2306.09896

ID: 58
Title: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback
Abstract: Humans write code in a fundamentally interactive manner and rely on constant
execution feedback to correct errors, resolve ambiguities, and decompose tasks.
While LLMs have recently exhibited promising coding capabilities, current
coding benchmarks mostly consider a static instruction-to-code sequence
transduction process, which has the potential for error propagation and a
disconnect between the generated code and its final execution environment. To
address this gap, we introduce InterCode, a lightweight, flexible, and
easy-to-use framework of interactive coding as a standard reinforcement
learning (RL) environment, with code as actions and execution feedback as
observations. Our framework is language and platform agnostic, uses
self-contained Docker environments to provide safe and reproducible execution,
and is compatible out-of-the-box with traditional seq2seq coding methods, while
enabling the development of new methods for interactive code generation. We use
InterCode to create three interactive code environments with Bash, SQL, and
Python as action spaces, leveraging data from the static NL2Bash, Spider, and
MBPP datasets. We demonstrate InterCode's viability as a testbed by evaluating
multiple state-of-the-art LLMs configured with different prompting strategies
such as ReAct and Plan & Solve. Our results showcase the benefits of
interactive code generation and demonstrate that InterCode can serve as a
challenging benchmark for advancing code understanding and generation
capabilities. InterCode is designed to be easily extensible and can even be
used to create new tasks such as Capture the Flag, a popular coding puzzle that
is inherently multi-step and involves multiple programming languages. Project
site with code and data: https://intercode-benchmark.github.io
URL: https://arxiv.org/abs/2306.14898

ID: 59
Title: OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement
Abstract: The introduction of large language models has significantly advanced code
generation. However, open-source models often lack the execution capabilities
and iterative refinement of advanced systems like the GPT-4 Code Interpreter.
To address this, we introduce OpenCodeInterpreter, a family of open-source code
systems designed for generating, executing, and iteratively refining code.
Supported by Code-Feedback, a dataset featuring 68K multi-turn interactions,
OpenCodeInterpreter integrates execution and human feedback for dynamic code
refinement. Our comprehensive evaluation of OpenCodeInterpreter across key
benchmarks such as HumanEval, MBPP, and their enhanced versions from EvalPlus
reveals its exceptional performance. Notably, OpenCodeInterpreter-33B achieves
an accuracy of 83.2 (76.4) on the average (and plus versions) of HumanEval and
MBPP, closely rivaling GPT-4's 84.2 (76.2) and further elevates to 91.6 (84.6)
with synthesized human feedback from GPT-4. OpenCodeInterpreter brings the gap
between open-source code generation models and proprietary systems like GPT-4
Code Interpreter.
URL: https://arxiv.org/abs/2402.14658

ID: 60
Title: Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback
Abstract: Large Language Models (LLMs) have shown remarkable progress in automated code
generation. Yet, LLM-generated code may contain errors in API usage, class,
data structure, or missing project-specific information. As much of this
project-specific context cannot fit into the prompts of LLMs, we must find ways
to allow the model to explore the project-level code context. We present
CoCoGen, a new code generation approach that uses compiler feedback to improve
the LLM-generated code. CoCoGen first leverages static analysis to identify
mismatches between the generated code and the project's context. It then
iteratively aligns and fixes the identified errors using information extracted
from the code repository. We integrate CoCoGen with two representative LLMs,
i.e., GPT-3.5-Turbo and Code Llama (13B), and apply it to Python code
generation. Experimental results show that CoCoGen significantly improves the
vanilla LLMs by over 80% in generating code dependent on the project context
and consistently outperforms the existing retrieval-based code generation
baselines.
URL: https://arxiv.org/abs/2403.16792

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