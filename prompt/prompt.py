prompt_to_catalogue = r"""
你是一个写综述的科研人员，你需要仔细理解所提供的特定主题的论文摘要,自主设计一个目录，并根据论文们的主要研究方向对以下论文进行分组。
要求：
1.每一个分组只需要有三部分：\section{}、%IDs:[]、%[over]。
2.论文编号汇总到注释%[]里面,格式为：%IDs:['1','2']。
3.每一组以%[over]结尾，方便后续操作。
4.要求每一篇论文都需要包含在内，论文可以被重复分组。
5.子标题下3到9篇论文合适。
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

\subsection{Learning from Proxy Tasks} 
%IDs:[]
%[over]

\section{Paradigm 3: NLP as Text Generation}

\subsection{Generating Label-Augmented Texts}
%IDs:[]
%[over]

\subsection{Generating Word Indices}
%IDs:[]
%[over]

\subsection{Generating Answers}
%IDs:[]
%[over]

\subsection{Filling templates}
%IDs:[]
%[over]

\subsection{Generating Structure-Linearized Texts}
%IDs:[]
%[over]

\subsection{Ranking Input-Output Pairs}
%IDs:[]
%[over]
"""

prompt_abs_ins = """
现在由此生成\begin{abstract}和\section{Introduction}的基本内容。要求学术风格。
参考示例：
\begin{abstract}
Large, pre-trained transformer-based language models such as BERT have drastically changed the Natural Language Processing (NLP) field. We present a survey of recent work that uses these large language models to solve NLP tasks via pre-training then fine-tuning, prompting, or text generation approaches. We also present approaches that use pre-trained language models to generate data for training augmentation or other purposes. We conclude with discussions on limitations and suggested directions for future research. 
\end{abstract}

\section{Introduction}

In recent years, large pre-trained transformer-based language models (PLMs), such as the BERT \citep{devlin-etal-2019-bert} and GPT \citep{radford2018improving} families of models, have taken Natural Language Processing (NLP) by storm, achieving state-of-the-art performance on many tasks. 

These large PLMs have fueled a paradigm shift in NLP. Take a classification task $p(y|x)$ (classifying textual input $x$ into a label $y$) as an example: traditional statistical NLP approaches often design hand-crafted features to represent $x$, and then apply a machine learning model (e.g. SVM \citep{cortes1995support}, logistic regression) to learn the classification function. Deep learning models learn the latent feature representation via a deep neural network \cite{lecun2015deep} in addition to the classification function. Note that the latent  representation needs to be learned afresh for each new NLP task, and that, in many cases, the size of the training data limits the quality of the latent feature representation. Given that the nuances of language are common to all NLP tasks, one could posit that we could learn a generic latent feature representations from some generic task once, and then share it across all NLP tasks. Language modeling, where the model needs to learn how to predict the next word given previous words, is  such a generic task with abundant naturally occurring text to pre-train such a model (hence the name pre-trained language models).  In fact, the latest, ongoing paradigm shift begins when PLMs are introduced: for numerous NLP tasks, researchers now leverage existing PLMs via {\it fine-tuning} for the task of interest, {\it prompting} the PLMs to perform the desired task, or reformulating the task as a {\it text generation} problem with application of PLMs to solve it accordingly. Advances in these three PLM-based paradigms have continuously established new state-of-the-art performances. 
"""

prompt_con = """
现在由此生成\section{Conclusion}的基本内容。要求学术风格。
参考示例：
\section{Conclusion}
\label{sec:conclusion}

In this paper, we present a survey of the three trending paradigms that use pre-trained language models for NLP. We describe each of them in depth, and summarize prior works whose applications have shown promise. In addition, we describe the use of pre-trained language models to automatically generate data that is used to improve performance in NLP tasks. We hope this survey will provide readers with key fundamental concepts and a comprehensive view of the paradigm shift. 
"""

