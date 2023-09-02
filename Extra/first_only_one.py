# Simple
# 剑指 Offer 50. 第一个只出现一次的字符
# https://blog.algomooc.com/050.html#%E4%B8%80%E3%80%81%E9%A2%98%E7%9B%AE%E6%8F%8F%E8%BF%B0

def first_only_one(s:str):
    cmap={}
    for i,c in enumerate(s):
        if c not in cmap:
            cmap[c]=i
        else:
            cmap[c]=-1
    for k,v in cmap.items():
        if v>-1:
            return k
    return " "

print(first_only_one("abaccdeff"))
print(first_only_one("abbbbaccdeff"))
print(first_only_one(""))