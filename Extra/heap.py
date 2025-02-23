"""Heap

https://nemo.cool/254.html
https://www.tutorialspoint.com/python_data_structure/python_heaps.htm

堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。
"""


class heap(object):
    def __init__(self):
        # 初始化一个空堆，使用数组来在存放堆元素，节省存储
        self.data_list = []

    def get_parent_index(self, index):
        # 返回父节点的下标
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            # 右移一位，相当于除以2。因为是从0开始的，所以要减1再除以2
            # 因为堆是完全二叉树，任何父节点到子节点的中间的节点的数量刚好是父节点序号的数量+1/+2
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        # 交换数组中的两个元素
        self.data_list[index_a], self.data_list[index_b] = (
            self.data_list[index_b],
            self.data_list[index_a],
        )

    def insert(self, data):
        # 先把元素放在最后，然后从后往前依次堆化
        # 这里以大顶堆为例，如果插入元素比父节点大，则交换，直到最后
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
        while (
            parent is not None
            and self.data_list[parent] < self.data_list[index]
        ):
            # 交换操作
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def removeMax(self):
        # 删除堆顶元素，然后将最后一个元素放在堆顶，再从上往下依次堆化
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        # 堆化
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        # 从上往下堆化，从index 开始堆化操作 (大顶堆)
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if (
                2 * index + 1 <= total_index
                and self.data_list[2 * index + 1]
                > self.data_list[maxvalue_index]
            ):
                # 左子节点大于父节点，标记最大值的下标为左子节点的下标
                maxvalue_index = 2 * index + 1

            if (
                2 * index + 2 <= total_index
                and self.data_list[2 * index + 2]
                > self.data_list[maxvalue_index]
            ):
                # 右子节点大于父节点，标记最大值的下标为右子节点的下标
                maxvalue_index = 2 * index + 2

            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


if __name__ == "__main__":
    myheap = heap()
    for i in range(10):
        myheap.insert(i + 1)
    print("建堆:", myheap.data_list) # [10, 9, 6, 8, 7, 2, 5, 1, 4, 3]
    print(myheap.get_parent_index(2))
    print("删除堆顶元素:", [myheap.removeMax() for _ in range(10)]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
