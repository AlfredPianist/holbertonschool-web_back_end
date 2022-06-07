#!/usr/bin/env python3
"""Typing more generalized inputs and output"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence.
     Args:
          lst: The list.
     Returns:
          The first element of the list. Otherwise None.
     """
    if lst:
        return lst[0]
    else:
        return None
