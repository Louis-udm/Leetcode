# There is an array A of N integers sorted in non-decreasing order. 
# in one move, you can either remove an integer from A or insert an integer
# before or after any element of A. The goal is to achieve an array in which 
# all values X that are present in the array occur exactly X times.
# The function should return the minimum number of moves after which every 
# value X in the array occurs exactly X times. Note that it's permissible to 
# remove some values entirely, if appropriate.
from collections import Counter

def solution(A):
    # write your code in Python 3.6
    max_op = len(A)
    count_dict=Counter(A)
    # count_dict = {}
    # for it in A:
    #     count_dict[it] = 1 if it not in count_dict else count_dict[it] + 1

    min_for_items = []
    for k, v in count_dict.items():
        # add/remove times for keep it: abs(k-v), completely remove it: v
        min_for_it = min(abs(k - v), v)
        min_for_items.append(min_for_it)
        
    return min(max_op, sum(min_for_items))


print(solution([1, 1, 3, 4, 4, 4]))
print(solution([1, 2, 2, 2, 5, 5, 5, 8]))
print(solution([1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4]))
print(solution([10, 10, 10]))
print(solution([10]))
print(solution([]))
print(solution([1]))
print(solution([2]))
print(solution([2,2]))
print(solution([1, 2, 2, 3, 3, 3]))


def s1():
    solution([1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4])

import timeit
print(timeit.timeit(s1, number=10000))