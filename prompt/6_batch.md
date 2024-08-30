
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
,以下是第7批次的论文ID，题目,和摘要：ID: 37
Title: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution
Abstract: In software development, resolving the emergent issues within GitHub
repositories is a complex challenge that involves not only the incorporation of
new code but also the maintenance of existing code. Large Language Models
(LLMs) have shown promise in code generation but face difficulties in resolving
Github issues, particularly at the repository level. To overcome this
challenge, we empirically study the reason why LLMs fail to resolve GitHub
issues and analyze the major factors. Motivated by the empirical findings, we
propose a novel LLM-based Multi-Agent framework for GitHub Issue reSolution,
MAGIS, consisting of four agents customized for software evolution: Manager,
Repository Custodian, Developer, and Quality Assurance Engineer agents. This
framework leverages the collaboration of various agents in the planning and
coding process to unlock the potential of LLMs to resolve GitHub issues. In
experiments, we employ the SWE-bench benchmark to compare MAGIS with popular
LLMs, including GPT-3.5, GPT-4, and Claude-2. MAGIS can resolve 13.94% GitHub
issues, significantly outperforming the baselines. Specifically, MAGIS achieves
an eight-fold increase in resolved ratio over the direct application of GPT-4,
the advanced LLM.
URL: https://arxiv.org/abs/2403.17927

ID: 38
Title: Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization
Abstract: Recent advancements in automatic code generation using large language model
(LLM) agent have brought us closer to the future of automated software
development. However, existing single-agent approaches face limitations in
generating and improving large-scale, complex codebases due to constraints in
context length. To tackle this challenge, we propose Self-Organized multi-Agent
framework (SoA), a novel multi-agent framework that enables the scalable and
efficient generation and optimization of large-scale code. In SoA,
self-organized agents operate independently to generate and modify code
components while seamlessly collaborating to construct the overall codebase. A
key feature of our framework is the automatic multiplication of agents based on
problem complexity, allowing for dynamic scalability. This enables the overall
code volume to be increased indefinitely according to the number of agents,
while the amount of code managed by each agent remains constant. We evaluate
SoA on the HumanEval benchmark and demonstrate that, compared to a single-agent
system, each agent in SoA handles significantly less code, yet the overall
generated code is substantially greater. Moreover, SoA surpasses the powerful
single-agent baseline by 5% in terms of Pass@1 accuracy.
URL: https://arxiv.org/abs/2404.02183

ID: 39
Title: AutoCodeRover: Autonomous Program Improvement
Abstract: Researchers have made significant progress in automating the software
development process in the past decades. Recent progress in Large Language
Models (LLMs) has significantly impacted the development process, where
developers can use LLM-based programming assistants to achieve automated
coding. Nevertheless, software engineering involves the process of program
improvement apart from coding, specifically to enable software maintenance
(e.g. bug fixing) and software evolution (e.g. feature additions). In this
paper, we propose an automated approach for solving GitHub issues to
autonomously achieve program improvement. In our approach called AutoCodeRover,
LLMs are combined with sophisticated code search capabilities, ultimately
leading to a program modification or patch. In contrast to recent LLM agent
approaches from AI researchers and practitioners, our outlook is more software
engineering oriented. We work on a program representation (abstract syntax
tree) as opposed to viewing a software project as a mere collection of files.
Our code search exploits the program structure in the form of classes/methods
to enhance LLM's understanding of the issue's root cause, and effectively
retrieve a context via iterative search. The use of spectrum-based fault
localization using tests, further sharpens the context, as long as a test-suite
is available. Experiments on SWE-bench-lite (300 real-life GitHub issues) show
increased efficacy in solving GitHub issues (19% on SWE-bench-lite), which is
higher than the efficacy of the recently reported SWE-agent. In addition,
AutoCodeRover achieved this efficacy with significantly lower cost (on average,
$0.43 USD), compared to other baselines. We posit that our workflow enables
autonomous software engineering, where, in future, auto-generated code from
LLMs can be autonomously improved.
URL: https://arxiv.org/abs/2404.05427

ID: 40
Title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
Abstract: Language model (LM) agents are increasingly being used to automate
complicated tasks in digital environments. Just as humans benefit from powerful
software applications, such as integrated development environments, for complex
tasks like software engineering, we posit that LM agents represent a new
category of end users with their own needs and abilities, and would benefit
from specially-built interfaces to the software they use. We investigate how
interface design affects the performance of language model agents. As a result
of this exploration, we introduce SWE-agent: a system that facilitates LM
agents to autonomously use computers to solve software engineering tasks.
SWE-agent's custom agent-computer interface (ACI) significantly enhances an
agent's ability to create and edit code files, navigate entire repositories,
and execute tests and other programs. We evaluate SWE-agent on SWE-bench and
HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate
of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art
achieved with non-interactive LMs. Finally, we provide insight on how the
design of the ACI can impact agents' behavior and performance.
URL: https://arxiv.org/abs/2405.15793

