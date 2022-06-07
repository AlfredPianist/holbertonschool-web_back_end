#!/usr/bin/env python3
"""To kv"""
from typing import Union, Tuple
from functools import reduce


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a float with its second element squared.
       Args:
            k (str): A string
            v (int, float): A number
       Returns:
           (:obj:`tuple` of `str, float`): The float with the string and the
            float doubled.
    """
    return (k, v ** 2)
