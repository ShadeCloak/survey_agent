prompt_to_catalogue = """
你是一个写综述的科研人员，你需要仔细理解所提供的特定主题的论文摘要,自主设计一个目录，并根据论文们的主要研究方向对这些论文进行分组。
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




































