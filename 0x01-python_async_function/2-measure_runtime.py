#!/usr/bin/env python3
"""Measuring time of concurrent coroutine"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures elapsed time used by the wait_n module.
       Args:
           n: The number of times to execute wait_random.
           max_delay: The maximum delay value.
       Returns:
           The mean time of all executions.
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()
    return (end_time - start_time) / n