prompt_to_section = r"""
你是一名撰写学术综述文章的科研人员，在参考示例的帮助下，根据几篇相关论文的摘要撰写一个学术论文段落,。

任务描述：

1.针对每篇论文的核心技术或方法进行详细说明，重点分析各技术或方法的优缺点。
2.在段落中对不同论文的异同进行深入对比，尤其是与前文提到的研究相比，突出创新点。
3.确保段落紧扣指定主题，逻辑严密，并符合学术写作风格。
4.只能使用\citeauthor{}或者\citealp{}或者\citet{}引用提供的论文，未提供的论文不能进行引用。

写作要求：

1.表达上避免口语化，要使用学术论文常见的严谨表达和结构
2.禁止简单堆砌内容，务必确保段落内容连贯且有逻辑。
3.禁止使用诸如“首先”、“接下来”、“最后”、'first','second','third','final'等简单的过渡词，改用符合学术写作的过渡方式。
4.论文引用格式必须严格按照示例格式执行，还要确保每个引用都准确无误。
5.按照LaTex格式输出，比如百分数：20\%；\textbf{}。

示例参考：
示例一：
\subsection{Instruction Finetuning and Reinforcement Learning for Code}\label{sec:instruction}
In natural language processing, training models on a diverse set of tasks with instruction prefix, known as instruction finetuning, has been shown to unlock the ability of cross-task generalization~(\citealp{2022InstructGPT}; \citealp{2022FLAN}; \citealp{2022OPT-IML}). At first, these instruction data samples are manually compiled or crowd-sourced~(\citealp{2021FLAN}; \citealp{2021T0}), but later researches find LLM-generated instructions to be sufficient~(\citealp{2022Self-Instruct}; \citealp{2022Unnatural}).

Following these works in natural language, researchers from the code community have applied instruction tuning to their models as well. \citet{2023CodeT5+} finetune CodeT5+ with 20K instruction data generated by InstructGPT~\citep{2022InstructGPT} to obtain InstructCodeT5+. WizardCoder~\citep{2023WizardCoder} follows the methods of WizardLM~\citep{2023WizardLM} to evolve 20K code Alpaca~\citep{2023alpaca} samples into a 78K dataset and uses it to finetune StarCoder. Pangu-Coder 2~\citep{2023Pangu-Coder2} also uses WizardLM's Evol-Instruct to generate 68K instruction samples from 20K code Alpaca, but also introduces reinforcement learning via Rank Responses to align Test \& Teacher Feedback (RRTF). OctoCoder~\citep{2023OctoPack}, on the other hand, takes a different path and uses Git commit histories as instruction data to finetune StarCoder and CodeGeeX2. More recently, CodeFuse~\citep{2023MFTCoder} also employs multitask-finetuning and explicitly introduces multiple downstream tasks into their instruction data. The performance of these instruction finetuned code models can also be found in Table~\ref{tab:specialized-model}.

In NLP, another technology closely related to instruction finetuning is reinforcement learning from human feedback (RLHF), which has played a significant role in aligning LLMs with human values~(\citealp{2022InstructGPT}; \citealp{2022Anthropic}). The merit of reinforcement learning is that it can incorporate non-differentiable reward signals into training, such as BLEU~\citep{2016RL-seq2seq} and human preference~\citep{2017RL-human}, but the human feedback required in aligning LLMs often involves extensive labor on annotation. In comparison, applying reinforcement learning to code models has a natural advantage, as compilers can be used for automatically generating feedback for code samples produced by language models.

CodeRL~\citep{2022CodeRL} is one such model, which defines four levels of rewards for each generated program (viz. compile error, runtime error, unit test failure, pass) as well as fine-grained token-level reward estimated by a critic model. The actor model, which is an extension of CodeT5, is then trained with REINFORCE algorithm~\citep{1992REINFORCE}. Similarly, CompCoder~\citep{2022CompCoder} and PPOCoder~\citep{2023PPOCoder} train CodeGPT and CodeT5 respectively with proximal policy optimization~\citep{2017PPO}, while RLTF~\citep{2023RLTF} proposes fine-grained feedback based on the error information and location provided by the compiler, as well as adaptive feedback that takes the ratio of passed test cases into account.
示例二：
\subsubsection{Explaining Models' Decisions}

Despite the impressive performance of deep learning models for various NLP tasks, a remaining challenge to widespread adoption is the lack of explanations for the models' decisions. This hinders the development and debugging process, as well as user trust. This is especially true for application domains such as healthcare, security, and online education. As such, a considerable number of approaches have been proposed for explaining deep learning models' behavior, including model-intrinsic \citep{ribeiro2016why,lundberg2017aunified,chen2018learning} and model-agnostic approaches \citep{park18multimodal,kim2018textual,ling2017program}. While model-intrinsic explanations expose internal model state (e.g. feature importance or attention scores), in model-agnostic (post-hoc) methods, explanations are generated via the model predictions without inspecting the internal state. Generative models are often applied for post-hoc explanations, aiming to obtain either counterexamples \citep{kim2016examples,wachter2018counterfactual,wu2021polyjuice} or natural language texts \citep{camburu2018esnli,kumar2020nile,chen2021kace} for explaining purposes. 

Generating {\it counterexamples} can shed light on the decision boundaries of the models (i.e. explaining when a model changes its decision), thus improving intepretability. To this end, the generated counterexamples should be close to the decision boundaries so that small modifications result in changing the model predictions. Traditionally, heuristic rules applied to the original inputs create likely counterexamples \citep{wachter2018counterfactual,ribeiro2018semantically,iyyer2018adversarial,li2021contextualized}. PLMs have been leveraged to generate more diverse examples for better evaluation \citep{madaan2021generate,wu2021polyjuice,ross2021explaining}. In particular, \citet{wu2021polyjuice} proposes a method based on GPT-2 to generate counterfactuals that are close to the original sentences and entail specific relationships with the original, facilitating label induction (e.g. negation, insertion, shuffle). Concretely, an input sentence is concatenated with a relation label (e.g. negation) and a template consisting of the special tokens \texttt{[BLANK]} to form the prompt for GPT-2 model. For instance, for the sentence ``\textit{It is great for kids}" and the relation label ``\texttt{negate}", the following prompt is constructed: ``\texttt{It is great for kids. [negation] It is [BLANK] great for [BLANK]. [SEP]}". Next, the GPT-2 model generates answers for the \texttt{[BLANK]} in the template (e.g. ``\texttt{not [ANSWER] children}'', separated by the special token \texttt{[ANSWER]}). To fine-tune the GPT-2 model, non-parallel datasets (e.g. CommonGen, Natural Questions and SQuAD) are automatically processed to find the relations between pairs of sentences and to construct the templates for each relation based on the obtained pairs. It is worth noting that the sentences generated by GPT-2 might have the same label as the original input sentence. In addition, \citet{wu2021polyjuice} show that the generated counterexamples can be helpful to improve the performance of the downstream models, e.g.~for natural language inference, duplicate question detection, and sentiment analysis.

Other research is informing the task of {\it natural language explanation generation}, where the goal is to expose the rationale behind the model decisions in automatically generated natural language text.  Any approach must critically require that the generated response is faithful to the model behavior. To this end, \citet{kumar2020nile} propose to first generate the explanations, and then employ the explanations to obtain the final model predictions. They use natural language inference as the task requiring explanations. Label-specific GPT-2 models are fine-tuned over concatenations of corresponding premises, hypotheses, and human-provided explanations, so that at inference, the model generates an explanation based on premise and hypothesis. Next, the explanations together with the premise and the hypothesis are consumed by an explanation processor model (e.g. RoBERTa) to select the most likely label. This process obtains a more faithful explanation for the  label choice, compared to traditional prediction-first approaches \cite{camburu2018esnli}. However, this approach does not provide explanations that reference non-selected labels. To address the question of why other labels are not chosen, \citet{chen2021kace} exploit counterexamples, deriving them from original samples with heuristic rules. The original samples and counterexamples are provided to GPT-2 to generate an explanation for the question ``\textit{Why A not B}''.
示例三：
\subsection{Direct Policy Optimization}\label{subsec:direct-methods}

The two-phase approach involving utility learning and policy optimization is not the only viable path to learning a policy from human feedback.
While we have previously discussed the case in which we learn a reward function from observed preferences by assuming a human feedback model, an emerging branch of the literature is concerned with circumventing the reward-learning step and using preferences directly to address the actual \gls{RL} problem.
Concrete approaches are DPO~\citep{rafailov2023direct}, SLiC-HF~\citep{zhao2023slichf}, OPPO~\citep{kang2023reward}, DPPO~\citep{an2023direct}, PRO~\citep{song2024preference}, RSO~\citep{liu2024statistical}, or by formulating policy search as a zeroth-order optimization \citep{tang2024zerothorder}.
\Citet{azar2023general} introduce an objective called $\Psi$-preference optimization ($\Psi$PO) that unifies the objective functions in \gls{DPO} and \gls{RLHF}.
More specifically, for a specific instantiation of $\Psi$, the objective in $\Psi$PO recovers \gls{DPO} and SLiC-HF.
In addition, \gls{DPO} has been further generalized to include diverse divergence constraints \citep{wang2024reverse}.
Besides, \citet{hejna2024contrastive} propose contrastive preference learning based on a regret preference model instead of the usual one in \gls{RLHF}.
It is also possible to learn a \( Q \) function from human preferences directly, which implies a policy without the need for separate policy- and reward-model training \citep{myers2023active}.

It is worth noting that approaches for directly learning the policy from preferences have been considered in the past as well~\citep{wilson2012bayesian,furnkranz2012preferencebased,wirth2013policy,wirth2013epmc,busa-fekete2014preferencebased}.
In Sections 3.2.1 and 3.2.2 in the survey by \citet{wirth2017survey}, these methods are explained in more detail.

Another recent trend in fine-tuning models with human feedback is to even manage it without the usage of RL. 
An alternative is based on supervised reward learning with new types of loss functions \citep{lee2023aligning,yuan2023rrhf} or a specific learning process   \citep{dong2023raft,korbak2023pretraining}.
There are also RL-free approaches that do not use a reward model to train a policy to execute natural-language instructions using a transformer
architecture \citep{brohan2023rt1,yu2023scaling}.
On a related note, \Citet{liu2024chain} suggest a way how to convert human feedback to natural language sentences for the task of fine-tuning language models.
"""

