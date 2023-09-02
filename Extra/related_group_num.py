"""
一个nxn matrix表示row元素i是否有送东西给col元素j, 1表示送，0表示没有送, m[i,i]=1
求联通子图个数 （就是有送东西关系的连接为一个子图)
"""
def related_group_num(related:list):
    """
    related is a matrix with the format looks like: 
    ["100000","110011","001000","000100","000110","000001"]
    """
    sets={i:{i} for i in range(len(related))}
    print(sets)
    for i,row in enumerate(related):
        for j,col in enumerate(row):
            if i!=j and int(col)>0:
                sets[i].update(sets[j])
                sets[j]=sets[i]

    return len(set([id(a) for a in sets.values()]))

print(related_group_num(["100000","110011","001000","000100","000110","000001"]))


