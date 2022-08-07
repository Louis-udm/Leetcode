
from typing import List

def reversed_pair_count(arr: List[int]):
    """
    借用归并排序思路
    """
    count = 0

    def merge(arr1:List[int], arr2:List[int]): 
        nonlocal count
        result = []
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
                # 在归并排序中唯一添加的statement
                # arr1当前item>arr2当前item，意味着arr1后面的都大于arr2当前item
                # len(arr1/2)是变动的 
                count+=len(arr1) 
        if arr1:
            result += arr1
        if arr2:
            result += arr2
        return result

    def merge_count(arr:List[int]):
        """
        归并排序
        :param arr: 待排序的List
        :return: 排好序的List
        """
        nonlocal count
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        return merge(merge_count(arr[:mid]), merge_count(arr[mid:]))

    merge_count(arr)
    return count

print(reversed_pair_count([7,5,6,4]))