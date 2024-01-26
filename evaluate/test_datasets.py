import datasets
from datasets import load_dataset,load_from_disk


CACHE_DIR= "/mnt/data/airaiot/LiangCheng/datasets/"
MODEL_DIR= "/mnt/data/airaiot/LiangCheng/model/"


# dataset = load_dataset("ms_marco",'v1.1',cache_dir = CACHE_DIR)


# dataset = datasets.load_from_disk("./datasets/ms_marco/v1.1/")
ds = load_dataset(path="./datasets/ms_marco")
print(len(ds))
print(ds)