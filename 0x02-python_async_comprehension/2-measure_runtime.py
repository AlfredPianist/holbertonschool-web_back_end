#!/usr/bin/env python3
"""Random generator coroutine"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine measuring the time taken for async comprehension to run
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time: float = time.perf_counter()
    return end_time - start_time