prompt_get_score = """
你是一个对语言风格敏感的评论家，现在需要对llm生成的综述片段进行学术风格方面的打分。

学术风格评分标准：
1. 语言的正式性：是否使用了正式、规范的学术语言，避免了口语化表达。
2. 引用与参考文献的使用：是否正确引用了相关文献，并采用了标准的学术引用格式。
3. 逻辑性与结构性：段落是否结构清晰，逻辑严密，内容层次分明。
4. 内容的准确性与精确性：是否准确表达了相关领域的概念与研究结果。
5. 中立性与客观性：是否保持中立立场，避免主观性陈述。

请在参考经典综述片段来理解学术风格的帮助下，对所给片段打一个百分制的分数,分数需要在一开始放在()里面，并给出打分理由和改进建议，打分理由和改进建议分别各自放在后面的()里面，以便后续操作。

输出格式：
(100)(理由：)(改进建议：)

参考经典综述片段：
示例一：
\subsection{Instruction Finetuning and Reinforcement Learning for Code}\label{sec:instruction}
In natural language processing, training models on a diverse set of tasks with instruction prefix, known as instruction finetuning, has been shown to unlock the ability of cross-task generalization~(\citealp{2022InstructGPT}; \citealp{2022FLAN}; \citealp{2022OPT-IML}). At first, these instruction data samples are manually compiled or crowd-sourced~(\citealp{2021FLAN}; \citealp{2021T0}), but later researches find LLM-generated instructions to be sufficient~(\citealp{2022Self-Instruct}; \citealp{2022Unnatural}).

Following these works in natural language, researchers from the code community have applied instruction tuning to their models as well. \citet{2023CodeT5+} finetune CodeT5+ with 20K instruction data generated by InstructGPT~\citep{2022InstructGPT} to obtain InstructCodeT5+. WizardCoder~\citep{2023WizardCoder} follows the methods of WizardLM~\citep{2023WizardLM} to evolve 20K code Alpaca~\citep{2023alpaca} samples into a 78K dataset and uses it to finetune StarCoder. Pangu-Coder 2~\citep{2023Pangu-Coder2} also uses WizardLM's Evol-Instruct to generate 68K instruction samples from 20K code Alpaca, but also introduces reinforcement learning via Rank Responses to align Test \& Teacher Feedback (RRTF). OctoCoder~\citep{2023OctoPack}, on the other hand, takes a different path and uses Git commit histories as instruction data to finetune StarCoder and CodeGeeX2. More recently, CodeFuse~\citep{2023MFTCoder} also employs multitask-finetuning and explicitly introduces multiple downstream tasks into their instruction data. The performance of these instruction finetuned code models can also be found in Table~\ref{tab:specialized-model}.

In NLP, another technology closely related to instruction finetuning is reinforcement learning from human feedback (RLHF), which has played a significant role in aligning LLMs with human values~(\citealp{2022InstructGPT}; \citealp{2022Anthropic}). The merit of reinforcement learning is that it can incorporate non-differentiable reward signals into training, such as BLEU~\citep{2016RL-seq2seq} and human preference~\citep{2017RL-human}, but the human feedback required in aligning LLMs often involves extensive labor on annotation. In comparison, applying reinforcement learning to code models has a natural advantage, as compilers can be used for automatically generating feedback for code samples produced by language models.

CodeRL~\citep{2022CodeRL} is one such model, which defines four levels of rewards for each generated program (viz. compile error, runtime error, unit test failure, pass) as well as fine-grained token-level reward estimated by a critic model. The actor model, which is an extension of CodeT5, is then trained with REINFORCE algorithm~\citep{1992REINFORCE}. Similarly, CompCoder~\citep{2022CompCoder} and PPOCoder~\citep{2023PPOCoder} train CodeGPT and CodeT5 respectively with proximal policy optimization~\citep{2017PPO}, while RLTF~\citep{2023RLTF} proposes fine-grained feedback based on the error information and location provided by the compiler, as well as adaptive feedback that takes the ratio of passed test cases into account.

示例二：
\subsubsection{Explaining Models' Decisions}

Despite the impressive performance of deep learning models for various NLP tasks, a remaining challenge to widespread adoption is the lack of explanations for the models' decisions. This hinders the development and debugging process, as well as user trust. This is especially true for application domains such as healthcare, security, and online education. As such, a considerable number of approaches have been proposed for explaining deep learning models' behavior, including model-intrinsic \citep{ribeiro2016why,lundberg2017aunified,chen2018learning} and model-agnostic approaches \citep{park18multimodal,kim2018textual,ling2017program}. While model-intrinsic explanations expose internal model state (e.g. feature importance or attention scores), in model-agnostic (post-hoc) methods, explanations are generated via the model predictions without inspecting the internal state. Generative models are often applied for post-hoc explanations, aiming to obtain either counterexamples \citep{kim2016examples,wachter2018counterfactual,wu2021polyjuice} or natural language texts \citep{camburu2018esnli,kumar2020nile,chen2021kace} for explaining purposes. 

Generating {\it counterexamples} can shed light on the decision boundaries of the models (i.e. explaining when a model changes its decision), thus improving intepretability. To this end, the generated counterexamples should be close to the decision boundaries so that small modifications result in changing the model predictions. Traditionally, heuristic rules applied to the original inputs create likely counterexamples \citep{wachter2018counterfactual,ribeiro2018semantically,iyyer2018adversarial,li2021contextualized}. PLMs have been leveraged to generate more diverse examples for better evaluation \citep{madaan2021generate,wu2021polyjuice,ross2021explaining}. In particular, \citet{wu2021polyjuice} proposes a method based on GPT-2 to generate counterfactuals that are close to the original sentences and entail specific relationships with the original, facilitating label induction (e.g. negation, insertion, shuffle). Concretely, an input sentence is concatenated with a relation label (e.g. negation) and a template consisting of the special tokens \texttt{[BLANK]} to form the prompt for GPT-2 model. For instance, for the sentence ``\textit{It is great for kids}" and the relation label ``\texttt{negate}", the following prompt is constructed: ``\texttt{It is great for kids. [negation] It is [BLANK] great for [BLANK]. [SEP]}". Next, the GPT-2 model generates answers for the \texttt{[BLANK]} in the template (e.g. ``\texttt{not [ANSWER] children}'', separated by the special token \texttt{[ANSWER]}). To fine-tune the GPT-2 model, non-parallel datasets (e.g. CommonGen, Natural Questions and SQuAD) are automatically processed to find the relations between pairs of sentences and to construct the templates for each relation based on the obtained pairs. It is worth noting that the sentences generated by GPT-2 might have the same label as the original input sentence. In addition, \citet{wu2021polyjuice} show that the generated counterexamples can be helpful to improve the performance of the downstream models, e.g.~for natural language inference, duplicate question detection, and sentiment analysis.

Other research is informing the task of {\it natural language explanation generation}, where the goal is to expose the rationale behind the model decisions in automatically generated natural language text.  Any approach must critically require that the generated response is faithful to the model behavior. To this end, \citet{kumar2020nile} propose to first generate the explanations, and then employ the explanations to obtain the final model predictions. They use natural language inference as the task requiring explanations. Label-specific GPT-2 models are fine-tuned over concatenations of corresponding premises, hypotheses, and human-provided explanations, so that at inference, the model generates an explanation based on premise and hypothesis. Next, the explanations together with the premise and the hypothesis are consumed by an explanation processor model (e.g. RoBERTa) to select the most likely label. This process obtains a more faithful explanation for the  label choice, compared to traditional prediction-first approaches \cite{camburu2018esnli}. However, this approach does not provide explanations that reference non-selected labels. To address the question of why other labels are not chosen, \citet{chen2021kace} exploit counterexamples, deriving them from original samples with heuristic rules. The original samples and counterexamples are provided to GPT-2 to generate an explanation for the question ``\textit{Why A not B}''.

示例三：
\subsection{Direct Policy Optimization}\label{subsec:direct-methods}

The two-phase approach involving utility learning and policy optimization is not the only viable path to learning a policy from human feedback.
While we have previously discussed the case in which we learn a reward function from observed preferences by assuming a human feedback model, an emerging branch of the literature is concerned with circumventing the reward-learning step and using preferences directly to address the actual \gls{RL} problem.
Concrete approaches are DPO~\citep{rafailov2023direct}, SLiC-HF~\citep{zhao2023slichf}, OPPO~\citep{kang2023reward}, DPPO~\citep{an2023direct}, PRO~\citep{song2024preference}, RSO~\citep{liu2024statistical}, or by formulating policy search as a zeroth-order optimization \citep{tang2024zerothorder}.
\Citet{azar2023general} introduce an objective called $\Psi$-preference optimization ($\Psi$PO) that unifies the objective functions in \gls{DPO} and \gls{RLHF}.
More specifically, for a specific instantiation of $\Psi$, the objective in $\Psi$PO recovers \gls{DPO} and SLiC-HF.
In addition, \gls{DPO} has been further generalized to include diverse divergence constraints \citep{wang2024reverse}.
Besides, \citet{hejna2024contrastive} propose contrastive preference learning based on a regret preference model instead of the usual one in \gls{RLHF}.
It is also possible to learn a \( Q \) function from human preferences directly, which implies a policy without the need for separate policy- and reward-model training \citep{myers2023active}.

It is worth noting that approaches for directly learning the policy from preferences have been considered in the past as well~\citep{wilson2012bayesian,furnkranz2012preferencebased,wirth2013policy,wirth2013epmc,busa-fekete2014preferencebased}.
In Sections 3.2.1 and 3.2.2 in the survey by \citet{wirth2017survey}, these methods are explained in more detail.

Another recent trend in fine-tuning models with human feedback is to even manage it without the usage of RL. 
An alternative is based on supervised reward learning with new types of loss functions \citep{lee2023aligning,yuan2023rrhf} or a specific learning process   \citep{dong2023raft,korbak2023pretraining}.
There are also RL-free approaches that do not use a reward model to train a policy to execute natural-language instructions using a transformer
architecture \citep{brohan2023rt1,yu2023scaling}.
On a related note, \Citet{liu2024chain} suggest a way how to convert human feedback to natural language sentences for the task of fine-tuning language models.
"""


