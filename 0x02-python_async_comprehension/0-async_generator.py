#!/usr/bin/env python3
"""Random generator coroutine"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine looping 10 times, waits asynchronously 1 second
    and yield a random number from 0 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
