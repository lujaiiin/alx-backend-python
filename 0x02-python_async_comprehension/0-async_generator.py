#!/usr/bin/env python3
""" modules """

import random
import asyncio
from typing import List


async def async_generator() -> List[float, None, None]:
    """ async generator function """

    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
