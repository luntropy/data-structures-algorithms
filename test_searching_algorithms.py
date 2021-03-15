#!/usr/bin/python3

import unittest
from algorithms import searching_algorithms as search_alg

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.arr_not_sorted = [ 5, 1, -4, 4, 2, 6, 4 ]
        self.x = -4
        self.x_correct = 2

        self.y = 10
        self.y_correct = -1

        self.arr_sorted = [ 1, 2, 3, 4, 4, 5, 6 ]
        self.z = 1
        self.z_correct = 0

        self.k = -2
        self.k_correct = -1

    def test_linear_search(self):
        self.assertEqual(search_alg.linear_search(self.arr_not_sorted, self.x), self.x_correct)

        self.assertEqual(search_alg.linear_search(self.arr_not_sorted, self.y), self.y_correct)

        self.assertEqual(search_alg.linear_search(self.arr_sorted, self.z), self.z_correct)

        self.assertEqual(search_alg.linear_search(self.arr_sorted, self.k), self.k_correct)

    def test_binary_search(self):
        self.assertEqual(search_alg.binary_search(self.arr_sorted, 0, len(self.arr_sorted) - 1, self.z), self.z_correct)

        self.assertEqual(search_alg.binary_search(self.arr_sorted, 0, len(self.arr_sorted) - 1, self.k), self.k_correct)

    def test_ternary_search(self):
        self.assertEqual(search_alg.ternary_search(self.arr_sorted, 0, len(self.arr_sorted) - 1, self.z), self.z_correct)

        self.assertEqual(search_alg.ternary_search(self.arr_sorted, 0, len(self.arr_sorted) - 1, self.k), self.k_correct)

if __name__ == '__main__':
    unittest.main()
