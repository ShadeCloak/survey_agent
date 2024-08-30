
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
,以下是第9批次的论文ID，题目,和摘要：ID: 49
Title: AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents
Abstract: Autonomous agents that address day-to-day digital tasks (e.g., ordering
groceries for a household), must not only operate multiple apps (e.g., notes,
messaging, shopping app) via APIs, but also generate rich code with complex
control flow in an iterative manner based on their interaction with the
environment. However, existing benchmarks for tool use are inadequate, as they
only cover tasks that require a simple sequence of API calls.
  To remedy this gap, we built $\textbf{AppWorld Engine}$, a high-quality
execution environment (60K lines of code) of 9 day-to-day apps operable via 457
APIs and populated with realistic digital activities simulating the lives of
~100 fictitious users. We then created $\textbf{AppWorld Benchmark}$ (40K lines
of code), a suite of 750 natural, diverse, and challenging autonomous agent
tasks requiring rich and interactive code generation. It supports robust
programmatic evaluation with state-based unit tests, allowing for different
ways of completing a task while also checking for unexpected changes, i.e.,
collateral damage. The state-of-the-art LLM, GPT-4o, solves only ~49% of our
'normal' tasks and ~30% of 'challenge' tasks, while other models solve at least
16% fewer. This highlights the benchmark's difficulty and AppWorld's potential
to push the frontiers of interactive coding agents. The project website is
available at https://appworld.dev/.
URL: https://arxiv.org/abs/2407.18901

ID: 50
Title: Interactive Program Synthesis
Abstract: Program synthesis from incomplete specifications (e.g. input-output examples)
has gained popularity and found real-world applications, primarily due to its
ease-of-use. Since this technology is often used in an interactive setting,
efficiency and correctness are often the key user expectations from a system
based on such technologies. Ensuring efficiency is challenging since the highly
combinatorial nature of program synthesis algorithms does not fit in a 1-2
second response expectation of a user-facing system. Meeting correctness
expectations is also difficult, given that the specifications provided are
incomplete, and that the users of such systems are typically non-programmers.
  In this paper, we describe how interactivity can be leveraged to develop
efficient synthesis algorithms, as well as to decrease the cognitive burden
that a user endures trying to ensure that the system produces the desired
program. We build a formal model of user interaction along three dimensions:
incremental algorithm, step-based problem formulation, and feedback-based
intent refinement. We then illustrate the effectiveness of each of these forms
of interactivity with respect to synthesis performance and correctness on a set
of real-world case studies.
URL: https://arxiv.org/abs/1703.03539

ID: 51
Title: Interactive Code Generation via Test-Driven User-Intent Formalization
Abstract: Large language models (LLMs) have shown great potential in automating
significant aspects of coding by producing natural code from informal natural
language (NL) intent. However, when interacting with LLMs, users have no
guarantees that the code suggestions produced correctly satisfy the intent they
provided. In fact, it is hard to define a notion of correctness since natural
language can be ambiguous and lacks a formal semantics.
  In this paper, we propose the workflow of {\it interactive test-driven code
generation}, which leverages lightweight user feedback to (a) formalize the
user intent using generated tests that can be useful for debugging, and (b)
produce an improved set of code suggestions by pruning and ranking candidate
code suggestions. We describe a language-agnostic abstract algorithm and a
concrete implementation TiCoder. We perform an automated evaluation of TiCoder
on the \emph{MBPP} and \emph{HumanEval} code generation benchmarks. Our results
are promising with using the OpenAI Codex LLM: our best algorithm improves the
\passk{1} code generation accuracy (in absolute percentages) between $22.49\%$
to $37.71\%$ for MBPP and between $24.79\%$ to $53.98\%$ for HumanEval using
between 1 to 5 simulated user queries.
URL: https://arxiv.org/abs/2208.05950

ID: 52
Title: Improving Code Generation by Training with Natural Language Feedback
Abstract: The potential for pre-trained large language models (LLMs) to use natural
language feedback at inference time has been an exciting recent development. We
build upon this observation by formalizing an algorithm for learning from
natural language feedback at training time instead, which we call Imitation
learning from Language Feedback (ILF). ILF requires only a small amount of
human-written feedback during training and does not require the same feedback
at test time, making it both user-friendly and sample-efficient. We further
show that ILF can be seen as a form of minimizing the KL divergence to the
ground truth distribution and demonstrate a proof-of-concept on a neural
program synthesis task. We use ILF to improve a Codegen-Mono 6.1B model's
pass@1 rate by 38% relative (and 10% absolute) on the Mostly Basic Python
Problems (MBPP) benchmark, outperforming both fine-tuning on MBPP and
fine-tuning on repaired programs written by humans. Overall, our results
suggest that learning from human-written natural language feedback is both more
effective and sample-efficient than training exclusively on demonstrations for
improving an LLM's performance on code generation tasks.
URL: https://arxiv.org/abs/2303.16749

ID: 53
Title: Self-Refine: Iterative Refinement with Self-Feedback
Abstract: Like humans, large language models (LLMs) do not always generate the best
output on their first try. Motivated by how humans refine their written text,
we introduce Self-Refine, an approach for improving initial outputs from LLMs
through iterative feedback and refinement. The main idea is to generate an
initial output using an LLMs; then, the same LLMs provides feedback for its
output and uses it to refine itself, iteratively. Self-Refine does not require
any supervised training data, additional training, or reinforcement learning,
and instead uses a single LLM as the generator, refiner, and feedback provider.
We evaluate Self-Refine across 7 diverse tasks, ranging from dialog response
generation to mathematical reasoning, using state-of-the-art (GPT-3.5, ChatGPT,
and GPT-4) LLMs. Across all evaluated tasks, outputs generated with Self-Refine
are preferred by humans and automatic metrics over those generated with the
same LLM using conventional one-step generation, improving by ~20% absolute on
average in task performance. Our work demonstrates that even state-of-the-art
LLMs like GPT-4 can be further improved at test time using our simple,
standalone approach.
URL: https://arxiv.org/abs/2303.17651

ID: 54
Title: Teaching Large Language Models to Self-Debug
Abstract: Large language models (LLMs) have achieved impressive performance on code
generation. However, for complex programming tasks, generating the correct
solution in one go becomes challenging, thus some prior works have designed
program repair approaches to improve code generation performance. In this work,
we propose Self-Debugging, which teaches a large language model to debug its
predicted program via few-shot demonstrations. In particular, we demonstrate
that Self-Debugging can teach the large language model to perform rubber duck
debugging; i.e., without any human feedback on the code correctness or error
messages, the model is able to identify its mistakes by investigating the
execution results and explaining the generated code in natural language.
Self-Debugging achieves the state-of-the-art performance on several code
generation benchmarks, including the Spider dataset for text-to-SQL generation,
TransCoder for C++-to-Python translation, and MBPP for text-to-Python
generation. On the Spider benchmark where there are no unit tests to verify the
correctness of predictions, Self-Debugging with code explanation consistently
improves the baseline by 2-3%, and improves the prediction accuracy on problems
of the hardest level by 9%. On TransCoder and MBPP where unit tests are
available, Self-Debugging improves the baseline accuracy by up to 12%.
Meanwhile, by leveraging feedback messages and reusing failed predictions,
Self-Debugging notably improves sample efficiency, and can match or outperform
baseline models that generate more than 10x candidate programs.
URL: https://arxiv.org/abs/2304.05128

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