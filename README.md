# 从零开始理解大模型

这个目录整理了 **「从零开始理解大模型」** 系列文章与配套代码。

## 系列说明

- 正篇 10 篇：从“下一个词预测”一路讲到 Agent
- 番外篇 6 篇：补充多模态、GPU、API 计费、思考模式、MoE 与算子相关主题
- 每篇文章尽量配有可运行示例，方便边读边验证

## 文章目录

### 正篇

1. [从零开始理解大模型（一）：一切从"猜下一个词"开始](./llm-01-next-token.md)
2. [从零开始理解大模型（二）：Token——大模型眼中的"字"长什么样](./llm-02-token.md)
3. [从零开始理解大模型（三）：向量与 Embedding——把文字变成数学](./llm-03-embedding.md)
4. [从零开始理解大模型（四）：Attention——大模型的"阅读理解"机制](./llm-04-attention.md)
5. [从零开始理解大模型（五）：Transformer 全景——积木怎么搭成大厦](./llm-05-transformer.md)
6. [从零开始理解大模型（六）：训练——70 亿个参数是怎么"学"出来的](./llm-06-training.md)
7. [从零开始理解大模型（七）：推理——你按下回车后的这一秒发生了什么](./llm-07-inference.md)
8. [从零开始理解大模型（八）：上下文窗口——大模型的"工作记忆"到底有多大？](./llm-08-context-window.md)
9. [从零开始理解大模型（九）：Scaling Law——为什么“大力出奇迹”有效](./llm-09-scaling-law.md)
10. [从零开始理解大模型（十）：从大模型到 Agent——下一个词预测如何长出手脚](./llm-10-agent.md)

### 番外篇

11. [从零开始理解大模型（番外篇）：多模态——大模型是怎么“看懂”图片的](./llm-11-multimodal.md)
12. [从零开始理解大模型（番外篇二）：为什么大模型离不开 GPU](./llm-12-gpu.md)
13. [从零开始理解大模型（番外篇三）：为什么用 Token 计费？为什么输出比输入贵？](./llm-13-token-pricing.md)
14. [从零开始理解大模型（番外篇四）：思考模式和非思考模式到底有什么区别？](./llm-14-thinking-mode.md)
15. [从零开始理解大模型（番外篇五）：DeepSeek V4 Pro 总参数 1.6T，激活参数 49B——这到底是什么意思？](./llm-15-moe.md)
16. [从零开始理解大模型（番外篇六）：什么是算子？大模型里的“最小施工单位”](./llm-16-operators.md)

## 精读笔记

对应 16 篇文章的逐篇精读笔记：

- [精读笔记索引](./精读笔记/README.md)
- [01 — 猜下一个词](./精读笔记/01-猜下一个词.md)
- [02 — Token](./精读笔记/02-Token.md)
- [03 — Embedding](./精读笔记/03-Embedding.md)
- [04 — Attention](./精读笔记/04-Attention.md)
- [05 — Transformer](./精读笔记/05-Transformer.md)
- [06 — 训练](./精读笔记/06-训练.md)
- [07 — 推理与 KV-Cache](./精读笔记/07-推理与KV-Cache.md)
- [08 — 上下文窗口](./精读笔记/08-上下文窗口.md)
- [09 — Scaling Law](./精读笔记/09-Scaling-Law.md)
- [10 — Agent](./精读笔记/10-Agent.md)
- [11 — 多模态](./精读笔记/11-多模态.md)
- [12 — GPU](./精读笔记/12-GPU.md)
- [13 — Token 计费](./精读笔记/13-Token计费.md)
- [14 — 思考模式](./精读笔记/14-思考模式.md)
- [15 — MoE](./精读笔记/15-MoE.md)
- [16 — 算子](./精读笔记/16-算子.md)
- [精读笔记合订本](./从零开始理解大模型-精读笔记合订本.md)

## 配套代码

Python 示例脚本已统一放在 [`script/`](./script/README.md) 目录：

- [analogy.py](./script/analogy.py)
- [attention.py](./script/attention.py)
- [bpe_demo.py](./script/bpe_demo.py)
- [context_embedding.py](./script/context_embedding.py)
- [context_window.py](./script/context_window.py)
- [embedding.py](./script/embedding.py)
- [fetch.py](./script/fetch.py)
- [generate.py](./script/generate.py)
- [inference.py](./script/inference.py)
- [multi_head.py](./script/multi_head.py)
- [predict.py](./script/predict.py)
- [scaling_law.py](./script/scaling_law.py)
- [tiny_agent.py](./script/tiny_agent.py)
- [token_cost.py](./script/token_cost.py)
- [tokenizer_demo.py](./script/tokenizer_demo.py)
- [train_tiny.py](./script/train_tiny.py)
- [transformer_anatomy.py](./script/transformer_anatomy.py)
- [visualize.py](./script/visualize.py)

可按各篇文章中的说明分别运行。
