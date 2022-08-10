# Description
# Given two sorted arrays, return a sorted array that contains UNIQUE elements by merging both arrays.
# Question Statement
# Sample Cases
# [1,3,5] + [3,4] ==> [1,3,4,5]


def merge2arrays(A: list, B: list):
    C: list = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            if len(C) < 1:
                C.append(A[i])
            elif C[-1] < A[i]:
                C.append(A[i])
            i += 1
        else:
            if len(C) < 1:
                C.append(A[i])
            elif C[-1] < B[j]:
                C.append(B[j])
            j += 1
    if i < len(A):
        C += A[i:]
    if j < len(B):
        C += B[j:]

    return C


A = [1, 3, 5]
B = [3, 4]
print(merge2arrays(A, B))
# [1,3,4,5]

A = []
B = []
print(merge2arrays(A, B))
# []

A = []
B = [1]
print(merge2arrays(A, B))
# [1]
