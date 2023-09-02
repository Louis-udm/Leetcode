# Palindrome: word, phrase, or sequence that reads the same backward as forward, e.g., madam or nursesrun.
# Given a string, find the longest substring which is palindrome. For example, if the given string is “isevilolivealive”, the output should be “evilolive”.


def palin(st):
    i = 0
    tmp = ""
    results = []
    while i < len(st):
        j = len(st) - 1
        while j > -1:
            # print(i,j)
            if st[i] == st[j]:
                m = i
                n = j
                is_palindrome = True
                while m <= j and n >= i:
                    if st[m] == st[n]:
                        tmp += st[m]
                        m += 1
                        n -= 1
                    else:
                        is_palindrome = False
                        break
                if is_palindrome:
                    results.append(tmp)
                tmp = ""
            j -= 1
        i += 1
    # print(results)
    results.append(tmp)

    return max(results, key=len)  # return the longest str in results.


def palin_better(st):
    results = []
    # middles=[len(st)//2]
    for i in range(len(st)):
        if i < len(st) - 1 and st[i] == st[i + 1]:
            j = 0
            for j in range(1, i + 1):
                if st[i - j] != st[i + 1 + j]:
                    j -= 1
                    break
            results.append(st[i - j : i + 1 + j + 1])
        # if st[i]==st[i-1]:
        #     for j in range(1,i):
        #         if st[i-1-j]!=st[i+j]:
        #             j-=1
        #             break
        #     results.append(st[i-1-j:i+j])
        if i > 0 and i < len(st) - 1 and st[i + 1] == st[i - 1]:
            j = 0
            for j in range(1, i):
                if st[i - 1 - j] != st[i + 1 + j]:
                    j -= 1
                    break
            results.append(st[i - 1 - j : i + 1 + j + 1])

    return max(results, key=len)  # return the longest str in results.


def palin_dp(st: str):
    import numpy as np

    l = len(st)
    max_len = 0
    start = -1
    dp = np.zeros((l, l))
    for i in range(l):
        dp[i, i] = 1
        if i < l - 1 and st[i] == st[i + 1]:
            dp[i, i + 1] = 1
            start = i
            max_len = 2
    for cur_len in range(3, l):
        for i in range(l - cur_len):
            j = i + cur_len - 1
            if dp[i + 1, j - 1] and st[i] == st[j]:
                dp[i, j] = 1
                max_len = cur_len
                start = i
    if max_len >= 2:
        return st[start : start + max_len]
    return None


def manacher(s0: str) -> list:
    """
    https://writings.sh/post/algorithm-longest-palindromic-substring
    https://blog.csdn.net/u013309870/article/details/70742315
    https://www.cnblogs.com/champock/articles/15431349.html
    https://www.cxyxiaowu.com/2869.html

    这个python代码来自: https://zh.m.wikipedia.org/zh-hans/%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2#:~:text=%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2%EF%BC%88%E8%8B%B1%E8%AA%9E%EF%BC%9ALongest%20palindromic%20substring%EF%BC%89,%E6%96%87%E5%AD%90%E4%B8%B2%E6%98%AF%E2%80%9Canana%E2%80%9D%E3%80%82
    """
    T = "$#" + "#".join(s0) + "#@"
    l = len(T)
    P = [0] * l
    R, C = 0, 0
    for i in range(1, l - 1):
        if i < R:
            P[i] = min(P[2 * C - i], R - i)

        while T[i + (P[i] + 1)] == T[i - (P[i] + 1)]:
            P[i] += 1

        if P[i] + i > R:
            R = P[i] + i
            C = i
    # return P
    return list(map(lambda x: s0[x], P))


str0 = str1 = "aamadamb"
str1 = "madefgc6gfedam5aamadamb"
str2 = "isevilolivealive"
str3 = "abccba6"
print(palin(str0))
print(palin(str1))
print(palin(str2))
print(palin(str3))

print(palin_better(str0))
print(palin_better(str1))
print(palin_better(str2))
print(palin_better(str3))

print(palin_dp(str0))
print(palin_dp(str1))
print(palin_dp(str2))
print(palin_dp(str3))

# print(manacher(str0))
# print(manacher(str1))
# print(manacher(str2))
# print(manacher(str3))


def s1():
    global str1
    palin(str1)


def s2():
    global str1
    palin_better(str1)


def s3():
    global str1
    palin_dp(str1)


import timeit

print(timeit.timeit(s1, number=10000))
print(timeit.timeit(s2, number=10000))
print(timeit.timeit(s3, number=10000))
