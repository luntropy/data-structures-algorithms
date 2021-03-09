#!/usr/bin/python3

def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        arr_left = arr[:m]
        arr_right = arr[m:]

        merge_sort(arr_left)
        merge_sort(arr_right)

        i = j = k = 0
        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] <= arr_right[j]:
                arr[k] = arr_left[i]
                k += 1
                i += 1

            elif arr_left[i] > arr_right[j]:
                arr[k] = arr_right[j]
                k += 1
                j += 1

        while i < len(arr_left):
            arr[k] = arr_left[i]
            k += 1
            i += 1

        while j < len(arr_right):
            arr[k] = arr_right[j]
            k += 1
            j += 1

if __name__ == '__main__':
    arr = [ 12, 11, 13, 5, 6, 7 ]

    merge_sort(arr)

    print(arr)
