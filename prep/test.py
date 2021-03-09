#!/usr/bin/python3

import algorithms as alg

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

    # alg.bubble_sort(arr)
    # alg.selection_sort(arr)
    # alg.insertion_sort(arr)
    # alg.counting_sort(arr)
    # alg.merge_sort(arr)
    alg.quick_sort(arr, 0, len(arr) - 1)

    if compare(arr, correct_res):
        print('Works!')
    else:
        print('Does not work!')
        print(arr)

    # Searching algorithms
    arr = [ 5, 1, -4, 4, 2, 6, 4 ]
    x = -4
    correct_idx_x = 2

    # idx = alg.linear_search(arr, x)

    arr = [ 1, 2, 3, 4, 4, 5, 6 ]
    x = 3
    correct_idx_x = 2
    
    idx = alg.binary_search(arr, 0, len(arr) - 1, x)

    if idx == correct_idx_x:
        print('Works!')
    else:
        print('Does not work!', idx)
