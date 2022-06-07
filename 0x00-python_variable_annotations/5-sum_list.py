#!/usr/bin/env python3
"""Suming list with anotations"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of float.
       Args:
           input_list (:obj:`list` of `float`): The list of numbers to be sumed.
       Returns:
           float: the sum of all floats from the list.
    """
    return reduce(lambda a, b: a + b, input_list)
