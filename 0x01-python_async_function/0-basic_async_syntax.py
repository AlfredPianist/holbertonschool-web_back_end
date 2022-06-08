#!/usr/bin/env python3
"""Wait random coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes max_delay and returns a random value between 0 and max_delay.
       Args:
           max_delay: The maximum delay value.
       Returns:
           The random value calculated.
    """
    rand_val: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)
    return rand_val
