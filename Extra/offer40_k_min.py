# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入 4、5、1、6、2、7、3、8 这 8 个数字，
# 则最小的 4 个数字是 1、2、3、4 。
# 暴力解法: sorted(array)[:k]
# quicksort apporch: 
# 因为找出的这 k 个数并不需要按照顺序排列。借助快速排序,不断的缩小排序的区间, 直到左区域=k

def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1 
            # 这种写法的意思: 移动基准点，使得左边的都<=基准点都值,
            # 为什么是先右移pivot再互换，因为pivot会指向最后真正放基准值的地方,
            # loop中最后一个被互换到pivot暂存的小于基准的值，退出loop后会真正同begin互换
            # 这样begin就真正到了pivot的地方
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort_k(array, k, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        nonlocal k
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        if pivot<k:
            # 比pivot小的不足k个, 只需要排pivot右边的，寻找下一个pivot是否刚好==k
            _quicksort(array, pivot + 1, end)
        elif pivot>k:
            # 比pivot小的大于k个, 只需要排pivot左边的，寻找下一个pivot是否刚好==k
            _quicksort(array, begin, pivot - 1)
        elif pivot==k:
            # 比pivot小的刚好k个
            return

    _quicksort(array, begin, end)
    return array[:k]


array = [100, 211, 200, 101, 107, 97, 2,3,1]
print(quicksort_k(array, 3))
print(array)
array = [ 100, 97, 200, 211,100, 211, 107,1]
print(quicksort_k(array, 3))
print(array)