catalogue = r""" 
\title{Recent Advances in Code Reasoning and Generation with Large Language Models: A Survey}

\section{Program-Aided Language Models for Reasoning}

\subsection{Mathematical and Numerical Reasoning via Code}
%IDs:['1', '2', '3', '4', '13', '14', '17']
%[over]

\subsection{Program Generation and Execution for Enhanced Reasoning}
%IDs:['5', '6', '11', '12', '15', '16', '18']
%[over]

\section{Code Integration and Structural Reasoning}

\subsection{Leveraging Code for Structured Reasoning and Generalization}
%IDs:['7', '9', '8', '19', '22', '23', '24']
%[over]

\subsection{Evaluation and Challenges in Code Reasoning with LLMs}
%IDs:['10', '25', '26', '20', '21', '27', '28']
%[over]

\section{Interactive and Autonomous Code Generation}

\subsection{Interactive and Multi-Agent Code Generation Systems}
%IDs:['29', '30', '31', '32', '33', '34', '38']
%[over]

\subsection{Autonomous Code Generation and Self-Improvement}
%IDs:['35', '36', '37', '39', '40', '41', '42', '43']
%[over]

\section{Refinement, Optimization, and Benchmarking in Code Generation}

\subsection{Iterative Refinement and Self-Optimization}
%IDs:['53', '54', '55', '57', '59', '60', '61', '63']
%[over]

\subsection{Benchmarking and Evaluation of LLM-Based Code Generation}
%IDs:['58', '62', '44', '45', '46', '47', '48', '49']
%[over]

\subsection{Advanced Techniques in Code Repair and Generation}
%IDs:['64', '65', '66', '67', '50', '51', '52', '56', '68']
%[over]
"""
catalogue_825 = r""" 
\title{Recent Advances in Code-Augmented Reasoning and Program-Aided Language Models: A Survey}

\section{Code-Aided Language Model Reasoning}

\subsection{Program-Aided Reasoning Techniques}
%IDs:['1', '2', '3', '4', '5', '6', '7']

\subsection{Code-Enhanced Mathematical Problem Solving}
%IDs:['8', '9', '10', '11', '12', '13']

\subsection{Code-Based Reasoning in Diverse Domains}
%IDs:['14', '15', '16', '17', '18', '19', '20']

\section{Program Synthesis and Code Generation}

\subsection{Language Models as Code Generators}
%IDs:['21', '22', '23', '24', '25', '26', '27']

\subsection{Frameworks for Code Generation and Evaluation}
%IDs:['28', '29', '30', '31', '32', '33', '34']

\subsection{Program Repair and Optimization}
%IDs:['35', '36', '37', '38', '39', '40', '41']

\section{Multi-Agent and Collaborative Systems}

\subsection{Multi-Agent Collaboration for Code Generation}
%IDs:['42', '43', '44', '45', '46', '47', '48']

\subsection{Code Simulation and Testing in Multi-Agent Systems}
%IDs:['49', '50', '51', '52', '53', '54']

\subsection{Autonomous Program Synthesis and Improvement}
%IDs:['55', '56', '57', '58', '59', '60']

\section{Emerging Trends and Future Directions}

\subsection{Novel Approaches in Program-Aided Reasoning}
%IDs:['61', '62', '63', '64', '65', '66']

\subsection{Integration of Code Reasoning with AI Models}
%IDs:['67', '68']
"""

