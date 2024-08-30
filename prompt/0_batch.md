
你是一个写综述的科研人员，你需要仔细理解所提供的很多篇特定主题的论文摘要,
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
,以下是第1批次的论文ID，题目,和摘要：ID: 1
Title: PAL: Program-aided Language Models
Abstract: Large language models (LLMs) have recently demonstrated an impressive ability
to perform arithmetic and symbolic reasoning tasks, when provided with a few
examples at test time ("few-shot prompting"). Much of this success can be
attributed to prompting methods such as "chain-of-thought'', which employ LLMs
for both understanding the problem description by decomposing it into steps, as
well as solving each step of the problem. While LLMs seem to be adept at this
sort of step-by-step decomposition, LLMs often make logical and arithmetic
mistakes in the solution part, even when the problem is decomposed correctly.
In this paper, we present Program-Aided Language models (PAL): a novel approach
that uses the LLM to read natural language problems and generate programs as
the intermediate reasoning steps, but offloads the solution step to a runtime
such as a Python interpreter. With PAL, decomposing the natural language
problem into runnable steps remains the only learning task for the LLM, while
solving is delegated to the interpreter. We demonstrate this synergy between a
neural LLM and a symbolic interpreter across 13 mathematical, symbolic, and
algorithmic reasoning tasks from BIG-Bench Hard and other benchmarks. In all
these natural language reasoning tasks, generating code using an LLM and
reasoning using a Python interpreter leads to more accurate results than much
larger models. For example, PAL using Codex achieves state-of-the-art few-shot
accuracy on the GSM8K benchmark of math word problems, surpassing PaLM-540B
which uses chain-of-thought by absolute 15% top-1. Our code and data are
publicly available at http://reasonwithpal.com/ .
URL: https://arxiv.org/abs/2211.10435

ID: 2
Title: Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks
Abstract: Recently, there has been significant progress in teaching language models to
perform step-by-step reasoning to solve complex numerical reasoning tasks.
Chain-of-thoughts prompting (CoT) is by far the state-of-art method for these
tasks. CoT uses language models to perform both reasoning and computation in
the multi-step `thought' process. To disentangle computation from reasoning, we
propose `Program of Thoughts' (PoT), which uses language models (mainly Codex)
to express the reasoning process as a program. The computation is relegated to
an external computer, which executes the generated programs to derive the
answer. We evaluate PoT on five math word problem datasets (GSM, AQuA, SVAMP,
TabMWP, MultiArith) and three financial-QA datasets (FinQA, ConvFinQA, TATQA)
for both few-shot and zero-shot setups. Under both few-shot and zero-shot
settings, PoT can show an average performance gain over CoT by around 12\%
across all the evaluated datasets. By combining PoT with self-consistency
decoding, we can achieve SoTA performance on all math problem datasets and
near-SoTA performance on financial datasets. All of our data and code are
released in Github https://github.com/wenhuchen/Program-of-Thoughts
URL: https://arxiv.org/abs/2211.12588

ID: 3
Title: Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification
Abstract: Recent progress in large language models (LLMs) like GPT-4 and PaLM-2 has
brought significant advancements in addressing math reasoning problems. In
particular, OpenAI's latest version of GPT-4, known as GPT-4 Code Interpreter,
shows remarkable performance on challenging math datasets. In this paper, we
explore the effect of code on enhancing LLMs' reasoning capability by
introducing different constraints on the \textit{Code Usage Frequency} of GPT-4
Code Interpreter. We found that its success can be largely attributed to its
powerful skills in generating and executing code, evaluating the output of code
execution, and rectifying its solution when receiving unreasonable outputs.
Based on this insight, we propose a novel and effective prompting method,
explicit \uline{c}ode-based \uline{s}elf-\uline{v}erification~(CSV), to further
boost the mathematical reasoning potential of GPT-4 Code Interpreter. This
method employs a zero-shot prompt on GPT-4 Code Interpreter to encourage it to
use code to self-verify its answers. In instances where the verification state
registers as ``False'', the model shall automatically amend its solution,
analogous to our approach of rectifying errors during a mathematics
examination. Furthermore, we recognize that the states of the verification
result indicate the confidence of a solution, which can improve the
effectiveness of majority voting. With GPT-4 Code Interpreter and CSV, we
achieve an impressive zero-shot accuracy on MATH dataset \textbf{(53.9\% $\to$
84.3\%)}.
URL: https://arxiv.org/abs/2308.07921

ID: 4
Title: MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning
Abstract: The recently released GPT-4 Code Interpreter has demonstrated remarkable
proficiency in solving challenging math problems, primarily attributed to its
ability to seamlessly reason with natural language, generate code, execute
code, and continue reasoning based on the execution output. In this paper, we
present a method to fine-tune open-source language models, enabling them to use
code for modeling and deriving math equations and, consequently, enhancing
their mathematical reasoning abilities. We propose a method of generating novel
and high-quality datasets with math problems and their code-based solutions,
referred to as MathCodeInstruct. Each solution interleaves natural language,
code, and execution results. We also introduce a customized supervised
fine-tuning and inference approach. This approach yields the MathCoder models,
a family of models capable of generating code-based solutions for solving
challenging math problems. Impressively, the MathCoder models achieve
state-of-the-art scores among open-source LLMs on the MATH (45.2%) and GSM8K
(83.9%) datasets, substantially outperforming other open-source alternatives.
Notably, the MathCoder model not only surpasses ChatGPT-3.5 and PaLM-2 on GSM8K
and MATH but also outperforms GPT-4 on the competition-level MATH dataset. The
dataset and models will be released at https://github.com/mathllm/MathCoder.
URL: https://arxiv.org/abs/2310.03731

