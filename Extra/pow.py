# Question:
# implement power function.
# a^b
# 2^4 = 16
# 3^4 = 81
#
# op: +, -, /, *, %
# not ops: **, math lib, log, exp
# a, b – integers

# 2^7 -- = 128
# 2^7 = 2*2*2*2*2*2*2


def pow_vanila(a, b):
    # vanila algorithm, time complexity=O(b)
    if b == 0:
        return 1
    res = a
    for i in range(abs(b) - 1):
        res = res * a
    if b < 0:
        res = 1 / res
    return res


def pow(a, b):
    def p1(a, b):
        # 子函数用于“翻倍乘法”, 次数为2^i<b
        i = 2
        while i < b:
            a = a * a
            i *= 2

        return a, i // 2

    if b == 0:
        return 1

    res = 1
    remain = abs(b)
    while remain > 0:
        # 循环这个子函数，b每次为上一次翻倍乘法后剩下的次数。
        tmp, cur = p1(a, remain)
        res *= tmp
        remain -= cur

    if b < 0:
        res = 1 / res

    return res


print(pow(2, 1))  # 2
print(pow(2, 6))  # 64
print(pow(2, 7))  # 128
print(pow(2, 11))  # 2048
print(pow(3, 0))  # 1
print(pow(3, 2))  # 9
print(pow(3, 4))  # 81
print(pow(3, -2))  # 0.111
print(pow(3, 20))  # 3486784401


def s1():
    pow_vanila(3, 200)


def s2():
    pow(3, 200)


import timeit

print(timeit.timeit(s1, number=10000))
print(timeit.timeit(s2, number=10000))