prompt_to_bib = """
你将会看到一段学术风格的综述片段，综述中引用了多篇学术论文。
请根据这些引用的信息，生成对应的BibTeX条目格式，并确保这些条目可以直接用于main.bib文件中。
每个BibTeX条目应包括以下信息：作者、标题、出版年份、会议或期刊名称、卷号（如果有）、期号（如果有）、页码（如果有）、DOI（如果有），以及其他相关的出版信息。
请确保所有信息准确无误且格式正确，不要生成任何其他说明性文字。
不需要```。

参考示例：
@inproceedings{ribeiro2016why,
  author    = {Ribeiro, Marco T{\'{u}}lio and
               Singh, Sameer and
               Guestrin, Carlos},
  title     = {"Why Should {I} Trust You?": Explaining the Predictions of Any Classifier},
  booktitle = {Proceedings of the Demonstrations Session of 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)},
  year      = {2016},
  url       = {https://doi.org/10.18653/v1/n16-3020},
  doi       = {10.18653/v1/n16-3020},
}

@inproceedings{lundberg2017aunified,
  author    = {Lundberg, Scott M. and
               Lee, Su{-}In},
  title     = {A Unified Approach to Interpreting Model Predictions},
  booktitle = {Advances in Neural Information Processing Systems (NIPS)},
  year      = {2017},
  url       = {https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html}
}

@inproceedings{chen2018learning,
  author    = {Chen, Jianbo and
               Song, Le and
               Wainwright, Martin J. and
               Jordan, Michael I.},
  title     = {Learning to Explain: An Information-Theoretic Perspective on Model
               Interpretation},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
  year      = {2018},
  url       = {http://proceedings.mlr.press/v80/chen18j.html}
}
"""

