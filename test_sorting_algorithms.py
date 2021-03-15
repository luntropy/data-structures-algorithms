#!/usr/bin/python3

import unittest
from algorithms import sorting_algorithms as sort_alg

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.arr_positive = [ 170, 45, 75, 90, 802, 24, 2, 66 ]
        self.arr_positive_correct = [ 2, 24, 45, 66, 75, 90, 170, 802 ]

        self.arr_negative = [ -5, -1, -4, -4, -2, -6, -4 ]
        self.arr_negative_correct = [ -6, -5, -4, -4, -4, -2, -1 ]

        self.arr_positive_negative = [ 5, 1, -4, 4, 2, 6, 4 ]
        self.arr_positive_negative_correct = [ -4, 1, 2, 4, 4, 5, 6 ]

        self.arr_decimal = [ 0.98, 0.6, 0.91, 0.19, 0.304, 0.50, 0.80, 0.48, 0.768, 0.48 ]
        self.arr_decimal_correct = [ 0.19, 0.304, 0.48, 0.48, 0.5, 0.6, 0.768, 0.8, 0.91, 0.98 ]

        self.arr_decimal_int = [ 11, 9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68 ]
        self.arr_decimal_int_correct = [ 0.6, 1.9, 3.04, 3.07, 4.8, 5.0, 7.68, 8.0, 9.8, 10.1, 11 ]

        self.arr_sorted = [ -799056, -661009, -562222, -368704, -106617, 10521, 72268, 126495, 803913, 856353 ]
        self.arr_sorted_correct = [ -799056, -661009, -562222, -368704, -106617, 10521, 72268, 126495, 803913, 856353 ]

    def test_bubble_sort(self):
        sort_alg.bubble_sort(self.arr_positive)
        self.assertListEqual(self.arr_positive, self.arr_positive_correct)

        sort_alg.bubble_sort(self.arr_negative)
        self.assertListEqual(self.arr_negative, self.arr_negative_correct)

        sort_alg.bubble_sort(self.arr_positive_negative)
        self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

        sort_alg.bubble_sort(self.arr_decimal)
        self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

        sort_alg.bubble_sort(self.arr_decimal_int)
        self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

        sort_alg.bubble_sort(self.arr_sorted)
        self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

    def test_selection_sort(self):
            sort_alg.selection_sort(self.arr_positive)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

            sort_alg.selection_sort(self.arr_negative)
            self.assertListEqual(self.arr_negative, self.arr_negative_correct)

            sort_alg.selection_sort(self.arr_positive_negative)
            self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

            sort_alg.selection_sort(self.arr_decimal)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

            sort_alg.selection_sort(self.arr_decimal_int)
            self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

            sort_alg.selection_sort(self.arr_sorted)
            self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

    def test_insertion_sort(self):
            sort_alg.insertion_sort(self.arr_positive)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

            sort_alg.insertion_sort(self.arr_negative)
            self.assertListEqual(self.arr_negative, self.arr_negative_correct)

            sort_alg.insertion_sort(self.arr_positive_negative)
            self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

            sort_alg.insertion_sort(self.arr_decimal)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

            sort_alg.insertion_sort(self.arr_decimal_int)
            self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

            sort_alg.insertion_sort(self.arr_sorted)
            self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

    def test_counting_sort(self):
            sort_alg.counting_sort(self.arr_positive)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

            sort_alg.counting_sort(self.arr_negative)
            self.assertListEqual(self.arr_negative, self.arr_negative_correct)

            sort_alg.counting_sort(self.arr_positive_negative)
            self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

            sort_alg.counting_sort(self.arr_sorted)
            self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

    def test_merge_sort(self):
            sort_alg.merge_sort(self.arr_positive)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

            sort_alg.merge_sort(self.arr_negative)
            self.assertListEqual(self.arr_negative, self.arr_negative_correct)

            sort_alg.merge_sort(self.arr_positive_negative)
            self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

            sort_alg.merge_sort(self.arr_decimal)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

            sort_alg.merge_sort(self.arr_decimal_int)
            self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

            sort_alg.merge_sort(self.arr_sorted)
            self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

    def test_quick_sort(self):
            sort_alg.quick_sort(self.arr_positive, 0, len(self.arr_positive) - 1)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

            sort_alg.quick_sort(self.arr_negative, 0, len(self.arr_negative) - 1)
            self.assertListEqual(self.arr_negative, self.arr_negative_correct)

            sort_alg.quick_sort(self.arr_positive_negative, 0, len(self.arr_positive_negative) - 1)
            self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

            sort_alg.quick_sort(self.arr_decimal, 0, len(self.arr_decimal) - 1)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

            sort_alg.quick_sort(self.arr_decimal_int, 0, len(self.arr_decimal_int) - 1)
            self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

            sort_alg.quick_sort(self.arr_sorted, 0, len(self.arr_sorted) - 1)
            self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

    def test_bucket_sort(self):
            sort_alg.bucket_sort(self.arr_decimal)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

    def test_bucket_sort_modified(self):
            sort_alg.bucket_sort_modified(self.arr_decimal)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

            sort_alg.bucket_sort_modified(self.arr_decimal_int)
            self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

    def test_radix_sort(self):
            sort_alg.radix_sort(self.arr_positive)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

    def test_heap_sort(self):
            sort_alg.heap_sort(self.arr_positive)
            self.assertListEqual(self.arr_positive, self.arr_positive_correct)

            sort_alg.heap_sort(self.arr_negative)
            self.assertListEqual(self.arr_negative, self.arr_negative_correct)

            sort_alg.heap_sort(self.arr_positive_negative)
            self.assertListEqual(self.arr_positive_negative, self.arr_positive_negative_correct)

            sort_alg.heap_sort(self.arr_decimal)
            self.assertListEqual(self.arr_decimal, self.arr_decimal_correct)

            sort_alg.heap_sort(self.arr_decimal_int)
            self.assertListEqual(self.arr_decimal_int, self.arr_decimal_int_correct)

            sort_alg.heap_sort(self.arr_sorted)
            self.assertListEqual(self.arr_sorted, self.arr_sorted_correct)

if __name__ == '__main__':
    unittest.main()
