# Load model directly
import torch
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1",cache_dir="../models/")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
# 定义问题和上下文
question = "What's the capital of France?"
context = "France is a country in Europe. Its capital is Paris."

# 使用分词器处理文本
inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")

# 使用模型进行预测
output = model(**inputs)

# # 获取答案的起始和结束位置
# answer_start = torch.argmax(output.start_logits)
# answer_end = torch.argmax(output.end_logits) + 1

# # 将 token ID 转换回文本
# answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))

# print(answer)

# 将问题和上下文合并为一条输入文本
input_text = context + " " + question

# 使用分词器处理文本
inputs = tokenizer.encode_plus(input_text, return_tensors="pt", max_length=512, truncation=True)

# 使用模型生成答案
output = model.generate(inputs['input_ids'], max_length=512, num_return_sequences=1)

# 将 token ID 转换回文本
answer = tokenizer.decode(output[0], skip_special_tokens=True)

print(answer)