"""
[来源: 剑指 Offer 66. 构建乘积数组](https://blog.algomooc.com/066.html)
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。 **不能使用除法**
- 如果可以使用除法，则先一遍遍历算出总乘积，然后另一遍除以arr[i]
- 暴力算法为双循环，O(n^2)
- 在公式 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1] 中，实际上可以划分为两个部分，从 0 到 i - 1 和从 i + 1 到 n - 1，因此，想要构建乘积数组后某下标对应元素的值，只需要求出该下标对应原数组中其左边的元素的乘积和其右边的元素的乘积，最后将两个乘积再相乘即可
- 保存会被重复计算的中间结果，具体为：leftA list保存当前元素之外，左边的累乘； rightA list保存当前元素外，右边的累乘。
"""
from typing import List

def left_one_out_product(arr:List[int]):
    l=len(arr)
    leftA: List[int]=[1]*l
    rightA: List[int]=[1]*l
    for i, t in enumerate(arr[:l-1]):
        leftA[i+1]=leftA[i]*t
    # for i, t in enumerate(reversed(arr[1:])):
    #     rightA[l-i-2]=rightA[l-i-1]*t
    for i in range(l-2,-1,-1):
        rightA[i]=rightA[i+1]*arr[i+1]
    # print(leftA,rightA)

    return [a*b for a,b in zip(leftA,rightA)]

print(left_one_out_product([1,2,3,4,5]))