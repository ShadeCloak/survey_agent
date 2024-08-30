
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
,以下是第11批次的论文ID，题目,和摘要：ID: 61
Title: CYCLE: Learning to Self-Refine the Code Generation
Abstract: Pre-trained code language models have achieved promising performance in code
generation and improved the programming efficiency of human developers.
However, their self-refinement capability is typically overlooked by the
existing evaluations of code LMs, which focus only on the accuracy of the
one-time prediction. For the cases when code LMs fail to implement the correct
program, developers actually find it hard to debug and fix the faulty
prediction since it is not written by the developers themselves. Unfortunately,
our study reveals that code LMs cannot efficiently self-refine their faulty
generations as well.
  In this paper, we propose CYCLE framework, learning to self-refine the faulty
generation according to the available feedback, such as the execution results
reported by the test suites. We evaluate CYCLE on three popular code generation
benchmarks, HumanEval, MBPP, and APPS. The results reveal that CYCLE
successfully maintains, sometimes improves, the quality of one-time code
generation, while significantly improving the self-refinement capability of
code LMs. We implement four variants of CYCLE with varied numbers of parameters
across 350M, 1B, 2B, and 3B, and the experiments show that CYCLE consistently
boosts the code generation performance, by up to 63.5%, across benchmarks and
varied model sizes. We also notice that CYCLE outperforms code LMs that have
3$\times$ more parameters in self-refinement.
URL: https://arxiv.org/abs/2403.18746

ID: 62
Title: LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation
Abstract: Large language models (LLMs) have shown great potential in automating
significant aspects of coding by producing natural code from informal natural
language (NL) intent. However, given NL is informal, it does not lend easily to
checking that the generated code correctly satisfies the user intent. In this
paper, we propose a novel interactive workflow TiCoder for guided intent
clarification (i.e., partial formalization) through tests to support the
generation of more accurate code suggestions. Through a mixed methods user
study with 15 programmers, we present an empirical evaluation of the
effectiveness of the workflow to improve code generation accuracy. We find that
participants using the proposed workflow are significantly more likely to
correctly evaluate AI generated code, and report significantly less
task-induced cognitive load. Furthermore, we test the potential of the workflow
at scale with four different state-of-the-art LLMs on two python datasets,
using an idealized proxy for a user feedback. We observe an average absolute
improvement of 38.43% in the pass@1 code generation accuracy for both datasets
and across all LLMs within 5 user interactions, in addition to the automatic
generation of accompanying unit tests.
URL: https://arxiv.org/abs/2404.10100

ID: 63
Title: SOAP: Enhancing Efficiency of Generated Code via Self-Optimization
Abstract: Large language models (LLMs) have shown remarkable progress in code
generation, but their generated code often suffers from inefficiency, resulting
in longer execution times and higher memory consumption. To address this issue,
we propose Self Optimization based on OverheAd Profile (SOAP), a
self-optimization framework that utilizes execution overhead profiles to
improve the efficiency of LLM-generated code. SOAP first generates code using
an LLM, then executes it locally to capture execution time and memory usage
profiles. These profiles are fed back to the LLM, which then revises the code
to reduce overhead. To evaluate the effectiveness of SOAP, we conduct extensive
experiments on the EffiBench, HumanEval, and MBPP with 16 open-source and 6
closed-source models. Our evaluation results demonstrate that through iterative
self-optimization, SOAP significantly enhances the efficiency of LLM-generated
code. For example, the execution time (ET) of StarCoder2-15B for the EffiBench
decreases from 0.93 (s) to 0.12 (s) which reduces 87.1% execution time
requirement compared with the initial code. The total memory usage (TMU) of
StarCoder2-15B also decreases from 22.02 (Mb*s) to 2.03 (Mb*s), which decreases
90.8% total memory consumption during the execution process. The source code of
SOAP was released in https://github.com/huangd1999/SOAP.
URL: https://arxiv.org/abs/2405.15189

ID: 64
Title: Code Repair with LLMs gives an Exploration-Exploitation Tradeoff
Abstract: Iteratively improving and repairing source code with large language models
(LLMs), known as refinement, has emerged as a popular way of generating
programs that would be too complex to construct in one shot. Given a bank of
test cases, together with a candidate program, an LLM can improve that program
by being prompted with failed test cases. But it remains an open question how
to best iteratively refine code, with prior work employing simple greedy or
breadth-first strategies. We show here that refinement exposes an
explore-exploit tradeoff: exploit by refining the program that passes the most
test cases, or explore by refining a lesser considered program. We frame this
as an arm-acquiring bandit problem, which we solve with Thompson Sampling. The
resulting LLM-based program synthesis algorithm is broadly applicable: Across
loop invariant synthesis, visual reasoning puzzles, and competition programming
problems, we find that our new method can solve more problems using fewer
language model calls.
URL: https://arxiv.org/abs/2405.17503

ID: 65
Title: ReflectionCoder: Learning from Reflection Sequence for Enhanced One-off Code Generation
Abstract: Code generation plays a crucial role in various tasks, such as code
auto-completion and mathematical reasoning. Previous work has proposed numerous
methods to enhance code generation performance, including integrating feedback
from the compiler. Inspired by this, we present ReflectionCoder, a novel
approach that effectively leverages reflection sequences constructed by
integrating compiler feedback to improve one-off code generation performance.
Furthermore, we propose reflection self-distillation and dynamically masked
distillation to effectively utilize these reflection sequences. Extensive
experiments on three benchmarks, i.e., HumanEval (+), MBPP (+), and MultiPl-E,
demonstrate that models fine-tuned with our method achieve state-of-the-art
performance. Notably, ReflectionCoder-DeepSeek-Coder-33B reaches pass@1 of 82.9
(76.8) on HumanEval (+) and 84.1 (72.0) on MBPP (+), on par with GPT-3.5-Turbo
and Claude-3-opus, and surpasses early GPT-4. Beyond the code domain, we
believe this approach can benefit other domains that focus on final results and
require long reasoning paths. Code and data are available at
https://github.com/SenseLLM/ReflectionCoder.
URL: https://arxiv.org/abs/2405.17057

ID: 66
Title: Training LLMs to Better Self-Debug and Explain Code
Abstract: In the domain of code generation, self-debugging is crucial. It allows LLMs
to refine their generated code based on execution feedback. This is
particularly important because generating correct solutions in one attempt
proves challenging for complex tasks. Prior works on self-debugging mostly
focus on prompting methods by providing LLMs with few-shot examples, which work
poorly on small open-sourced LLMs. In this work, we propose a training
framework that significantly improves self-debugging capability of LLMs.
Intuitively, we observe that a chain of explanations on the wrong code followed
by code refinement helps LLMs better analyze the wrong code and do refinement.
We thus propose an automated pipeline to collect a high-quality dataset for
code explanation and refinement by generating a number of explanations and
refinement trajectories and filtering via execution verification. We perform
supervised fine-tuning (SFT) and further reinforcement learning (RL) on both
success and failure trajectories with a novel reward design considering code
explanation and refinement quality. SFT improves the pass@1 by up to 15.92% and
pass@10 by 9.30% over four benchmarks. RL training brings additional up to
3.54% improvement on pass@1 and 2.55% improvement on pass@10. The trained LLMs
show iterative refinement ability, and can keep refining code continuously.
Lastly, our human evaluation shows that the LLMs trained with our framework
generate more useful code explanations and help developers better understand
bugs in source code.
URL: https://arxiv.org/abs/2405.18649

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