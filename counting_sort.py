#!/usr/bin/python3

def counting_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    cnt_arr = [0 for i in range(0, range_of_elements)]
    for i in range(0, len(arr)):
        cnt_arr[arr[i] - min_element] += 1

    for i in range(1, len(cnt_arr)):
        cnt_arr[i] += cnt_arr[i - 1]

    res = [0 for i in range(0, len(arr))]
    for i in range(0, len(arr)):
        res[cnt_arr[arr[i] - min_element] - 1] = arr[i]
        cnt_arr[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        arr[i] = res[i]

if __name__ == '__main__':
    arr = [ 1, 4, 1, 2, 7, 5, 2, -1 ]

    counting_sort(arr)

    print(arr)