prompt_to_one_sentence = """
请把论文的摘要浓缩成一句话。不超过30词，英文回答。
"""

prompt_of_batches = r"""
你是一个写综述的科研人员，你需要仔细理解所提供的很多篇特定主题的论文题目和所给一句话文章描述,自主一步一步逐渐设计一个目录，来根据论文们的主要研究方向对这些论文进行分组。每一次更新目录，你大概率需要新建新的标题进行完善。

任务说明：
1.所有标题，子标题需要自行取标题。
2.考虑到一次性将所有论文摘要全部输入太长，所以分批处理。
3.每一次会向你提供：本次需要处理的论文批次、之前批次论文组成的临时目录。
4.需要根据本次提供的论文一句话描述将本次提供的论文ID添加到目录里面，你可能需要新建新的标题对目录进行完善。

任务要求：
1.每一个分组只需要有三部分：\section{}、%IDs:[]、%[over]。
2.论文编号汇总到注释%[]里面,格式为：%IDs:['1','2']。
3.每一组以%[over]结尾，方便后续操作。
4.要求每一篇论文都需要包含在内，论文可以被重复分组。
5.重点需要注意每个子标题下面尽量4-9篇论文.
6.对结果重新检查是否符合要求

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
"""

prompt_of_batches_830 = r"""
你是一个写综述的科研人员，你需要仔细理解所提供的很多篇特定主题的论文题目和所给一句话文章描述,自主一步一步逐渐设计一个目录，来根据论文们的主要研究方向对这些论文进行分组。

任务说明：
1.所有标题，子标题需要自行取标题。
2.考虑到一次性将所有论文摘要全部输入太长，所以分批处理。
3.每一次会向你提供：本次需要处理的论文批次、之前批次论文组成的临时目录。
4.需要根据本次提供的论文摘要将本次提供的论文ID添加到目录里面，你可能需要新建新的标题对目录进行完善。

任务要求：
1.每一个分组只需要有三部分：\section{}、%IDs:[]、%[over]。
2.论文编号汇总到注释%[]里面,格式为：%IDs:['1','2']。
3.每一组以%[over]结尾，方便后续操作。
4.要求每一篇论文都需要包含在内，论文可以被重复分组。
5.子标题下3到9篇论文合适。

目录结构参考更新示例：
之前所有批次的临时目录：
\title{Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey}

\section{Paradigm 1: Pre-Train then Fine-Tune}

\subsection{The Beginnings of the Paradigm Shift}
%IDs:['1', '2', '3', '4']
%[over]

\subsection{Modern Pre-Trained Language Models}
%IDs:['5', '6', '7']
%[over]

\subsection{Pre-Training Corpora} 
%IDs:['8', '9', '10']
%[over]
更新之后的输出目录：
\title{Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey}

\section{Paradigm 1: Pre-Train then Fine-Tune}

\subsection{The Beginnings of the Paradigm Shift}
%IDs:['1', '2', '3', '4','13']
%[over]

\subsection{Modern Pre-Trained Language Models}
%IDs:['5', '6', '7','11' ,'12']
%[over]

\subsection{Pre-Training Corpora} 
%IDs:['8', '9', '10']
%[over]

\section{Paradigm 2: Prompt-based Learning} 

\subsection{Learning from Instructions and Demonstrations}
%IDs:['14', '15', '16','17']
%[over]

\subsection{Template-based Learning} 
%IDs:['18', '19', '20']
%[over]
"""


