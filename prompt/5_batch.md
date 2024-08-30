
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
,以下是第6批次的论文ID，题目,和摘要：ID: 31
Title: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
Abstract: Remarkable progress has been made on automated problem solving through
societies of agents based on large language models (LLMs). Existing LLM-based
multi-agent systems can already solve simple dialogue tasks. Solutions to more
complex tasks, however, are complicated through logic inconsistencies due to
cascading hallucinations caused by naively chaining LLMs. Here we introduce
MetaGPT, an innovative meta-programming framework incorporating efficient human
workflows into LLM-based multi-agent collaborations. MetaGPT encodes
Standardized Operating Procedures (SOPs) into prompt sequences for more
streamlined workflows, thus allowing agents with human-like domain expertise to
verify intermediate results and reduce errors. MetaGPT utilizes an assembly
line paradigm to assign diverse roles to various agents, efficiently breaking
down complex tasks into subtasks involving many agents working together. On
collaborative software engineering benchmarks, MetaGPT generates more coherent
solutions than previous chat-based multi-agent systems. Our project can be
found at https://github.com/geekan/MetaGPT
URL: https://arxiv.org/abs/2308.00352

ID: 32
Title: CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules
Abstract: Large Language Models (LLMs) have already become quite proficient at solving
simpler programming tasks like those in HumanEval or MBPP benchmarks. However,
solving more complex and competitive programming tasks is still quite
challenging for these models - possibly due to their tendency to generate
solutions as monolithic code blocks instead of decomposing them into logical
sub-tasks and sub-modules. On the other hand, experienced programmers
instinctively write modularized code with abstraction for solving complex
tasks, often reusing previously developed modules. To address this gap, we
propose CodeChain, a novel framework for inference that elicits modularized
code generation through a chain of self-revisions, each being guided by some
representative sub-modules generated in previous iterations. Concretely,
CodeChain first instructs the LLM to generate modularized codes through
chain-of-thought prompting. Then it applies a chain of self-revisions by
iterating the two steps: 1) extracting and clustering the generated sub-modules
and selecting the cluster representatives as the more generic and re-usable
implementations, and 2) augmenting the original chain-of-thought prompt with
these selected module-implementations and instructing the LLM to re-generate
new modularized solutions. We find that by naturally encouraging the LLM to
reuse the previously developed and verified sub-modules, CodeChain can
significantly boost both modularity as well as correctness of the generated
solutions, achieving relative pass@1 improvements of 35% on APPS and 76% on
CodeContests. It is shown to be effective on both OpenAI LLMs as well as
open-sourced LLMs like WizardCoder. We also conduct comprehensive ablation
studies with different methods of prompting, number of clusters, model sizes,
program qualities, etc., to provide useful insights that underpin CodeChain's
success.
URL: https://arxiv.org/abs/2310.08992

ID: 33
Title: CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges
Abstract: Large Language Models (LLMs) have shown promise in automated code generation
but typically excel only in simpler tasks such as generating standalone code
units. Real-world software development, however, often involves complex code
repositories (named repo) with complex dependencies and extensive
documentation. To fill this gap, our research pivots towards evaluating LLMs in
a more realistic setting -- real-world repo-level code generation. We introduce
CodeAgentBench, a manually curated benchmark for repo-level code generation.
This benchmark comprises five high-quality Python projects, encompassing a
total of 101 samples. We assess nine leading LLMs on repo-level tasks and
observe a decline in their performance. To tackle this, we present CodeAgent, a
novel LLM-based agent framework that employs external tools for effective
repo-level code generation. CodeAgent integrates five programming tools,
enabling interaction with software artifacts for information retrieval, code
symbol navigation, and code testing. We implement four agent strategies to
optimize these tools' usage. Our experiments on CodeAgentBench show that
CodeAgent enhances LLM performance significantly, with improvements ranging
from 18.1\% to 250\%. Further tests on the HumanEval benchmark confirm
CodeAgent's adaptability and efficacy across various code generation tasks.
Notably, CodeAgent outperforms commercial products like Github Copilot,
showcasing superior accuracy and efficiency. These results demonstrate
CodeAgent's robust capabilities in code generation, highlighting its potential
for real-world repo-level coding challenges.
URL: https://arxiv.org/abs/2401.07339

ID: 34
Title: CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing
Abstract: Large Language Models have revolutionized code generation ability by
converting natural language descriptions into executable code. However,
generating complex code within real-world scenarios remains challenging due to
intricate structures, subtle bugs, understanding of advanced data types, and
lack of supplementary contents. To address these challenges, we introduce the
CoCoST framework, which enhances complex code generation by online searching
for more information with planned queries and correctness testing for code
refinement. Moreover, CoCoST serializes the complex inputs and outputs to
improve comprehension and generates test cases to ensure the adaptability for
real-world applications. CoCoST is validated through rigorous experiments on
the DS-1000 and ClassEval datasets. Experimental results show that CoCoST
substantially improves the quality of complex code generation, highlighting its
potential to enhance the practicality of LLMs in generating complex code.
URL: https://arxiv.org/abs/2403.13583

