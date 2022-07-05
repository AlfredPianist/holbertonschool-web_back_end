#!/usr/bin/env python3
"""Utils unit tests"""

from parameterized import parameterized
import unittest
from unittest.mock import patch
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Class testing access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map's raise when nested_map is not a Mapping"""
        self.assertRaises(KeyError, utils.access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class testing get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json"""
        with patch('requests.get') as mocked:
            mocked.return_value.json.return_value = test_payload
            self.assertEqual(utils.get_json(test_url), test_payload)
            mocked.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class testing memoize """

    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, mocked.return_value)
            self.assertEqual(test_class.a_property, mocked.return_value)
            mocked.assert_called_once()
