#!/usr/bin/env python3
"""Using mypy to check types of a Python module"""
from typing import List, Tuple, Any, cast


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a value of a mapping object.
    Args:
        lst: A list.
        factor: A number.
    Returns:
        The value.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(cast(Tuple, array))

zoom_3x = zoom_array(cast(Tuple, array), cast(int, 3.0))