ID: 35
Title: When LLM-based Code Generation Meets the Software Development Process
Abstract: Software process models play a pivotal role in fostering collaboration and
communication within software teams, enabling them to tackle intricate
development tasks effectively. This paper introduces LCG, a code generation
framework inspired by established software engineering practices. LCG leverages
multiple Large Language Model (LLM) agents to emulate various software process
models, namely LCGWaterfall, LCGTDD, and LCGScrum. Each model assigns LLM
agents specific roles such as requirement engineer, architect, developer,
tester, and scrum master, mirroring typical development activities and
communication patterns. Through collaborative efforts utilizing
chain-of-thought and prompt composition techniques, the agents continuously
refine themselves to enhance code quality. Utilizing GPT3.5 as the underlying
LLM and baseline (GPT), we evaluate LCG across four code generation benchmarks:
HumanEval, HumanEval-ET, MBPP, and MBPP-ET. Results indicate LCGScrum
outperforms other models, achieving Pass@1 scores of 75.2, 65.5, 82.5, and 56.7
in HumanEval, HumanEval-ET, MBPP, and MBPP-ET, respectively - an average 15%
improvement over GPT. Analysis reveals distinct impacts of development
activities on generated code, with design and code reviews contributing to
enhanced exception handling, while design, testing, and code reviews mitigate
code smells. Furthermore, temperature values exhibit negligible influence on
Pass@1 across all models. However, variations in Pass@1 are notable for
different GPT3.5 model versions, ranging from 5 to over 60 in HumanEval,
highlighting the stability of LCG across model versions. This stability
underscores the importance of adopting software process models to bolster the
quality and consistency of LLM-generated code.
URL: https://arxiv.org/abs/2403.15852

ID: 36
Title: RepairAgent: An Autonomous, LLM-Based Agent for Program Repair
Abstract: Automated program repair has emerged as a powerful technique to mitigate the
impact of software bugs on system reliability and user experience. This paper
introduces RepairAgent, the first work to address the program repair challenge
through an autonomous agent based on a large language model (LLM). Unlike
existing deep learning-based approaches, which prompt a model with a fixed
prompt or in a fixed feedback loop, our work treats the LLM as an agent capable
of autonomously planning and executing actions to fix bugs by invoking suitable
tools. RepairAgent freely interleaves gathering information about the bug,
gathering repair ingredients, and validating fixes, while deciding which tools
to invoke based on the gathered information and feedback from previous fix
attempts. Key contributions that enable RepairAgent include a set of tools that
are useful for program repair, a dynamically updated prompt format that allows
the LLM to interact with these tools, and a finite state machine that guides
the agent in invoking the tools. Our evaluation on the popular Defects4J
dataset demonstrates RepairAgent's effectiveness in autonomously repairing 164
bugs, including 39 bugs not fixed by prior techniques. Interacting with the LLM
imposes an average cost of 270,000 tokens per bug, which, under the current
pricing of OpenAI's GPT-3.5 model, translates to 14 cents of USD per bug. To
the best of our knowledge, this work is the first to present an autonomous,
LLM-based agent for program repair, paving the way for future agent-based
techniques in software engineering.
URL: https://arxiv.org/abs/2403.17134

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
,以下是第6批次的论文ID，题目,和一句话描述：ID: 51
Title: Interactive Code Generation via Test-Driven User-Intent Formalization
Sentence: We create interactive test-driven code generation, enhancing large language models by formalizing user intent through generated tests and improving code suggestions.

ID: 52
Title: Improving Code Generation by Training with Natural Language Feedback
Sentence: "Imitation learning from Language Feedback (ILF) is a user-friendly, sample-efficient method for training LLMs on natural language feedback, improving code generation tasks," suggests a new study published by Shanghai AI Lab.

ID: 53
Title: Self-Refine: Iterative Refinement with Self-Feedback
Sentence: This paper introduces Self-Refine, an iterative refinement approach using self-feedback to improve LLM outputs without external data, showing ~20% average performance Improvement.

ID: 54
Title: Teaching Large Language Models to Self-Debug
Sentence: Large language models learn to self-debug by investigating execution results and explaining code, significantly enhancing code generation accuracy and sample efficiency.


ID: 55
Title: Self-Edit: Fault-Aware Code Editor for Code Generation
Sentence: A self-editing fault-aware code editor improves competitive programming code accuracy by 89-94% utilizing execution results and post-processing edits over raw LLM code output.

ID: 56
Title: LeTI: Learning to Generate from Textual Interactions
Sentence: LETI fine-tunes LMs through textual feedback on code generation tasks, exceeding baselines without requiring ground-truth outputs and generalizing to other datasets.

ID: 57
Title: Is Self-Repair a Silver Bullet for Code Generation?
Sentence: Self-repair sometimes improves code generation, but gains are often modest and feedback quality often limits effectiveness.

ID: 58
Title: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback
Sentence: InterCode: A framework for interactive coding that improves execution feedback and reduces errors in LLM-generated code.

ID: 59
Title: OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement
Sentence: OpenCodeInterpreter integrates code generation, execution, and refinement, outperforming baseline models and rivaling proprietary systems with iterative human feedback.

ID: 60
Title: Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback
Sentence: CoCoGen improves LLM-generated code by iteratively refining project context with compiler feedback, enhancing context-dependent code generation by over 80%.

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