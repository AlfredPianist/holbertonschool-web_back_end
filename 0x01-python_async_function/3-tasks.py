#!/usr/bin/env python3
"""Returns a task object"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio Task object with a delay
       Args:
           max_delay: The maximum delay value.
       Returns:
           The asyncio Task object.
    """
    return asyncio.Task(wait_random(max_delay))
