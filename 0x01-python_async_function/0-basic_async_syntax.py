#!/usr/bin/env python3
"""Modules"""


import asyncio
import random


async def wait_random(max_delay=10):
    """ asynchronous coroutine that takes in an intege
        ) named wait_random that waits for a random d
        float value) seconds and eventually returns it.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
