"""
https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
Question: An Array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero.
For the below array, program should print -80 and 85.
Solution:
- 最重要的是先按绝对值排序
- quicksort: O(nlogn)
"""
import sys
 
def abs_partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if abs(array[i]) <= abs(array[begin]):
            pivot += 1 
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def abs_quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = abs_partition(array, begin, end)
        _quick_sort(array, begin, pivot - 1)
        _quick_sort(array, pivot + 1, end)

    return _quick_sort(array, begin, end)


def findMinSum(arr, n):
     
    abs_quicksort(arr,0,n-1)

    print(f"After abs qucksort: {arr}")
    Min = sys.maxsize
    x = 0
    y = 0
   
    for i in range(1, n):
         
        # Absolute value shows how
        # close it is to zero
        if (abs(arr[i - 1] + arr[i]) < Min):
             
            # If found an even close value
            # update min and store the index
            Min = abs(arr[i - 1] + arr[i])
            x = i - 1
            y = i
 
    print("The two elements whose sum is minimum are",
          arr[x], "and", arr[y])
 
# Driver code
# arr = [ 1, 60, -10, 70, -80, 85 ]
arr = [ 1, -80, -10, 70, 85, -64 ]
n = len(arr)
 
findMinSum(arr, n)
