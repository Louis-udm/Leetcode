"""
Input integer array, all item are unique，
找出所有连续sub-array（至少2个，并不打乱原始顺序）下，跳跃数量
example: [4,1,3,2], 
all consecutive array = [ [4,1], [1,3], [3,2], [4,1,3], [1,3,2], [4,1,3,2] ]
jump_count  =               1    + 1     + 0    + 1      + 0      + 0  = 3
这里的跳跃数量指，某个数组在变成排序后，不连续的次数, 
example: [4,1,3,2] -> [1,2,3,4] -> 0 jump; [4,1] -> [1,4] -> 1 jump.
"""
def find_total_imbalance(rank):
    count=0
    def merge_and_find_imbalance(A,B):
    """
    参考自merge_tew_arrays.py,或者说参考自merge_sort中的对两个有序数组合并
    """
        nonlocal count
        C=[]
        i = j = 0
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                if len(C) < 1:
                    C.append(A[i])
                elif C[-1] < A[i]:
                    if A[i]-C[-1]>1: #加入到C前判断，同C的最后一个元素比是否有跳跃
                        count+=1
                    C.append(A[i])
                i += 1
            else:
                if len(C) < 1:
                    C.append(B[j])
                elif C[-1] < B[j]:
                    if B[j]-C[-1]>1:
                        count+=1
                    C.append(B[j])
                j += 1

        if i < len(A):
            for it in A[i:]:
                if not C or C[-1]<it:
                    if C and it-C[-1]>1:
                        count+=1
                    C.append(it)
        if j < len(B):
            for it in B[j:]:
                if not C or C[-1]<it:
                    if C and it-C[-1]>1:
                        count+=1
                    C.append(it)
        return C

    cur_lists=[[it] for it in rank] # 从两两合并开始
    next_lists=[]
    while len(cur_lists)>1:
        for i in range(len(cur_lists)-1):
            next_lists.append(merge_and_find_imbalance(cur_lists[i],cur_lists[i+1]))
        cur_lists=next_lists
        next_lists=[]
    
    return count


arr=[4,1,3,2] #3
print(find_total_imbalance(arr))
arr=[8,1,5,3,4,11] #21
print(find_total_imbalance(arr))