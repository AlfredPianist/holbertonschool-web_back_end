#!/usr/bin/env python3
"""Multiplier function returning Callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier.
       Args:
            multiplier: The multiplier.
       Returns:
            The function which multiplies multiplier to a float.
    """
    return lambda y: multiplier * y
