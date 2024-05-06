#!/usr/bin/env python3
"""modules"""

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure time"""

    timez = time()
    run(wait_n(n, max_delay))
    timeo = time()
    elapsed = timeo - timez

    return elapsed / n
