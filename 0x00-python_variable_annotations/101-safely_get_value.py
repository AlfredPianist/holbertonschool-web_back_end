#!/usr/bin/env python3
"""Typing a dictionary return"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns a value of a mapping object.
    Args:
        dct: The mapping.
        key: A key to search for in the mapping.
        default: The default value to search.
    Returns:
        The value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
