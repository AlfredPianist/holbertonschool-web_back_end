#!/usr/bin/env python3
"""Mixed list with anotations"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats and ints.
       Args:
           input_list (:obj:`list` of `int, float`): The list of numbers to be\
               sumed.
       Returns:
           float: the sum of all floats from the list.
    """
    return reduce(lambda a, b: a + b, mxd_lst)
