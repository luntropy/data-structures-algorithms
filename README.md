# Algorithms

## Bubble sort
Time complexity: O(n^2)
Space complexity: O(1)

### Optimizations
- Optimization: added boolean variable 'swapped' to check if any swap occurred on the first run, if it is false then the array is already sorted.
- In case of sorted array the time complexity is O(n) with the optimization.
- On each run one more number is in it is correct position.

- The worst case occurs when the array is reverse sorted.

### Notes
- On each iteration there is one element that found its position - the biggest number.
- The second iteration must be dependent on 'i'. No point in trying to sort elements that are already sorted.

## Selection sort
Time complexity: O(n^2)
Space complexity: O(1)

### Notes
- Finds the index of the minimum element.
- Similarly to the bubble sort on each iteration there is one element that found its position, but it is the smallest number not the biggest.
- Second iteration must be dependent on 'i' otherwise it considers the already ordered smallest elements.

## Insertion sort
Time complexity: O(n^2)
Space complexity: O(1)

### Notes
- Checks if a key element has bigger elements before it.
- Each element overwrites its next element starting from one element before the given key element until the key element finds its correct position.

## Counting sort
Time complexity: O(n + k)
Space complexity: O(n + k)
k - the range of the input

### Notes
- Count the numbers in separate array where the number identifies the position in the new array.
- For each element position, summarize the values of the previous elements.
- Order the elements in resulting array.

- The position of a given element (arr[i]) in the resulting array (res_arr) is the result from the counting array (cnt_arr) at the position of the element's value minus one:
`res_arr[cnt_arr[arr[i]] - 1] = arr[i]`

#### Optimizations to work with negative values
- We need to take into consideration that the range is not between positive numbers.
- That is why we get the maximum and minimum element from the array and calculate the range:
`range = max_element - min_element + 1`

- The counting array is generated using that range.
- When the elements are counted their position is based on the element's value minus the minimum element in the array:
`counting[arr[i] - min_element] += 1`

## Merge sort
Time complexity: O(n*log(n))
Space complexity: O(n*log(n))

- Divides the array in two halves and takes linear time to merge.

### Notes
- If the length of the array is more than one then we can call recursively merge sort.
- Use while loops to merge two sorted arrays.

## Quick sort
Time complexity: O(n*log(n))
Space complexity: O(log(n))

- Traversing the array when positioning the elements compared to the pivot.
- Recursively traversing smaller parts of the array.

### Notes
- If the length of the array is one, return the array.
- Proceed if low < high.
- Choose pivot 'x' (randomly) and sort compared to the pivot by placing the values less than 'x' in its left side and the values, bigger than 'x' on its right side.
- Position all the elements before repositioning the pivot in its correct position.
- The partition function must return the index of positioned 'x'.
`partition(arr, low, high)`
- When calling recursively quick sort the pivot should be excluded:
`quick_sort(arr, left, pi - 1)`
`quick_sort(arr, pi - 1, right)`
- All the time we work with the same array but in different parts of it and we are just swapping positions.
- The partitioning does not care to order them perfectly, it just positions them correctly compared to the pivot.

### Optimizations
- The partition always takes the pivot at high index. When randomizing we use another function that switches the randomly chosen element with the element in the high index.

## Linear search
Time complexity: O(n)
Space complexity: O(1)

## Binary search
Time complexity: O(log(n))
Space complexity: O(1)

! Works only for sorted arrays.

### Notes
- If left <= high, proceed.
- Middle position calculation:
`middle = left + (right - left) // 2`
- Check if the element at the middle (arr[middle]) of the array is 'x'. If it is not, call the binary searched.
- If  x < arr[middle], then call the binary search for the left side of the array.
`binary_search(arr, left, middle - 1, x)`
- If x > arr[middle], then call binary search for the right side of the array:
`binary_search(arr, middle + 1, right, x)`
- Exclude the middle position since we already know that is is not 'x'.

## Ternary search
Time complexity:
Space complexity:
