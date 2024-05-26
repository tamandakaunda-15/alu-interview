#!/usr/bin/python3
"""
Main file for testing using unittest
"""

import unittest
from minoperations import minOperations

class TestMinOperations(unittest.TestCase):
    """Test cases for the minOperations function."""

    def test_4_characters(self):
        """Test with n = 4."""
        self.assertEqual(minOperations(4), 4)

    def test_12_characters(self):
        """Test with n = 12."""
        self.assertEqual(minOperations(12), 7)

    # You can add more test methods as needed

if __name__ == '__main__':
    unittest.main()
