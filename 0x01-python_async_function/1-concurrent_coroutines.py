#!/usr/bin/python3
"""modules"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
     An asynchronous coroutine that spawns wait_random n times with the
     specified max_delay and returns a list of all the delays in
    """

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
