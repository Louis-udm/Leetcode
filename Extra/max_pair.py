# return the number that it's the maximun pair in the array.
# [1, 2, -3,3,2,-2 -4] -> 3, because 3 and -3 are max pair in the array.


def solution(A):
    # write your code in Python 3.6
    sorted_a = sorted(A)
    for it in sorted_a:
        if it >= 0:
            return 0
        if -it in sorted_a:
            return -it
    return 0


def solution2(A):
    # write your code in Python 3.6
    res = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] == -A[i]:
                res = max(abs(A[i]), res)
                break
    return res


# print(solution2([1, 2, 3, -4]))
# print(solution2([1, -4, 3, 4]))
# print(solution2([1, -4, 3, -4]))
# print(solution2([1, 2, -3, 3, 2, -2 - 4]))
# print(solution2([]))
# print(solution2([2]))
arr=[ -7,   7,   6,   1,  28,  -7,  14,  -2,  14, -22,  19,  -8,  12,
         0, -30,  -9, -28,   5,   9,  21,   8,  11,  -9, -15,  -7,   9,
       -23, -13, -25,  -8,  23,  -3, -10,  18, -17, -16,   1,   4, -26,
        20,  19,  -2,  21,  13,  25,  -4,  -8, -23,  29, -14, -22,   5,
        -4,   8,   1,   1,   4,   7, -16,   3, -14, -18,  19,  18,  11,
        27,   4, -22, -30, -21,  27, -29,  20,  -7,  18,  -7, -14, -22,
        -5,   8,   0, -11,  21,   6, -22,  -8,  -3, -11, -22,  -6,  20,
       -29,  11, -29,  17,  17,  12, -25,   2,  15]
print(solution(arr))
print(solution2(arr))
def s1():
    global arr
    solution(arr)

def s2():
    global arr
    solution2(arr)

import timeit
print(timeit.timeit(s1, number=10000))
print(timeit.timeit(s2, number=10000))