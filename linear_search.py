#!/usr/bin/python3

def linear_search(x, arr):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i

    return -1

if __name__ == '__main__':
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10

    index = linear_search(x, arr)

    print(index)
