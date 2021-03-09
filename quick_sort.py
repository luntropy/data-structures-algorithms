#!/usr/bin/python3

import random

def partition_r(arr, low, high):
    r = random.randint(low, high)
    arr[r], arr[high] = arr[high], arr[r]

    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if (arr[j] <= pivot):
            i += 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition_r(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == '__main__':
    arr = [ 10, 80, 30, 90, 40, 50, 70 ]

    quick_sort(arr, 0, len(arr) - 1)

    print(arr)
