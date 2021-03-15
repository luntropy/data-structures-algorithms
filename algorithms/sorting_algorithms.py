#!/usr/bin/python3

import random
import math

# TC: O(n^2), SC: O(1)
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False

        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            return

# TC: O(n^2), SC: O(1)
def selection_sort(arr):
    for i in range(len(arr)):
        idx_min_el = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min_el]:
                idx_min_el = j

        arr[i], arr[idx_min_el] = arr[idx_min_el], arr[i]

# TC: O(n^2), SC: O(1)
def insertion_sort(arr):
    for i in range(len(arr)):
        value = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value

# TC: O(n + k), SC: O(n + k)
def counting_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_elements = max_element - min_element + 1

    cnt_arr = [0 for _ in range(range_elements)]
    for i in range(len(arr)):
        cnt_arr[arr[i] - min_element] += 1

    for i in range(1, len(cnt_arr)):
        cnt_arr[i] += cnt_arr[i - 1]

    res = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        res[cnt_arr[arr[i] - min_element] - 1] = arr[i]
        cnt_arr[arr[i] - min_element] -= 1

    for i in range(len(arr)):
        arr[i] = res[i]

# TC: O(n * log(n)), SC: O(n * log(n))
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        arr_left = arr[:middle]
        arr_right = arr[middle:]

        merge_sort(arr_left)
        merge_sort(arr_right)

        i = j = k = 0
        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] <= arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
                k += 1
            else:
                arr[k] = arr_right[j]
                j += 1
                k += 1

        while i < len(arr_left):
            arr[k] = arr_left[i]
            i += 1
            k += 1

        while j < len(arr_right):
            arr[k] = arr_right[j]
            j += 1
            k += 1

# Part of quick sort
# TC: O(n * log(n)), SC: O(log(n))
def random_partition(arr, low, high):
    rand_idx = random.randint(low, high)

    arr[high], arr[rand_idx] = arr[rand_idx], arr[high]

    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]

    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = random_partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# TC: O(n + k), SC: O(n + k)
def bucket_sort(arr):
    bucket_cnt = len(arr)
    buckets = [[] for _ in range(bucket_cnt)]

    for i in arr:
        idx = int(bucket_cnt * i)
        buckets[idx].append(i)

    for bucket in buckets:
        if len(bucket):
            insertion_sort(bucket)

    j = 0
    for bucket in buckets:
        for element in bucket:
            arr[j] = element
            j += 1

# Bucket sort, modified to work with integers
def bucket_sort_modified(arr):
    max_element = max(arr)
    min_element = min(arr)

    buckets_cnt = len(arr)
    buckets = [[] for _ in range(buckets_cnt)]

    range_elements = (max_element - min_element) / buckets_cnt

    for el in arr:
        diff = (el - min_element) / range_elements - int(el - min_element / range_elements)

        if diff == 0 and el != min_element:
            buckets[int((el - min_element) / range_elements) - 1].append(el)
        else:
            buckets[int(el - min_element / range_elements)].append(el)

    for bucket in buckets:
        if len(bucket):
            insertion_sort(bucket)

    j = 0
    for bucket in buckets:
        for i in bucket:
            arr[j] = i
            j += 1

# Counting sort for the radix sort algorithm
# TC: O(n * k / d), SC: O(n + 2^d)
def radix_counting_sort(arr, exp):
    counting_arr = [0 for _ in range(10)]

    for i in arr:
        index = i / exp
        counting_arr[int(index % 10)] += 1

    for i in range(0, len(counting_arr) - 1):
        counting_arr[i + 1] += counting_arr[i]

    result_arr = [0 for _ in range(len(arr))]

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] / exp

        result_arr[counting_arr[int(index % 10)] - 1] = arr[i]
        counting_arr[int(index % 10)] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = result_arr[i]

def radix_sort(arr):
    max_element = max(arr)

    exp = 1
    while math.floor(max_element / exp) > 0:
        radix_counting_sort(arr, exp)
        exp *= 10

# Part of the heap sort algorithm
# TC: O(n * log(n)), SC: O(1)
def heapify(arr, n, i):
    idx_largest = i
    idx_left = 2 * i + 1
    idx_right = 2 * i + 2

    if idx_left < n and arr[idx_left] > arr[idx_largest]:
        idx_largest = idx_left

    if idx_right < n and arr[idx_right] > arr[idx_largest]:
        idx_largest = idx_right

    if idx_largest != i:
        arr[idx_largest], arr[i] = arr[i], arr[idx_largest]
        heapify(arr, n, idx_largest)

def heap_sort(arr):
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
