#!/usr/bin/env python3
"""Simple pagination module"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a page range from the dataset.
        Args:
            page: The first string.
            page_size: The second string.
        Returns:
            The sliced list with the initial and ending values.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        if start_idx > len(self.dataset()):
            return []
        return self.dataset()[start_idx:end_idx]
