#!/usr/bin/env python3
"""mod"""
from functools import reduce
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """sum"""
    return reduce(lambda a, b: a + b, input_list)
