# Load model directly
import torch
import os
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2",cache_dir="model/")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
# 定义问题和上下文
question = "What's the capital of France?"
context = "France is a country in Europe. Its capital is Paris."

# 使用分词器处理文本
inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")

# 使用模型进行预测
output = model(**inputs)

# 获取答案的起始和结束位置
answer_start = torch.argmax(output.start_logits)
answer_end = torch.argmax(output.end_logits) + 1

# 将 token ID 转换回文本
answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))

print(answer)