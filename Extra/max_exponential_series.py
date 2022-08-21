""" 
输入integer数组, 输出能形成[x1, x2=x1*x1, x3=x2*x2, ...], x_i in input arr 
的这种数组的最大长度
"""

def max_set_size(rice_bags):
    rice_bags = sorted(rice_bags)
    bag_map = {r: r for r in rice_bags}
    max_count = count = 1
    taked_map = {}
    for r in rice_bags:
        if r not in taked_map:
            cur = r * r
            while cur in bag_map:
                taked_map[cur] = cur
                count += 1
                cur *= cur
            max_count = max(max_count, count)
            count = 1

    return max_count if max_count > 1 else -1


print(max_set_size([9, 3, 625, 2, 4, 5, 16, 25, 256])) # len([2,4,16,256])=4
