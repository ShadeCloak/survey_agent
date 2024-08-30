
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
,以下是第5批次的论文ID，题目,和摘要：ID: 25
Title: Can Language Models Pretend Solvers? Logic Code Simulation with LLMs
Abstract: Transformer-based large language models (LLMs) have demonstrated significant
potential in addressing logic problems. capitalizing on the great capabilities
of LLMs for code-related activities, several frameworks leveraging logical
solvers for logic reasoning have been proposed recently. While existing
research predominantly focuses on viewing LLMs as natural language logic
solvers or translators, their roles as logic code interpreters and executors
have received limited attention. This study delves into a novel aspect, namely
logic code simulation, which forces LLMs to emulate logical solvers in
predicting the results of logical programs. To further investigate this novel
task, we formulate our three research questions: Can LLMs efficiently simulate
the outputs of logic codes? What strength arises along with logic code
simulation? And what pitfalls? To address these inquiries, we curate three
novel datasets tailored for the logic code simulation task and undertake
thorough experiments to establish the baseline performance of LLMs in code
simulation. Subsequently, we introduce a pioneering LLM-based code simulation
technique, Dual Chains of Logic (DCoL). This technique advocates a dual-path
thinking approach for LLMs, which has demonstrated state-of-the-art performance
compared to other LLM prompt strategies, achieving a notable improvement in
accuracy by 7.06% with GPT-4-Turbo.
URL: https://arxiv.org/abs/2403.16097

ID: 26
Title: Reasoning Runtime Behavior of a Program with LLM: How Far Are We?
Abstract: Large language models for code (i.e., code LLMs) have shown strong code
understanding and generation capabilities. To evaluate the capabilities of code
LLMs in various aspects, many benchmarks have been proposed (e.g., HumanEval
and ClassEval). Code reasoning is one of the most essential abilities of code
LLMs, but existing benchmarks for code reasoning are not sufficient. Typically,
they focus on predicting the input and output of a program, ignoring the
evaluation of the intermediate behavior during program execution, as well as
the logical consistency (e.g., the model should not give the correct output if
the prediction of execution path is wrong) when performing the reasoning. To
address these problems, in this paper, we propose a framework, namely REval,
for evaluating code reasoning abilities and consistency of code LLMs with
program execution. We utilize existing code benchmarks and adapt them to new
benchmarks within our framework. A large-scale empirical study is conducted and
most LLMs show unsatisfactory performance on both Runtime Behavior Reasoning
(i.e., an average accuracy of 44.4%) and Incremental Consistency Evaluation
(i.e., an average IC score of 10.3). Evaluation results of current code LLMs
reflect the urgent need for the community to strengthen the code reasoning
capability of code LLMs. Our code, data, and \newname leaderboard are available
at https://r-eval.github.io.
URL: https://arxiv.org/abs/2403.16437

ID: 27
Title: NExT: Teaching Large Language Models to Reason about Code Execution
Abstract: A fundamental skill among human developers is the ability to understand and
reason about program execution. As an example, a programmer can mentally
simulate code execution in natural language to debug and repair code (aka.
rubber duck debugging). However, large language models (LLMs) of code are
typically trained on the surface textual form of programs, thus may lack a
semantic understanding of how programs execute at run-time. To address this
issue, we propose NExT, a method to teach LLMs to inspect the execution traces
of programs (variable states of executed lines) and reason about their run-time
behavior through chain-of-thought (CoT) rationales. Specifically, NExT uses
self-training to bootstrap a synthetic training set of execution-aware
rationales that lead to correct task solutions (e.g., fixed programs) without
laborious manual annotation. Experiments on program repair tasks based on MBPP
and HumanEval demonstrate that NExT improves the fix rate of a PaLM 2 model, by
26.1% and 14.3% absolute, respectively, with significantly improved rationale
quality as verified by automated metrics and human raters. Our model can also
generalize to scenarios where program traces are absent at test-time.
URL: https://arxiv.org/abs/2404.14662

ID: 28
Title: SelfPiCo: Self-Guided Partial Code Execution with LLMs
Abstract: Code executability plays a vital role in software debugging and testing
(e.g., detecting runtime exceptions or assertion violations). However, code
execution, especially partial or arbitrary code execution, is a non-trivial
task due to missing definitions and complex third-party dependencies. To make
partial code (such as code snippets posted on the web or code fragments deep
inside complex software projects) executable, the existing study has proposed a
machine learning model to predict the undefined element types and inject the
pre-defined dummy values into execution. However, the performance of their tool
is limited due to its simply designed dummy values and the inability to
continue learning. In this paper, we design and implement a novel framework,
named SelfPiCo (Self Guided Partial Code Executor), to dynamically guide
partial code execution by incorporating the open-source LLM (i.e., Code Llama)
within an interactive loop. Particularly, SelfPiCo leverages few-shot
in-context learning and chain-of-thought reasoning to elicit human knowledge
and logical reasoning based on fine-tuning the Code Llama model. SelfPiCo
continuously learns from code execution results and refines its predictions
step after step. Our evaluations demonstrate that SelfPiCo can execute 72.7%
and 83.3% of all lines in the open-source code and Stack Overflow snippets,
outperforming the most recent state-of-the-art Lexecutor by 37.9% and 33.5%,
respectively. Moreover, SelfPiCo successfully detected 18 and 33 runtime type
error issues by executing the partial code from eight GitHub software projects
and 43 Stack Overflow posts, demonstrating the practical usage and potential
application of our framework in practice.
URL: https://arxiv.org/abs/2407.16974

