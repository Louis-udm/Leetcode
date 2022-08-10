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
    s = sum(L)
    if s < k:
        return 0, 0
    max_v = s // k
    count = 0
    total = 0
    for v in range(max_v, 0, -1):
        for l in L:
            count += l // v
            total += 1
            if count >= k:
                return total, v
        count = 0

    return total, 0

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