ID: 41
Title: MapCoder: Multi-Agent Code Generation for Competitive Problem Solving
Abstract: Code synthesis, which requires a deep understanding of complex natural
language problem descriptions, generation of code instructions for complex
algorithms and data structures, and the successful execution of comprehensive
unit tests, presents a significant challenge. While large language models
(LLMs) demonstrate impressive proficiency in natural language processing, their
performance in code generation tasks remains limited. In this paper, we
introduce a new approach to code generation tasks leveraging multi-agent
prompting that uniquely replicates the full cycle of program synthesis as
observed in human developers. Our framework, MapCoder, consists of four LLM
agents specifically designed to emulate the stages of this cycle: recalling
relevant examples, planning, code generation, and debugging. After conducting
thorough experiments, with multiple LLM ablations and analyses across eight
challenging competitive problem-solving and program synthesis benchmarks,
MapCoder showcases remarkable code generation capabilities, achieving new
state-of-the-art results (pass@1) on HumanEval (93.9%), MBPP (83.1%), APPS
(22.0%), CodeContests (28.5%), and xCodeEval (45.3%). Moreover, our method
consistently delivers superior performance across various programming languages
and varying problem difficulties. We open-source our framework at
https://github.com/Md-Ashraful-Pramanik/MapCoder.
URL: https://arxiv.org/abs/2405.11403

ID: 42
Title: Fight Fire with Fire: How Much Can We Trust ChatGPT on Source Code-Related Tasks?
Abstract: With the increasing utilization of large language models such as ChatGPT
during software development, it has become crucial to verify the quality of
code content it generates. Recent studies proposed utilizing ChatGPT as both a
developer and tester for multi-agent collaborative software development. The
multi-agent collaboration empowers ChatGPT to produce test reports for its
generated code, enabling it to self-verify the code content and fix bugs based
on these reports. However, these studies did not assess the effectiveness of
the generated test reports in validating the code. Therefore, we conduct a
comprehensive empirical investigation to evaluate ChatGPT's self-verification
capability in code generation, code completion, and program repair. We request
ChatGPT to (1) generate correct code and then self-verify its correctness; (2)
complete code without vulnerabilities and then self-verify for the presence of
vulnerabilities; and (3) repair buggy code and then self-verify whether the
bugs are resolved. Our findings on two code generation datasets, one code
completion dataset, and two program repair datasets reveal the following
observations: (1) ChatGPT often erroneously predicts its generated incorrect
code as correct. (2) The self-contradictory hallucinations in ChatGPT's
behavior arise. (3) The self-verification capability of ChatGPT can be enhanced
by asking the guiding question, which queries whether ChatGPT agrees with
assertions about incorrectly generated or repaired code and vulnerabilities in
completed code. (4) Using test reports generated by ChatGPT can identify more
vulnerabilities in completed code, but the explanations for incorrectly
generated code and failed repairs are mostly inaccurate in the test reports.
Based on these findings, we provide implications for further research or
development using ChatGPT.
URL: https://arxiv.org/abs/2405.12641

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
,以下是第7批次的论文ID，题目,和一句话描述：ID: 61
Title: CYCLE: Learning to Self-Refine the Code Generation
Sentence: CYCLE framework improves code generation models' ability to refine their own faulty code based on feedback.

ID: 62
Title: LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation
Sentence: A study on TiCoder, a novel interactive workflow that improves large language model-based code generation accuracy through test-driven user intent clarification which was found to reduce cognitive load and improve accuracy by 38.43%.

ID: 63
Title: SOAP: Enhancing Efficiency of Generated Code via Self-Optimization
Sentence: SOAP uses execution profiles to iteratively optimize LLM-generated code, significantly reducing execution time and memory usage.

ID: 64
Title: Code Repair with LLMs gives an Exploration-Exploitation Tradeoff
Sentence: An LLM-based program synthesis algorithm exploits or explores for optimal code repair using Thompson Sampling.

ID: 65
Title: ReflectionCoder: Learning from Reflection Sequence for Enhanced One-off Code Generation
Sentence: Refining one-off code generation via ReflectionCoder, leveraging compiler feedback to yield top-tier performance on HumanEval, MBPP, and MultiPl-E benchmarks, excelling GPT-3.5-Turbo, Claude-3-opus, and early GPT-4.

ID: 66
Title: Training LLMs to Better Self-Debug and Explain Code
Sentence: Enables LLMs to refine code iteratively via fine-tuning and reinforcement learning, improving self-debugging and explanations for developers.

ID: 67
Title: Requirements are All You Need: From Requirements to Code with LLMs
Sentence: This study proposes a tailored LLM for generating code from requirements, enhancing software development processes.

ID: 68
Title: I Need Help! Evaluating LLM's Ability to Ask for Users' Support: A Case Study on Text-to-SQL Generation
Sentence: We evaluate LLMs' ability to ask for user support, finding they often fail to recognize needing help without external signals.

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