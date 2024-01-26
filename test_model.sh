export NUMEXPR_MAX_THREADS=64
export HF_ENDPOINT=https://hf-mirror.com
lm_eval --model hf \
    --use_cache './evaluate_cache/' \
    --model_args pretrained=mistralai/Mixtral-8x7B-Instruct-v0.1,cache_dir='./model_cache/' \
    --tasks coqa \
    --device cuda:0 \
    --batch_size 8 \
    --output_path './test_output/'