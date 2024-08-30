
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
,以下是第4批次的论文ID，题目,和摘要：ID: 19
Title: PyBench: Evaluating LLM Agent on various real-world coding tasks
Abstract: The LLM Agent, equipped with a code interpreter, is capable of automatically
solving real-world coding tasks, such as data analysis and image editing.
  However, existing benchmarks primarily focus on either simplistic tasks, such
as completing a few lines of code, or on extremely complex and specific tasks
at the repository level, neither of which are representative of various daily
coding tasks.
  To address this gap, we introduce \textbf{PyBench}, a benchmark encompassing
five main categories of real-world tasks, covering more than 10 types of files.
Given a high-level user query and related files, the LLM Agent needs to reason
and execute Python code via a code interpreter for a few turns before making a
formal response to fulfill the user's requirements. Successfully addressing
tasks in PyBench demands a robust understanding of various Python packages,
superior reasoning capabilities, and the ability to incorporate feedback from
executed code. Our evaluations indicate that current open-source LLMs are
struggling with these tasks. Hence, we conduct analysis and experiments on four
kinds of datasets proving that comprehensive abilities are needed for PyBench.
Our fine-tuned 8B size model: \textbf{PyLlama3} achieves an exciting
performance on PyBench which surpasses many 33B and 70B size models. Our
Benchmark, Training Dataset, and Model are available at:
{https://github.com/Mercury7353/PyBench}
URL: https://arxiv.org/abs/2407.16732

ID: 20
Title: AdaCoder: Adaptive Prompt Compression for Programmatic Visual Question Answering
Abstract: Visual question answering aims to provide responses to natural language
questions given visual input. Recently, visual programmatic models (VPMs),
which generate executable programs to answer questions through large language
models (LLMs), have attracted research interest. However, they often require
long input prompts to provide the LLM with sufficient API usage details to
generate relevant code. To address this limitation, we propose AdaCoder, an
adaptive prompt compression framework for VPMs. AdaCoder operates in two
phases: a compression phase and an inference phase. In the compression phase,
given a preprompt that describes all API definitions in the Python language
with example snippets of code, a set of compressed preprompts is generated,
each depending on a specific question type. In the inference phase, given an
input question, AdaCoder predicts the question type and chooses the appropriate
corresponding compressed preprompt to generate code to answer the question.
Notably, AdaCoder employs a single frozen LLM and pre-defined prompts, negating
the necessity of additional training and maintaining adaptability across
different powerful black-box LLMs such as GPT and Claude. In experiments, we
apply AdaCoder to ViperGPT and demonstrate that it reduces token length by
71.1%, while maintaining or even improving the performance of visual question
answering.
URL: https://arxiv.org/abs/2407.19410

ID: 21
Title: Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering
Abstract: Visual question answering (VQA) is the task of providing accurate answers to
natural language questions based on visual input. Programmatic VQA (PVQA)
models have been gaining attention recently. These use large language models
(LLMs) to formulate executable programs that address questions requiring
complex visual reasoning. However, there are challenges in enabling LLMs to
comprehend the usage of image processing modules and generate relevant code. To
overcome these challenges, this paper introduces PyramidCoder, a novel
prompting framework for PVQA models. PyramidCoder consists of three
hierarchical levels, each serving a distinct purpose: query rephrasing, code
generation, and answer aggregation. Notably, PyramidCoder utilizes a single
frozen LLM and pre-defined prompts at each level, eliminating the need for
additional training and ensuring flexibility across various LLM architectures.
Compared to the state-of-the-art PVQA model, our approach improves accuracy by
at least 0.5% on the GQA dataset, 1.4% on the VQAv2 dataset, and 2.9% on the
NLVR2 dataset.
URL: https://arxiv.org/abs/2407.20563

ID: 22
Title: Code Simulation Challenges for Large Language Models
Abstract: Many reasoning, planning, and problem-solving tasks share an intrinsic
algorithmic nature: correctly simulating each step is a sufficient condition to
solve them correctly. This work studies to what extent Large Language Models
(LLMs) can simulate coding and algorithmic tasks to provide insights into
general capabilities in such algorithmic reasoning tasks. We introduce
benchmarks for straight-line programs, code that contains critical paths, and
approximate and redundant instructions. We further assess the simulation
capabilities of LLMs with sorting algorithms and nested loops and show that a
routine's computational complexity directly affects an LLM's ability to
simulate its execution. While the most powerful LLMs exhibit relatively strong
simulation capabilities, the process is fragile, seems to rely heavily on
pattern recognition, and is affected by memorisation. We propose a novel
off-the-shelf prompting method, Chain of Simulation (CoSm), which instructs
LLMs to simulate code execution line by line/follow the computation pattern of
compilers. CoSm efficiently helps LLMs reduce memorisation and shallow pattern
recognition while improving simulation performance. We consider the success of
CoSm in code simulation to be inspirational for other general routine
simulation reasoning tasks.
URL: https://arxiv.org/abs/2401.09074

ID: 23
Title: CodeMind: A Framework to Challenge Large Language Models for Code Reasoning
Abstract: Solely relying on test passing to evaluate Large Language Models (LLMs) for
code synthesis may result in unfair assessment or promoting models with data
leakage. As an alternative, we introduce CodeMind, a framework designed to
gauge the code reasoning abilities of LLMs. CodeMind currently supports three
code reasoning tasks: Independent Execution Reasoning (IER), Dependent
Execution Reasoning (DER), and Specification Reasoning (SR). The first two
evaluate models to predict the execution output of an arbitrary code or code
the model could correctly synthesize. The third one evaluates the extent to
which LLMs implement the specified expected behavior.
  Our extensive evaluation of nine LLMs across five benchmarks in two different
programming languages using CodeMind shows that LLMs fairly follow control flow
constructs and, in general, explain how inputs evolve to output, specifically
for simple programs and the ones they can correctly synthesize. However, their
performance drops for code with higher complexity, non-trivial logical and
arithmetic operators, non-primitive types, and API calls. Furthermore, we
observe that, while correlated, specification reasoning (essential for code
synthesis) does not imply execution reasoning (essential for broader
programming tasks such as testing and debugging): ranking LLMs based on test
passing can be different compared to code reasoning.
URL: https://arxiv.org/abs/2402.09664

ID: 24
Title: Executing Natural Language-Described Algorithms with Large Language Models: An Investigation
Abstract: Executing computer programs described in natural language has long been a
pursuit of computer science. With the advent of enhanced natural language
understanding capabilities exhibited by large language models (LLMs), the path
toward this goal has been illuminated. In this paper, we seek to examine the
capacity of present-day LLMs to comprehend and execute algorithms outlined in
natural language. We established an algorithm test set sourced from
Introduction to Algorithm, a well-known textbook that contains many
representative widely-used algorithms. To systematically assess LLMs' code
execution abilities, we selected 30 algorithms, generated 300 random-sampled
instances in total, and evaluated whether popular LLMs can understand and
execute these algorithms. Our findings reveal that LLMs, notably GPT-4, can
effectively execute programs described in natural language, as long as no heavy
numeric computation is involved. We believe our findings contribute to
evaluating LLMs' code execution abilities and would encourage further
investigation and application for the computation power of LLMs.
URL: https://arxiv.org/abs/2403.00795

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
,以下是第4批次的论文ID，题目,和一句话描述：ID: 31
Title: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
Sentence: MetaGPT enhances LLM-based multi-agent systems for complex tasks via meta-programming and SOPs for streamlined, human-like collaboration.

ID: 32
Title: CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules
Sentence: CodeChain improves computational code generation by iteratively generating and reusing modular code submodules.

ID: 33
Title: CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges
Sentence: CodeAgent: A novel LLM-based agent system that enhances code generation performance by integrating external tools for real-world repo-level coding challenges, outperforming existing solutions.

ID: 34
Title: CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing
Sentence: CoCoST improves complex code generation via online searching, correctness testing, input/output serialization, and test case generation, significantly enhancing LLM practicality.

ID: 35
Title: When LLM-based Code Generation Meets the Software Development Process
Sentence: This study proposes the LCG framework that employs multiple LLM agents to emulate various software process models, improving code quality and consistency compared to baseline, with LCGScrum achieving the best performance.

ID: 36
Title: RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
Sentence: RepairAgent uses an autonomous LLM-based agent to autonomously repair bugs with tools, demonstrating effectiveness in fixing bugs not addressed by prior techniques.

ID: 37
Title: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution
Sentence: MAGIS is an LLM-based framework that leverages multi-agent collaboration to resolve GitHub issues, outperforming single-agent LLMs with an eight-fold increase in resolution rate.

ID: 38
Title: Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization
Sentence: "Self-Organized Agents: A Multi-Agent Framework for Large-Scale Code Generation and Optimization using LLMs."

ID: 39
Title: AutoCodeRover: Autonomous Program Improvement
Sentence: AutoCodeRover automatically improves software by combining LLMs and advanced code search, enhancing bug fixing and feature addition with low cost.

ID: 40
Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
Sentence: SWE-agent: Custom agent-computer interface boosts LM agents in automated software engineering tasks, exceeds previous performance.

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