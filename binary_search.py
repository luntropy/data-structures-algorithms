#!/usr/bin/python3

def binary_search(arr, left, right, x):
    if left <= right:
        m = left + (right - left) // 2

        if x == arr[m]:
            return m
        elif x > arr[m]:
            return binary_search(arr, m + 1, right, x)
        else:
            return binary_search(arr, left, m - 1, x)
    else:
        return -1

if __name__ == '__main__':
    arr = [ 2, 3, 4, 10, 40 ]
    x = 40
    y = -1

    index = binary_search(arr, 0, len(arr) - 1, x)

    print(index)
