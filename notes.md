# Notice
* 先看, 有动画和解题思路: https://blog.algomooc.com/(但是题目不完全同leetcode对应) 
* java leetcode中文 https://github.com/MisterBooo/LeetCodeAnimation
* 结合本repository看python实现: Python solution of problems from [LeetCode](https://leetcode.com/).
  
# 其他python相关leetcode资源:
* https://zhenyu0519.github.io/categories/#Linked-List
* https://github.com/youngyangyang04/leetcode-master

# Questions:
* 前几道经典题的动画解析: https://github.com/MisterBooo/LeetCodeAnimation
* [NO.1 TwoSum](./1-100q/01_TwoSum.py)
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
![TwoSum](https://camo.githubusercontent.com/c8a78a4da1b40f98100cec12b6dc724e6159ab9859135dab3b87473e7374353e/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f61763437762e676966)

* [NO.2](./1-100q/02.py)
题目来源于 LeetCode 上第 2 号问题：两数相加。题目难度为 Medium，目前通过率为 33.9%. 
给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
![NO.2](https://camo.githubusercontent.com/56a78d49fe71daeb64a888d5167e0e924127f94ff670c48871825ce634c38820/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f667a3933332e676966)

* [NO.3](./1-100q/03.py) 给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。
建立一个256位大小的整型数组 freg ，用来建立字符和其出现位置之间的映射。维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
- （1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
- （2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
- （3）重复（1）（2），直到左边索引无法再移动；
- （4）维护一个结果res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。
![NO.3](https://camo.githubusercontent.com/4d78fd6ac2ffe9559d2188efb0dd57a95f5aeb3c831653ce186777eb5ed298b9/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f76786137662e676966)

* [NO.9](./1-100q/09.py)
判断一个整数是否是回文数
![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/v3tkl.gif)

* [NO.53](./1-100q/53.py) 对应[剑指 Offer 42. 连续子数组的最大和](https://blog.algomooc.com/042.html#%E4%B8%80%E3%80%81%E9%A2%98%E7%9B%AE%E6%8F%8F%E8%BF%B0)
![NO.53](https://camo.githubusercontent.com/4d78fd6ac2ffe9559d2188efb0dd57a95f5aeb3c831653ce186777eb5ed298b9/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f76786137662e676966)

* [Palindrome](./Extra/palindrome.py) 
Palindrome: word, phrase, or sequence that reads the same backward as forward, e.g., madam or nursesrun. Given a string, find the longest substring which is palindrome. For example, if the given string is “isevilolivealive”, the output should be “evilolive”.

* [Max pair](./Extra/max_pair.py) 
return the number that it's the maximun pair in the array.
[1, 2, -3,3,2,-2 -4] -> 3, because 3 and -3 are max pair in the array.

* [Mini remove](./Extra/minimum_remove.py) 
There is an array A of N integers sorted in non-decreasing order. in one move, you can either remove an integer from A or insert an integerbefore or after any element of A. The goal is to achieve an array in which all values X that are present in the array occur exactly X times.The function should return the minimum number of moves after which every value X in the array occurs exactly X times. Note that it's permissible to remove some values entirely, if appropriate.

* [implement power function.](./Extra/pow.py) 
Implement power function only using +-*/

* [bracket](./Extra/bracket.py) 
Match the parentheses.
