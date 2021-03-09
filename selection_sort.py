#!/usr/bin/python3

def selection_sort(arr):
    for i in range(0, len(arr)):
        idx_min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min]:
                idx_min = j

        temp = arr[idx_min]
        arr[idx_min] = arr[i]
        arr[i] = temp

if __name__ == '__main__':
    arr = [ 64, 25, 12, 22, 11 ]

    selection_sort(arr)

    print(arr)
