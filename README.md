使用开源测试框架：`lm-evaluation-harness`

[lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/main)

对llm进行评测：

- 评测模型：`mistralai/Mixtral-8x7B-Instruct-v0.1`

- 评测任务：`coqa`
  - [CoQA: A Conversational Question Answering Challenge (stanfordnlp.github.io)](https://stanfordnlp.github.io/coqa/)

- 评测方式：

````
# 安装lm-evaluation-harness
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
# 使用脚本评测
./test_model.sh
````

目录结构：

```
.
├── datasets				--数据集目录
├── evaluate_cache			--测试缓存目录
├── lm-evaluation-harness	--评测工具目录
├── model_cache				--模型缓存目录
├── test_datasets.py		--简易测试数据脚本
├── test_model.py			--简易测试模型脚本
├── test_model.sh			--测试模型脚本
└── test_output				--测试输出目录
```



