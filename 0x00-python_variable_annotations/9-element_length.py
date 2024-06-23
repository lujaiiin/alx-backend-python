#!/usr/bin/env python3
'''
9-element_length.py
'''
from typing import List, Tuple, Iterable, Sequence

return_type = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> return_type:
    ''' returns a list of tuples have (list, len) as values '''
    return [(i, len(i)) for i in lst]
