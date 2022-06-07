#!/usr/bin/env python3
"""Typing a function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples.
     Args:
          lst: The element.
     Returns:
          The length of said element.
     """
    return [(i, len(i)) for i in lst]
