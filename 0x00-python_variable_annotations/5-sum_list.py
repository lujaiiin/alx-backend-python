#!/usr/bin/env python3
"""us"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum"""
    return reduce(lambda a, b: a + b, input_list)
