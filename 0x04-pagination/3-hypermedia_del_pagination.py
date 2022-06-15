#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Gets a dictionary with some pagination information from indexed
        dictionary.
        Args:
            index: The current index.
            page_size: The page size.
        Returns:
            The dictionary with the pagination information.
        """
        assert type(index) == int and index >= 0
        assert type(page_size) == int and page_size > 0
        assert 0 <= index < len(self.indexed_dataset())
        indexed_keys = sorted(list(self.indexed_dataset().keys()))
        begin_index = index
        try:
            begin_index = indexed_keys.index(index)
        except ValueError:
            pass
        indexed_keys_slice = indexed_keys[begin_index:begin_index + page_size]
        data = [self.indexed_dataset()[key] for key in indexed_keys_slice]
        return {
            "index": index,
            "next_index": indexed_keys_slice[-1] + 1,
            "page_size": page_size,
            "data": data
        }
