#!/usr/bin/env python3
"""m"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """jj"""
    return lambda n: n * multiplier
