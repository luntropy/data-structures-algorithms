#!/usr/bin/python3

# TC: O(n), SC: O(1)
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

# TC: O(log(n)), SC: O(1)
def binary_search(arr, left, right, x):
    if left <= right:
        middle = left + (right - left) // 2

        if x == arr[middle]:
            return middle
        elif x < arr[middle]:
            return binary_search(arr, left, middle - 1, x)
        else:
            return binary_search(arr, middle + 1, right, x)
    else:
        return -1

# TC: O(log3(n)), SC: O(1)
def ternary_search(arr, left, right, x):
    if left <= right:
        middle_first = left + (right - left) // 3
        middle_second = right - (right - left) // 3

        if x == arr[middle_first]:
            return middle_first
        elif x == arr[middle_second]:
            return middle_second
        elif x < arr[middle_first]:
            return ternary_search(arr, left, middle_first - 1, x)
        elif x > arr[middle_second]:
            return ternary_search(arr, middle_second + 1, right, x)
        else:
            return ternary_search(arr, middle_first + 1, middle_second - 1, x)

    return -1
