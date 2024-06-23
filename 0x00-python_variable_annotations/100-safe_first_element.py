#!/usr/bin/env python3
"""haha"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """safe"""
    if lst:
        return lst[0]
    else:
        return None
