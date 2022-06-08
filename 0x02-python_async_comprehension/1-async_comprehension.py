#!/usr/bin/env python3
"""Random generator coroutine"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine looping 10 times collecting 10 floats asynchronously
    using the async generator function
    """
    return [num async for num in async_generator()]
