import random

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

# TC: O(n*log(n)), SC: O(n*log(n))
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

# TC: O(n*log(n)), SC: O(log(n))
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
