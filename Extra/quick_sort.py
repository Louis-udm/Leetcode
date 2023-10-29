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
    # 注意begin指针一直不变，loop中移动的是i和pivot指针
    # begin的值就是基准值，这个基准值在loop结束后要移动到正确的位置(pivot)。
    # 循环开始时,pivot指针指向begin，i指针指向begin+1.
    # loop过程中，pivot指针的作用是指定最后一个小于基准的值(begin)的位置
    # loop过程中，i值同begin值比较，如果i值小于begin值，pivot指针+1，然后i值和pivot指针的值互换
    # 换了以后，pivot指定的位置和它前面的位置的值都是小于基准(begin)的值
    # loop结束后，pivot和begin的值互换，这样基准值就到了正确的位置
    pivot = begin
    for i in range(begin + 1, end + 1):
        # 注意i是同begin比(begin-value是基准值)，begin指针是不动的。
        # 这写法的意思是，begin的那个值最终要放在pivot的位置
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        # pivot = partition_traditional(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


array = [97, 200, 100, 101, 211, 107]
quicksort(array)
print(array)
array = [97, 200, 211, 100, 100, 211, 107, 1]
quicksort(array)
print(array)
