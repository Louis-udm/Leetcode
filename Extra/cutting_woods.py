# Cutting woods
# We have n pieces of wood, with known lengths (integer array L). We need k pieces of wood with equal length. What's the maximum integer length?

# Examples
# - L=[5, 9, 7], k=3, return 5
# - L=[5, 9, 7], k=4, return 4

# L, k, v

# Given v, is it possible to cut L into k pieces of length v?


def cutting_woods(L: list, k):
    # k is k pieces that needed
    # return total iteration and the maximum integer length
    # O(max(L)*len(L))
    if sum(L) < k:
        return 0, 0
    max_v = max(L)
    count = 0
    total = 0
    for v in range(max_v, 0, -1):
        for l in L:
            total += 1
            count += l // v
            if count >= k:
                return total, v
        count = 0
    return total, 0


def cutting_woods_better(L: list, k):
    # k is k pieces that needed
    # return total iteration and the maximum integer length
    # O(max(L)*len(L))
    # max_v 不一定同最小的那根有关，因为有可能有一根特别长，可以满足k段并且还大于最小那根
    s = sum(L)
    if s < k:
        return 0, 0
    max_v = s // k
    count = 0
    total_loop = 0
    for v in range(max_v, 0, -1):
        for l in L:
            count += l // v
            total_loop += 1
            if count >= k:
                return total_loop, v
        count = 0

    return total_loop, 0


def cutting_woods_binary_search(L: list, k):
    # k is k pieces that needed
    # return total iteration and the maximum integer length
    # O(max(L)*len(L))
    # 为什么要用2分查找:
    # 原始2分法是, 给你一个数字，在一个有序数组中找到它的位置
    # 这里是递增有序数组[1..max_v], 你要找到满足一定条件的value, 并且这个条件可以知道大小
    # 当当前value的划分计数大于k时，说明要在右边找，如果小于则在左边找。
    s = sum(L)
    if s < k:
        return 0, 0
    max_v = s // k
    if max_v == 1:
        return 0, 1
    min_v=1
    cur_v = max_v // 2
    count = 0
    total_loop = 0
    while True:
        for l in L:
            count += l // cur_v
            total_loop += 1
            if count > k:
                min_v=cur_v
                break
        if count == k:
            return total_loop, cur_v
        if count < k:
            max_v = cur_v
        if cur_v == (min_v + max_v) // 2:
            return total_loop, cur_v
        cur_v = (min_v + max_v) // 2
        count = 0

    return total_loop, 0


def cutting_woods_binary_search_better(L: list, k):
    # k is k pieces that needed
    # return total iteration and the maximum integer length
    # O(max(L)*len(L))
    # 为什么要用2分查找:
    # 原始2分法是, 给你一个数字，在一个有序数组中找到它的位置
    # 这里是递增有序数组[1..max_v], 你要找到满足一定条件的v, 并且可以根据条件值分两边再找
    # 当当前value的划分计数大于k时，说明要在右边找，如果小于则在左边找。
    # 这里对L从大到小排序会让平均复杂度降低
    s = sum(L)
    if s < k:
        return 0, 0
    max_v = s // k
    if max_v == 1:
        return 0, 1
    min_v=1
    cur_v = max_v // 2
    count = 0
    total_loop = 0
    L = sorted(L, reverse=True)
    while True:
        for l in L:
            count += l // cur_v
            total_loop += 1
            if count > k:
                min_v=cur_v
                break
        if count == k:
            return total_loop, cur_v
        if count < k:
            max_v = cur_v
        if cur_v == (min_v + max_v) // 2:
            return total_loop, cur_v
        cur_v = (min_v + max_v) // 2
        count = 0

    return total_loop, 0


# 可能还有其他更好的算法
# dp[max_v,len(L)], # record dp[1, 1]=count, dp[2, 1]= count, sum(dp[:1])

print(cutting_woods([5, 9, 7], 3))  # 5
print(cutting_woods([5, 9, 7], 4))  # 4
print(cutting_woods([5, 9, 7], 20))  # 1
print(cutting_woods([5, 9, 7], 21))  # 1
print(cutting_woods([5, 9, 7], 22))  # 0

print(cutting_woods_better([5, 9, 7], 3))  # 5
print(cutting_woods_better([5, 9, 7], 4))  # 4
print(cutting_woods_better([5, 9, 7], 20))  # 1
print(cutting_woods_better([5, 9, 7], 21))  # 1
print(cutting_woods_better([5, 9, 7], 22))  # 0

print(cutting_woods_binary_search([5, 9, 7], 3))  # 5
print(cutting_woods_binary_search([5, 9, 7], 4))  # 4
print(cutting_woods_binary_search([5, 9, 7], 20))  # 1
print(cutting_woods_binary_search([5, 9, 7], 21))  # 1
print(cutting_woods_binary_search([5, 9, 7], 22))  # 0

print(cutting_woods_binary_search_better([5, 9, 7], 3))  # 5
print(cutting_woods_binary_search_better([5, 9, 7], 4))  # 4
print(cutting_woods_binary_search_better([5, 9, 7], 20))  # 1
print(cutting_woods_binary_search_better([5, 9, 7], 21))  # 1
print(cutting_woods_binary_search_better([5, 9, 7], 22))  # 0

print("---------")
print(cutting_woods(
            [3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], 20
        ))
print(cutting_woods_better(
            [3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], 20
        ))
print(cutting_woods_binary_search(
            [3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], 20
        ))
print(cutting_woods_binary_search_better(
            [3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], 20
        ))
        

K=[ 45,  20,  70,  93, 149, 140,  24,  58, 134,  61, 100,  84, 152,
        15,  24,  99,  82, 145,  37,  40,  42, 101,  23,  60,  80,  40,
        56,  67,  47, 100,  11, 126,  86, 129,  42, 120, 102,  37,  50,
        45,  98,  70,  49,  27,  16,   3,   3,  44,  31,  32]


def s1():
    global K
    for k in K:
        cutting_woods_better([3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], k)


def s2():
    global K
    for k in K:
        cutting_woods_binary_search(
            [3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], k
        )


def s3():
    global K
    for k in K:
        cutting_woods_binary_search_better(
            [3, 5, 9, 7, 15, 40, 5, 8, 20, 4, 21, 16], k
        )


import timeit

print(timeit.timeit(s1, number=10000))
print(timeit.timeit(s2, number=10000))
print(timeit.timeit(s3, number=10000))
