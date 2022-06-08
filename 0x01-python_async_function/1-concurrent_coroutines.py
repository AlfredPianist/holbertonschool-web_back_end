#!/usr/bin/env python3
"""Wait random coroutine"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Uses wait_random and outputs a list a random values.
       Args:
           n: The number of times to execute wait_random.
           max_delay: The maximum delay value.
       Returns:
           The list of the random values calculated.
    """
    values = []
    for _ in range(n):
        values.append(await wait_random(max_delay))
    return sorted(values)
