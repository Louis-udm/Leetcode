"""
Quick Sort in Python
source: https://stackoverflow.com/questions/18262306/quicksort-with-python
"""


def partition_traditional(array, left: int, right: int):
    # 经典快速排序的写法
    # 目的就是使得 all left < pivot < all right，并且返回这个中心点
    # pivot称为基准点，partition后它不一定就会在中间，它可以在任何地方，所以最差的其中
    # 一种情况是对已经排好序的array做快速排序, O(n²)
    # 最差的情况就是每一次取到的元素就是数组中最小/最大的 (O(n²))，这种情况其实就是冒泡排序了(每一次都排好一个元素的顺序)
    # 平均和最佳都是O(nlogn)

    # 设置当前区间的第一个元素为基准元素
    pivot_value = array[left]

    # left 向右移动，right 向左移动，直到 left 和 right 指向同一元素为止
    while left < right:

        # 只有当遇到小于 pivot 的元素时，right 才停止移动
        # 此时，right 指向了一个小于 pivot 的元素，这个元素不在它该在的位置上
        while left < right and array[right] >= pivot_value:
            # 如果 right 指向的元素是大于 pivot 的，那么
            # right 不断的向左移动
            right -= 1

        # 将此时的 nums[left] 赋值为 nums[right]
        # 执行完这个操作，比 pivot 小的这个元素被移动到了左侧
        array[left] = array[right]

        # 只有当遇到大于 pivot left 才停止移动
        # 此时，left 指向了一个大于 pivot 的元素，这个元素不在它该在的位置上
        while left < right:
            # 如果 left 指向的元素是小于 pivot 的，那么
            # left 不断的向右移动
            left += 1

        # 将此时的 nums[right] 赋值为 nums[left]
        # 执行完这个操作，比 pivot 大的这个元素被移动到了右侧
        array[right] = array[left]

    # 此时，left 和 right 相遇，那么需要将此时的元素设置为 pivot
    # 这个时候，pivot 的左侧元素都小于它，右侧元素都大于它
    array[left] = pivot_value

    return left


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


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        # pivot = partition(array, begin, end)
        pivot = partition_traditional(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


array = [97, 200, 100, 101, 211, 107]
quicksort(array)
print(array)
array = [97, 200, 211, 100, 100, 211, 107,1]
quicksort(array)
print(array)
