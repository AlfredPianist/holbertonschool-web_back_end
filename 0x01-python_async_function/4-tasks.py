#!/usr/bin/env python3
"""Returns a task object calling wait_n"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Uses task_wait_random and outputs a list a random values
        Args:
            n: The number of times task_wait_random is called.
            max_delay: The maximum delay value.
        Returns:
            The list of sorted random values.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