prompt_final = """
你是一个写综述的科研人员，你需要仔细理解所提供的很多篇特定主题的论文题目和所给一句话文章描述,
自主一步一步逐渐设计一个目录，来根据论文们的主要研究方向对这些论文进行分组。
考虑到一次性将所有论文摘要全部输入太长，所以分批处理，现在所有目录迭代完成。
你需要最后根据所有论文的ID和标题，整合优化出来一个最后版本。

要求：
1.每一个分组只需要有三部分：\section{}、%IDs:[]、%[over]。
2.论文编号汇总到注释%[]里面,格式为：%IDs:['1','2']。
3.要求每一篇论文都需要包含在内，论文可以被重复分组。
4.子标题下3到9篇论文合适。
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
,以下是所有论文ID和标题ID: 1
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
\title{Recent Advances in Program-Aided Reasoning and Code Utilization in Language Models: A Survey}

\section{Program-Aided Reasoning and Computation in Language Models}

\subsection{Code Integration and Execution for Enhanced Reasoning} %IDs:['1', '4', '5', '7', '13', '17', '22', '23', '24', '26', '27'] %[over]

\subsection{Disentangling Computation from Reasoning} %IDs:['2', '14'] %[over]

\subsection{Self-Verification and Code-Based Problem Solving} %IDs:['3', '11', '42'] %[over]

\subsection{Hybrid Question Answering and Multilingual Structured Reasoning} %IDs:['8', '9', '20', '21'] %[over]

\subsection{Program Synthesis and Abstraction Discovery} %IDs:['6', '12', '16', '50'] %[over]

\subsection{Workflow Automation and LLM Integration} %IDs:['10', '18', '19'] %[over]

\subsection{Mathematical and Arithmetic Reasoning with LLMs} %IDs:['15', '13', '17'] %[over]

\section{Code Simulation, Reasoning, and Execution Challenges in LLMs}

\subsection{Simulation and Logic Code Execution} %IDs:['25', '22', '23'] %[over]

\subsection{Runtime Behavior and Code Reasoning Evaluation} %IDs:['26', '27', '28'] %[over]

\subsection{Collaborative and Hierarchical Code Generation} %IDs:['29', '30', '21'] %[over]

\section{LLM-Based Multi-Agent Collaboration and Software Development Frameworks}

\subsection{Multi-Agent Collaboration for Code Generation and Optimization} %IDs:['31', '38', '41', '46'] %[over]

\subsection{Agent Systems for Real-World Coding Challenges} %IDs:['32', '33', '34', '37', '47'] %[over]

\subsection{Frameworks for Software Development and Issue Resolution} %IDs:['35', '36', '39', '40', '44', '45', '49'] %[over]

\subsection{Innovative Approaches in Code Generation} %IDs:['43', '48'] %[over]

\section{Interactive and Feedback-Driven Code Generation}

\subsection{Test-Driven and Interactive Code Generation} %IDs:['51', '58', '62'] %[over]

\subsection{Natural Language and Self-Feedback for Code Generation} %IDs:['52', '53', '56', '61'] %[over]

\subsection{Self-Debugging and Fault-Aware Code Editing} %IDs:['54', '55', '66'] %[over]

\subsection{Iterative Refinement and Execution Feedback} %IDs:['57', '59', '60', '63'] %[over]

\subsection{Code Repair and Optimization Techniques} %IDs:['64', '65'] %[over]

\section{Code Generation from Requirements}

\subsection{Generating Code from Requirements with LLMs} %IDs:['67'] %[over]

\subsection{User Interaction and Support in Code Generation} %IDs:['68'] %[over]
"""































