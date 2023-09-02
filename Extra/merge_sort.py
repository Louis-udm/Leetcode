"""
Merge Sort: 稳定排序, O(nlog_2n)
https://segmentfault.com/a/1190000022722050
"""

from typing import List

def merge(arr1:List[int], arr2:List[int]): 
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result

def merge_sort(arr:List[int]):
    """
    归并排序
    :param arr: 待排序的List
    :return: 排好序的List
    """
    if len(arr) <= 1:
        return arr
    # mid = len(arr) // 2
    mid = len(arr) >> 1
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


import random
random.seed(54)
arr = [random.randint(0,100) for _ in range(10)]
print("原始数据：", arr)
arr_new = merge_sort(arr)
print("归并排序结果：", arr_new)