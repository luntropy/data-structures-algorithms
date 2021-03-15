#!/usr/bin/python3

import sorting_algorithms as sort_alg
import searching_algorithms as search_alg

def compare(arr, res):
    if len(arr) != len(res):
        return False

    for i in range(len(arr)):
        if arr[i] != res[i]:
            return False

    return True

if __name__ == '__main__':
    # Sorting algorithms
    arr = [ 5, 1, -4, 4, 2, 6, 4 ]
    correct_res = [ -4, 1, 2, 4, 4, 5, 6 ]

    arr = [ 0.98, 0.6, 0.91, 0.19, 0.304, 0.50, 0.80, 0.48, 0.768, 0.48 ]
    correct_res = [ 0.19, 0.304, 0.48, 0.48, 0.5, 0.6, 0.768, 0.8, 0.91, 0.98 ]

    arr = [ 11, 9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68 ]
    correct_res = [ 0.6, 1.9, 3.04, 3.07, 4.8, 5.0, 7.68, 8.0, 9.8, 10.1, 11 ]

    arr = [ 170, 45, 75, 90, 802, 24, 2, 66 ]
    correct_res = [ 2, 24, 45, 66, 75, 90, 170, 802 ]

    # sort_alg.bubble_sort(arr)
    # sort_alg.selection_sort(arr)
    # sort_alg.insertion_sort(arr)
    # sort_alg.counting_sort(arr)
    # sort_alg.merge_sort(arr)
    # sort_alg.quick_sort(arr, 0, len(arr) - 1)
    # sort_alg.bucket_sort(arr)
    # sort_alg.bucket_sort_modified(arr)
    # sort_alg.radix_sort(arr)
    sort_alg.heap_sort(arr)

    if compare(arr, correct_res):
        print('Works!')
    else:
        print('Does not work!')
        print(arr)

    # Searching algorithms
    arr = [ 5, 1, -4, 4, 2, 6, 4 ]
    x = -4
    correct_idx_x = 2

    # idx = search_alg.linear_search(arr, x)

    arr = [ 1, 2, 3, 4, 4, 5, 6 ]
    x = 3
    correct_idx_x = 2

    idx = search_alg.binary_search(arr, 0, len(arr) - 1, x)
    # idx = search_alg.ternary_search(arr, 0, len(arr) - 1, x)

    if idx == correct_idx_x:
        print('Works!')
    else:
        print('Does not work!', idx)
