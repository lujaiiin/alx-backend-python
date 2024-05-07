#!/usr/bin/env python3
"""modules"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """mm"""
    spawn = []
    delays = []
    for i in range(n):
        delayedt = task_wait_random(max_delay)
        delayedt.add_done_callback(lambda x: delays.append(x.result()))
        spawn.append(delayedt)

    for spawnn in spawn:
        await spawnn

    return delays
