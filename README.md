# Data structures & Algorithms
## Purpose


## Bubble sort
Time complexity: O(n^2)\
Space complexity: O(1)

- The worst case occurs when the array is reverse sorted.

### Optimizations
- Optimization: added boolean variable 'swapped' to check if any swap occurred on the first run, if it is false then the array is already sorted.
- In case of sorted array the time complexity is O(n) with the optimization.
- On each run one more number is in it is correct position.

### Notes
- On each iteration there is one element that found its position - the biggest number.
- The second iteration must be dependent on 'i'. No point in trying to sort elements that are already sorted.

## Selection sort
Time complexity: O(n^2)\
Space complexity: O(1)

### Notes
- Finds the index of the minimum element.
- Similarly to the bubble sort on each iteration there is one element that found its position, but it is the smallest number not the biggest.
- Second iteration must be dependent on 'i' otherwise it considers the already ordered smallest elements.

## Insertion sort
Time complexity: O(n^2)\
Space complexity: O(1)

### Notes
- Checks if a key element has bigger elements before it.
- Each element overwrites its next element starting from one element before the given key element until the key element finds its correct position.

## Counting sort
Time complexity: O(n + k)\
Space complexity: O(n + k)\
k - the range of the input

### Notes
- Count the numbers in separate array where the number identifies the position in the new array.
- For each element position, summarize the values of the previous elements.
- Order the elements in resulting array.

- The position of a given element (arr[i]) in the resulting array (res_arr) is the result from the counting array (cnt_arr) at the position of the element's value minus one:\
`res_arr[cnt_arr[arr[i]] - 1] = arr[i]`

#### Optimizations to work with negative values
- We need to take into consideration that the range is not between positive numbers.
- That is why we get the maximum and minimum element from the array and calculate the range:\
`range = max_element - min_element + 1`

- The counting array is generated using that range.
- When the elements are counted their position is based on the element's value minus the minimum element in the array:\
`counting[arr[i] - min_element] += 1`

## Merge sort
Time complexity: O(n * log(n))\
Space complexity: O(n * log(n))

- Divides the array in two halves and takes linear time to merge.

### Notes
- If the length of the array is more than one then we can call recursively merge sort.
- Use while loops to merge two sorted arrays.

## Quick sort
Time complexity: O(n * log(n))\
Space complexity: O(log(n))

- Traversing the array when positioning the elements compared to the pivot.
- Recursively traversing smaller parts of the array.

### Notes
- If the length of the array is one, return the array.
- Proceed if low < high.
- Choose pivot 'x' (randomly) and sort compared to the pivot by placing the values less than 'x' in its left side and the values, bigger than 'x' on its right side.
- Position all the elements before repositioning the pivot in its correct position.
- The partition function must return the index of positioned 'x'.\
`partition(arr, low, high)`
- When calling recursively quick sort the pivot should be excluded:\
`quick_sort(arr, left, pi - 1)`\
`quick_sort(arr, pi - 1, right)`
- All the time we work with the same array but in different parts of it and we are just swapping positions.
- The partitioning does not care to order them perfectly, it just positions them correctly compared to the pivot.

### Optimizations
- The partition always takes the pivot at high index. When randomizing we use another function that switches the randomly chosen element with the element in the high index.

## Bucket sort
Time complexity: O(n + k)\
Space complexity: O(n + k)

- Worst case time complexity: O(n^2)

### Notes
- Works for numbers between 0 and 1.
- Does not work for count of the buckets > 10.
- Separate numbers in buckets, sort each bucket (using insertion sort) and then merge them.

### Optimizations
- Can be modified to work with integers.
- The count of the buckets can be the length of the array.

## Radix sort
Time complexity: O(d * (n + b))\
Space complexity: O(n + 2^d)

### Notes
- The counting sort traverses the array backwards (when assigning the numbers to the output array) because it needs to preserve the ordering, established by previous calls to counting sorts (needs to be stable).
- Example:\
Input: [ 643, 613 ]\
Order by second digit -> [ 613, 643 ]. If we traverse forward the first index to assign 613 will be 5 and then 4 for 643, so we will have [ 643, 613 ], but if we traverse backwards we will preserve the order -> [ 613, 643 ].

- One algorithm is stable if the order of the elements is preserved.

## Heap sort
Time complexity: O(n * log(n))\
Space complexity: O(1)

- Building the heap has time complexity O(n).

### Notes
- We build the max-heap backwards because in order for it to work it assumes that each subtree is already max-heap.
- For ordering of the array we move the root (the maximum element in the max-heap) in the last index then we resize the heap with one and reorder it to be max-heap again. It is repeated until one element is left in the heap.

## Linear search
Time complexity: O(n)\
Space complexity: O(1)

## Binary search
Time complexity: O(log(n))\
Space complexity: O(1)\

! Works only for sorted arrays.

### Notes
- If left <= high, proceed.
- Middle position calculation:\
`middle = left + (right - left) // 2`
- Check if the element at the middle (arr[middle]) of the array is 'x'. If it is not, call the binary searched.
- If  x < arr[middle], then call the binary search for the left side of the array.\
`binary_search(arr, left, middle - 1, x)`
- If x > arr[middle], then call binary search for the right side of the array:\
`binary_search(arr, middle + 1, right, x)`
- Exclude the middle position since we already know that is is not 'x'.

## Ternary search
Time complexity: O(log3(n))\
Space complexity: O(1)\

! Works only for sorted arrays.

### Notes
- Same as binary search but we separate the array in three parts.

## DFS
Time complexity: O(b^m)\
Space complexity: O(b * m)

## BFS
Time complexity: O(b^(d + 1))\
Space complexity: O(b^(d + 1))