ID: 29
Title: Self-collaboration Code Generation via ChatGPT
Abstract: Although Large Language Models (LLMs) have demonstrated remarkable
code-generation ability, they still struggle with complex tasks. In real-world
software development, humans usually tackle complex tasks through collaborative
teamwork, a strategy that significantly controls development complexity and
enhances software quality. Inspired by this, we present a self-collaboration
framework for code generation employing LLMs, exemplified by ChatGPT.
Specifically, through role instructions, 1) Multiple LLM agents act as distinct
`experts', each responsible for a specific subtask within a complex task; 2)
Specify the way to collaborate and interact, so that different roles form a
virtual team to facilitate each other's work, ultimately the virtual team
addresses code generation tasks collaboratively without the need for human
intervention. To effectively organize and manage this virtual team, we
incorporate software-development methodology into the framework. Thus, we
assemble an elementary team consisting of three LLM roles (i.e., analyst,
coder, and tester) responsible for software development's analysis, coding, and
testing stages. We conduct comprehensive experiments on various code-generation
benchmarks. Experimental results indicate that self-collaboration code
generation relatively improves 29.9%-47.1% Pass@1 compared to the base LLM
agent. Moreover, we showcase that self-collaboration could potentially enable
LLMs to efficiently handle complex repository-level tasks that are not readily
solved by the single LLM agent.
URL: https://arxiv.org/abs/2304.07590

ID: 30
Title: ChatDev: Communicative Agents for Software Development
Abstract: Software development is a complex task that necessitates cooperation among
multiple members with diverse skills. Numerous studies used deep learning to
improve specific phases in a waterfall model, such as design, coding, and
testing. However, the deep learning model in each phase requires unique
designs, leading to technical inconsistencies across various phases, which
results in a fragmented and ineffective development process. In this paper, we
introduce ChatDev, a chat-powered software development framework in which
specialized agents driven by large language models (LLMs) are guided in what to
communicate (via chat chain) and how to communicate (via communicative
dehallucination). These agents actively contribute to the design, coding, and
testing phases through unified language-based communication, with solutions
derived from their multi-turn dialogues. We found their utilization of natural
language is advantageous for system design, and communicating in programming
language proves helpful in debugging. This paradigm demonstrates how linguistic
communication facilitates multi-agent collaboration, establishing language as a
unifying bridge for autonomous task-solving among LLM agents. The code and data
are available at https://github.com/OpenBMB/ChatDev.
URL: https://arxiv.org/abs/2307.07924

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
,以下是第5批次的论文ID，题目,和一句话描述：ID: 41
Title: MapCoder: Multi-Agent Code Generation for Competitive Problem Solving
Sentence: MapCoder improves code generation by mimicking human programmers with multi-agent prompting, achieving state-of-the-art results on multiple benchmarks.

ID: 42
Title: Fight Fire with Fire: How Much Can We Trust ChatGPT on Source Code-Related Tasks?
Sentence: In a comprehensive evaluation, ChatGPT exhibits limitations in self-verifying generated code, highlighting the need for guiding questions and accurate test reports to enhance its reliability in software development tasks.

ID: 43
Title: Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation
Sentence: FunCoder is a code generation framework that uses a divide-and-conquer strategy with functional consensus to produce more complex programs and reduce error propagation. This approach has significantly improved performance over previous state-of-the-art methods.

ID: 44
Title: Multi-Agent Software Development through Cross-Team Collaboration
Sentence: Our study presents a groundbreaking multi-agent collaborative framework, Cross-Team Collaboration (CTC), which significantly boosts software development quality and efficiency, paving the way for transformative advancements in AI.

ID: 45
Title: MASAI: Modular Architecture for Software-engineering AI Agents
Sentence: MASAI: A modular architecture integrates diverse LLM-agents for efficient, sub-problem solving in software engineering with improved resolution rates on GitHub issues.

ID: 46
Title: AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology
Sentence: AgileCoder is a multi-agent system that enhances software development efficiency using Agile Methodology and a dynamic code graph generator.

ID: 47
Title: CodeNav: Beyond tool-use to using real-world codebases with LLM agents
Sentence: CodeNav is an LLM agent that navigates and leverages code repositories to solve queries without manual tool registration.

ID: 48
Title: INDICT: Code Generation with Internal Dialogues of Critiques for Both Security and Helpfulness
Sentence: INDICT uses internal dialogue of safety and helpfulness critics to enhance LLM code generation, improving output quality by 10%.

ID: 49
Title: AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents
Sentence: AppWorld Engine and Benchmark offer a high-quality environment and diverse tasks to assess interactive coding agents in realistic digital settings, showcasing their capabilities and challenges.

ID: 50
Title: Interactive Program Synthesis
Sentence: Improving program synthesis efficiency and correctness through interactive techniques like incremental algorithms, step-based problem formulation, and feedback-based intent refinement.

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