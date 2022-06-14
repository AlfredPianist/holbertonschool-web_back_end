#!/usr/bin/env python3
"""Return tuple with start and end indices"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the index range given the current page and the page size.
       Args:
           page: The first string.
           page_size: The second string.
       Returns:
           The tuple with start and end indices.
    """
    start_idx: int = page_size * (page - 1)
    end_idx: int = start_idx + page_size
    return (start_idx, end_idx)
