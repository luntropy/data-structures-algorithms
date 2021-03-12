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

# TC: O(n * k / d), SC: O(n + 2^d)
def radix_sort(arr):
    max_element = max(arr)

    exp = 1
    while math.floor(max_element / exp) > 0:
        radix_counting_sort(arr, exp)
        exp *= 10

# Part of the heap sort algorithm
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

# TC: O(n * log(n)), SC: O(1)
def heap_sort(arr):
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Part of DFS
# TC: O(b^m), SC: O(b * m)
def dfs_until(v, visited, graph):
    visited.add(v)
    print(v, end = ' ')

    for neighbour in graph[v]:
        if neighbour not in visited:
            dfs_until(neighbour, visited, graph)

def dfs(graph, s):
    visited = set()
    dfs_until(s, visited, graph)

def dfs_stack(graph, s):
    visited = set()
    stack = []

    stack.append(s)

    while stack:
        v = stack.pop()

        if v not in visited:
            print(v, end = ' ')
            visited.add(v)

            for c in graph[v]:
                stack.append(c)

# TC: O(b^(d + 1)), SC: O(b^(d + 1))
def bfs(graph, s):
    visited = set()
    queue = []

    queue.append(s)

    while queue:
        v = queue.pop(0)

        if v not in visited:
            print(v, end = ' ')
            visited.add(v)

            for c in graph[v]:
                queue.append(c)

def preorder(root):
    if root:
        print(root.value, end = ' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end = ' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end = ' ')
