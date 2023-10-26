class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val


def binary_insert(root: Node|None, node: Node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)


def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

# 层次遍历, 广度优先搜索
def breadth_travel(root):
    if not root:
        return
    q = [root]
    while q:
        node = q.pop(0)
        print(node.data)
        if node.l_child:
            q.append(node.l_child)
        if node.r_child:
            q.append(node.r_child)

r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
pre_order_print(r)
