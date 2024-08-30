
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
,以下是第8批次的论文ID，题目,和摘要：ID: 43
Title: Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation
Abstract: Despite recent progress made by large language models in code generation,
they still struggle with programs that meet complex requirements. Recent work
utilizes plan-and-solve decomposition to decrease the complexity and leverage
self-tests to refine the generated program. Yet, planning deep-inside
requirements in advance can be challenging, and the tests need to be accurate
to accomplish self-improvement. To this end, we propose FunCoder, a code
generation framework incorporating the divide-and-conquer strategy with
functional consensus. Specifically, FunCoder recursively branches off
sub-functions as smaller goals during code generation, represented by a tree
hierarchy. These sub-functions are then composited to attain more complex
objectives. Additionally, we designate functions via a consensus formed by
identifying similarities in program behavior, mitigating error propagation.
FunCoder outperforms state-of-the-art methods by +9.8% on average in HumanEval,
MBPP, xCodeEval and MATH with GPT-3.5 and GPT-4. Moreover, our method
demonstrates superiority on smaller models: With FunCoder, StableCode-3b
surpasses GPT-3.5 by +18.6% and achieves 97.7% of GPT-4's performance on
HumanEval. Further analysis reveals that our proposed dynamic function
decomposition is capable of handling complex requirements, and the functional
consensus prevails over self-testing in correctness evaluation.
URL: https://arxiv.org/abs/2405.20092

ID: 44
Title: Multi-Agent Software Development through Cross-Team Collaboration
Abstract: The latest breakthroughs in Large Language Models (LLMs), eg., ChatDev, have
catalyzed profound transformations, particularly through multi-agent
collaboration for software development. LLM agents can collaborate in teams
like humans, and follow the waterfall model to sequentially work on
requirements analysis, development, review, testing, and other phases to
perform autonomous software generation. However, for an agent team, each phase
in a single development process yields only one possible outcome. This results
in the completion of only one development chain, thereby losing the opportunity
to explore multiple potential decision paths within the solution space.
Consequently, this may lead to obtaining suboptimal results. To address this
challenge, we introduce Cross-Team Collaboration (CTC), a scalable multi-team
framework that enables orchestrated teams to jointly propose various decisions
and communicate with their insights in a cross-team collaboration environment
for superior content generation. Experimental results in software development
reveal a notable increase in quality compared to state-of-the-art baselines,
underscoring the efficacy of our framework. The significant improvements in
story generation demonstrate the promising generalization ability of our
framework across various domains. We anticipate that our work will guide LLM
agents towards a cross-team paradigm and contribute to their significant growth
in but not limited to software development. The code and data will be available
at https://github.com/OpenBMB/ChatDev.
URL: https://arxiv.org/abs/2406.08979

ID: 45
Title: MASAI: Modular Architecture for Software-engineering AI Agents
Abstract: A common method to solve complex problems in software engineering, is to
divide the problem into multiple sub-problems. Inspired by this, we propose a
Modular Architecture for Software-engineering AI (MASAI) agents, where
different LLM-powered sub-agents are instantiated with well-defined objectives
and strategies tuned to achieve those objectives. Our modular architecture
offers several advantages: (1) employing and tuning different problem-solving
strategies across sub-agents, (2) enabling sub-agents to gather information
from different sources scattered throughout a repository, and (3) avoiding
unnecessarily long trajectories which inflate costs and add extraneous context.
MASAI enabled us to achieve the highest performance (28.33% resolution rate) on
the popular and highly challenging SWE-bench Lite dataset consisting of 300
GitHub issues from 11 Python repositories. We conduct a comprehensive
evaluation of MASAI relative to other agentic methods and analyze the effects
of our design decisions and their contribution to the success of MASAI.
URL: https://arxiv.org/abs/2406.11638

ID: 46
Title: AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology
Abstract: Software agents have emerged as promising tools for addressing complex
software engineering tasks. Existing works, on the other hand, frequently
oversimplify software development workflows, despite the fact that such
workflows are typically more complex in the real world. Thus, we propose
AgileCoder, a multi agent system that integrates Agile Methodology (AM) into
the framework. This system assigns specific AM roles - such as Product Manager,
Developer, and Tester to different agents, who then collaboratively develop
software based on user inputs. AgileCoder enhances development efficiency by
organizing work into sprints, focusing on incrementally developing software
through sprints. Additionally, we introduce Dynamic Code Graph Generator, a
module that creates a Code Dependency Graph dynamically as updates are made to
the codebase. This allows agents to better comprehend the codebase, leading to
more precise code generation and modifications throughout the software
development process. AgileCoder surpasses existing benchmarks, like ChatDev and
MetaGPT, establishing a new standard and showcasing the capabilities of multi
agent systems in advanced software engineering environments.
URL: https://arxiv.org/abs/2406.11912

ID: 47
Title: CodeNav: Beyond tool-use to using real-world codebases with LLM agents
Abstract: We present CodeNav, an LLM agent that navigates and leverages previously
unseen code repositories to solve user queries. In contrast to tool-use LLM
agents that require ``registration'' of all relevant tools via manual
descriptions within the LLM context, CodeNav automatically indexes and searches
over code blocks in the target codebase, finds relevant code snippets, imports
them, and uses them to iteratively generate a solution with execution feedback.
To highlight the core-capabilities of CodeNav, we first showcase three case
studies where we use CodeNav for solving complex user queries using three
diverse codebases. Next, on three benchmarks, we quantitatively compare the
effectiveness of code-use (which only has access to the target codebase) to
tool-use (which has privileged access to all tool names and descriptions).
Finally, we study the effect of varying kinds of tool and library descriptions
on code-use performance, as well as investigate the advantage of the agent
seeing source code as opposed to natural descriptions of code. All code will be
made open source under a permissive license.
URL: https://arxiv.org/abs/2406.12276

ID: 48
Title: INDICT: Code Generation with Internal Dialogues of Critiques for Both Security and Helpfulness
Abstract: Large language models (LLMs) for code are typically trained to align with
natural language instructions to closely follow their intentions and
requirements. However, in many practical scenarios, it becomes increasingly
challenging for these models to navigate the intricate boundary between
helpfulness and safety, especially against highly complex yet potentially
malicious instructions. In this work, we introduce INDICT: a new framework that
empowers LLMs with Internal Dialogues of Critiques for both safety and
helpfulness guidance. The internal dialogue is a dual cooperative system
between a safety-driven critic and a helpfulness-driven critic. Each critic
provides analysis against the given task and corresponding generated response,
equipped with external knowledge queried through relevant code snippets and
tools like web search and code interpreter. We engage the dual critic system in
both code generation stage as well as code execution stage, providing
preemptive and post-hoc guidance respectively to LLMs. We evaluated INDICT on 8
diverse tasks across 8 programming languages from 5 benchmarks, using LLMs from
7B to 70B parameters. We observed that our approach can provide an advanced
level of critiques of both safety and helpfulness analysis, significantly
improving the quality of output codes ($+10\%$ absolute improvements in all
models).
URL: https://arxiv.org/abs/2407.02518

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