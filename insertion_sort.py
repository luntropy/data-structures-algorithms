#!/usr/bin/python3

def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            # First we write the previous number on the key's position
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

if __name__ == '__main__':
    arr = [ 12, 11, 13, 5, 6 ]

    insertion_sort(arr)

    print(arr)
