#!/usr/bin/python3

def bubble_sort(arr):
    for i in range(0, len(arr)):
        swapped = False

        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    arr = [ 5, 1, 4, 2, 8 ]

    bubble_sort(arr)

    print(arr)
