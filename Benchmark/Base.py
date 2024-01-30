# -*- coding: UTF-8 -*-
"""
@Project:
@File   :Base
@Date   :2024/1/29
@Author :Oracle Yuan
"""

from LongContext import LongContextDataset
from typing import Optional,Callable

class Benchmark:
    def __init__(self,dataset:LongContextDataset,memoryLimitation:Optional[int],model:Callable,method):
        




