"""题目来源于 LeetCode 第 9 号问题：回文数。题目难度为 Easy，目前通过率为 56.0%。

## 题目描述

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

```
输入: 121
输出: true
```

**示例 2:**

```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3:**

```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```

**进阶:**

你能不将整数转为字符串来解决这个问题吗？

## 题目解析

### 解法一：普通解法

最好理解的一种解法就是先将 **整数转为字符串** ，然后将字符串分割为数组，只需要循环数组的一半长度进行判断对应元素是否相等即可。

### 解法二：进阶解法---数学解法

通过取整和取余操作获取整数中对应的数字进行比较。

举个例子：1221 这个数字。

- 通过计算 1221 / 1000， 得首位1
- 通过计算 1221 % 10， 可得末位 1
- 进行比较
- 再将 22 取出来继续比较
"""


def is_palindrome_int(num: int) -> bool:
    i = 1
    l = len(str(num))
    while True:
        # 循环中每次,num去头去尾
        # 去头num % 10 ** (l - i + 1), 去尾// 10 ** (i - 1)
        num = (num % 10 ** (l - i + 1)) // 10 ** (i - 1)
        l = len(str(num))
        # 比较num的头==尾?
        if num // 10 ** (l - 1) != num % 10:
            return False
        if l <= 1:
            return True
        i += 1


print(is_palindrome_int(12353721))
print(is_palindrome_int(1235321))
print(is_palindrome_int(123321))
print(is_palindrome_int(131))
print(is_palindrome_int(131))
print(is_palindrome_int(11))
print(is_palindrome_int(1))
