#!/usr/bin/env python3
"""modules"""
import asyncio
import random


async def wait_n(n: int, max_delay: int) -> list:
    """
     An asynchronous coroutine that spawns wait_random n times with the
     specified max_delay and returns a list of all the delays in
    """

    module_name = "0-basic_async_syntax"
    module = __import__(module_name)
    wait_random = module.wait_random

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays

if __name__ == "__main__":
    asyncio.run(wait_n())