ID: 5
Title: Chain of Code: Reasoning with a Language Model-Augmented Code Emulator
Abstract: Code provides a general syntactic structure to build complex programs and
perform precise computations when paired with a code interpreter - we
hypothesize that language models (LMs) can leverage code-writing to improve
Chain of Thought reasoning not only for logic and arithmetic tasks, but also
for semantic ones (and in particular, those that are a mix of both). For
example, consider prompting an LM to write code that counts the number of times
it detects sarcasm in an essay: the LM may struggle to write an implementation
for "detect_sarcasm(string)" that can be executed by the interpreter (handling
the edge cases would be insurmountable). However, LMs may still produce a valid
solution if they not only write code, but also selectively "emulate" the
interpreter by generating the expected output of "detect_sarcasm(string)". In
this work, we propose Chain of Code (CoC), a simple yet surprisingly effective
extension that improves LM code-driven reasoning. The key idea is to encourage
LMs to format semantic sub-tasks in a program as flexible pseudocode that the
interpreter can explicitly catch undefined behaviors and hand off to simulate
with an LM (as an "LMulator"). Experiments demonstrate that Chain of Code
outperforms Chain of Thought and other baselines across a variety of
benchmarks; on BIG-Bench Hard, Chain of Code achieves 84%, a gain of 12% over
Chain of Thought. In a nutshell, CoC broadens the scope of reasoning questions
that LMs can answer by "thinking in code".
URL: https://arxiv.org/abs/2312.04474

ID: 6
Title: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
Abstract: While large language models (LLMs) are increasingly being used for program
synthesis, they lack the global view needed to develop useful abstractions;
they generally predict programs one at a time, often repeating the same
functionality. Generating redundant code from scratch is both inefficient and
error-prone. To address this, we propose Refactoring for Generalizable
Abstraction Learning (ReGAL), a gradient-free method for learning a library of
reusable functions via code refactorization, i.e., restructuring code without
changing its execution output. ReGAL learns from a small set of existing
programs, iteratively verifying and refining its abstractions via execution. We
find that the shared function libraries discovered by ReGAL make programs
easier to predict across diverse domains. On five datasets -- LOGO graphics
generation, Date reasoning, TextCraft (a Minecraft-based text-game) MATH, and
TabMWP -- both open-source and proprietary LLMs improve in accuracy when
predicting programs with ReGAL functions. For CodeLlama-13B, ReGAL results in
absolute accuracy increases of 11.5% on LOGO, 26.1% on date understanding, and
8.1% on TextCraft, outperforming GPT-3.5 in two of three domains. Our analysis
reveals ReGAL's abstractions encapsulate frequently-used subroutines as well as
environment dynamics.
URL: https://arxiv.org/abs/2401.16467

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
,以下是第1批次的论文ID，题目,和一句话描述：ID: 1
Title: PAL: Program-aided Language Models
Sentence: PAL leverizes neural LLMs to generate codes solving natural language problem into runnable steps, with accurate results beating larger models.

ID: 2
Title: Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks
Sentence: This study proposes `Program of Thoughts', which uses language models to separate computation from reasoning in numerical reasoning tasks, significantly improving performance over the conventional Chain-of-Thoughts method.

ID: 3
Title: Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification
Sentence: This study investigates GPT-4 Code Interpreter's use of code-based self-verification to enhance math problem-solving, achieving a 53.9% to 84.3% accuracy boost.

ID: 4
Title: MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning
Sentence: Fine-tuned Language models use code for solving math problems, achieving state-of-the-art results on benchmark datasets.

ID: 5
Title: Chain of Code: Reasoning with a Language Model-Augmented Code Emulator
Sentence: Chain of Code enhances language model reasoning by emulating code execution, improving task handling and achieving 12% gains.

ID: 6
Title: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
Sentence: ReGAL refactors code to discover reusable abstractions, enhancing LLMs' program synthesis across diverse domains.

ID: 7
Title: Executable Code Actions Elicit Better LLM Agents
Sentence: Executable CodeAct consolidates LLM actions into unified space, enhancing flexibility and performance.

ID: 8
Title: Exploring Hybrid Question Answering via Program-based Prompting
Sentence: This paper introduces HProPro, a novel program-based prompting framework for hybrid question answering that performs hybrid information-seeking without training specialized retrievers or modal transformations, significantly surpassing baseline systems in few-shot settings.

ID: 9
Title: Eliciting Better Multilingual Structured Reasoning from LLMs through Code
Sentence: This study introduces xSTREET, a multilingual reasoning dataset, and proposes training with code-augmented data and using code-based inference prompts to improve LLMs' non-English structured reasoning skills.

ID: 10
Title: FlowMind: Automatic Workflow Generation with LLMs
Sentence: FlowMind automates workflow generation by leveraging LLMs, enhancing RPA for unconventional tasks with hallucination mitigation and secure, user-facilitated processes.

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
