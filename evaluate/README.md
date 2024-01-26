使用开源测试框架：`lm-evaluation-harness`

[lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/main)

对llm进行评测：

- 评测模型：`mistralai/Mixtral-8x7B-Instruct-v0.1`

- 评测任务：`coqa`
  - [CoQA: A Conversational Question Answering Challenge (stanfordnlp.github.io)](https://stanfordnlp.github.io/coqa/)

- 评测方式：

````
# 主目录下
# 安装lm-evaluation-harness
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
# 使用脚本评测
./test_model.sh
````
