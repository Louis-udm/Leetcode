# Notices

* 先看, 有动画和解题思路: https://blog.algomooc.com/(但是题目不完全同leetcode对应) 
* java leetcode中文 https://github.com/MisterBooo/LeetCodeAnimation
* 结合本repository看python实现: Python solution of problems from [LeetCode](https://leetcode.com/).
  
# 其他python相关leetcode资源:
* https://zhenyu0519.github.io/categories/#Linked-List
* https://github.com/youngyangyang04/leetcode-master

# Data structure and general algo in Python
* [TheAlgorithms in python](https://github.com/TheAlgorithms/Python)
* [Python 标准内置类1](https://www.cnblogs.com/paulwhw/articles/12304977.html)
* [Python 标准内置类2](https://zhuanlan.zhihu.com/p/69487899)
* [自己手动实现](https://nemo.cool/254.html)

#### [BST (binary search tree)](Extra/bst.py)
二叉搜索树是一棵有序的二叉树: 1、若它的左子树不为空，那么左子树上的所有值均小于它的根节点; 2、若它的右子树不为空，那么右子树上所有值均大于它的根节点; 3、它的左子树和右子树也都是二叉搜索树

#### [Heap (堆)](Extra/heap.py)
堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。

#### [Time complexities of sort algorithms](https://segmentfault.com/a/1190000021638663)

#### [Quick Sort](./Extra/quick_sort.py)

#### [Merge Sort](./Extra/merge_sort.py)

# Questions:
前几道经典题的动画解析: https://github.com/MisterBooo/LeetCodeAnimation

## Array and Tree
### [NO.1 TwoSum](./1-100q/01_TwoSum.py)
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
![TwoSum](https://camo.githubusercontent.com/c8a78a4da1b40f98100cec12b6dc724e6159ab9859135dab3b87473e7374353e/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f61763437762e676966)
- map辅助，扫描一遍，看(target-arr[i])是否在map中
- 如果是已排序，并且不用map辅助，可以先2分法找到<=target的index作为right指针，然后只在前半部分找。left->, <-right [参考: 剑指 Offer 57. 和为s的两个数字](https://blog.algomooc.com/057.html)
- 但是如果使用map辅助，不管是不是排序了的array，第二个解法似乎不占优势。

### [NO.2 AddTwoNumbers (linked list)](./1-100q/02.py)
题目来源于 LeetCode 上第 2 号问题：两数相加。题目难度为 Medium，目前通过率为 33.9%. 
给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
![NO.2](https://camo.githubusercontent.com/56a78d49fe71daeb64a888d5167e0e924127f94ff670c48871825ce634c38820/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f667a3933332e676966)

### [NO.3 Longest Substring Without Repeating Characters](./1-100q/03.py) 给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。
建立一个256位大小的整型数组 freg ，用来建立字符和其出现位置之间的映射。维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
- （1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
- （2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
- （3）重复（1）（2），直到左边索引无法再移动；
- （4）维护一个结果res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。

更具体：mapSet记录(更新)遍历过程中各char最后一次出现的位置+1, 遍历的下一个char是否在mapSet中? 不在其中则窗口右侧(end指针)加一; 
如果已在其中，说明这个char之前出现过，start = max(mapSet[s[end]], start)包含两种可能：
1. 之前出现过并且在当前window中，start变为之前出现过的(位置+1)，相当于缩小window.
2. 之前出现过但是没有在当前window，start不用变(但更新mapset中这个char的位置+1)
![NO.3](https://camo.githubusercontent.com/4d78fd6ac2ffe9559d2188efb0dd57a95f5aeb3c831653ce186777eb5ed298b9/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f76786137662e676966)

### [NO.9 Palindrome Number](./1-100q/09.py)
判断一个整数是否是回文数:
loo循环, 每次num去头去尾. 去头num % 10 ** (l - i + 1), 去尾// 10 ** (i - 1), 然后比较num的头==尾(num // 10 ** (l - 1) == num % 10)
![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/v3tkl.gif)

### [NO.53 Max sum of contiguous subarray](./1-100q/53.py) 
[来源: 剑指 Offer 42. 连续子数组的最大和](https://blog.algomooc.com/042.html)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- 可以这样理解：遍历每个item, 对于当前item，前面的sum是不是当前item的累赘(就是前面的sum是不是>0),
- 如果前面的sum<0，那就舍弃前面的sum，新的sum从当前item开始. 可以保留每移动一步新update后的sum，然后max(list_of_sums)
![NO.53](https://camo.githubusercontent.com/4d78fd6ac2ffe9559d2188efb0dd57a95f5aeb3c831653ce186777eb5ed298b9/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f76786137662e676966)

### [Smallest missing](./Extra/smallest_missing.py)
Given a list of positive integers (greater than 0), find the smallest missing one from the list range.
Example: list = [2,4,6], your function will return 3, which will be the smallest one in this case.
- min( set(list( range( min(l),max(l)+1 ) )) - set(l) )
- 正常解法: 如果是已排序的array, 2分法比较中间item的值和index的大小：如果相等说明前面是连续的，则继续2分法找后面；如果大于，说明前面不连续，则继续2分法找前面。
- [参考: 剑指 Offer 53 - II. 0～n-1中缺失的数字](https://blog.algomooc.com/0532.html)

### [Palindrome](./Extra/palindrome.py) 
Palindrome: word, phrase, or sequence that reads the same backward as forward, e.g., madam or nursesrun. Given a string, find the longest substring which is palindrome. For example, if the given string is “isevilolivealive”, the output should be “evilolive”.
- 以每个char为中心，判断左右char是否相同并向外扩展。分单中心字符和双中心字符（也可以采用间隔插入一个字符比如|来变为只按单中心字符类型)

### [Max pair](./Extra/max_pair.py) 
return the number that it's the maximun pair in the array.
[1, 2, -3,3,2,-2 -4] -> 3, because 3 and -3 are max pair in the array. no found returns 0
- sorted(list), 然后循环遍历 if -item in list?
- 注意如果第一个item>0 则马上返回0

### [Mini remove](./Extra/minimum_remove.py) 
There is an array A of N integers sorted in non-decreasing order. in one move, you can either remove an integer from A or insert an integerbefore or after any element of A. The goal is to achieve an array in which all values X that are present in the array occur exactly X times.The function should return the minimum number of moves after which every value X in the array occurs exactly X times. Note that it's permissible to remove some values entirely, if appropriate.
- collections.Counter(int list)
- sum( for each int, min( add/remove times for keep it: abs(k-v), completely remove it: v ) )

### [Implement power function](./Extra/pow.py) 
Implement power(a,b) function only using +-*/
- 先写一个子函数, 子函数用于“翻倍乘法”, 次数为2^i<b
- 循环这个子函数，b每次为上一次翻倍乘法后剩下的次数。
- 注意特例b=0,1,2,负数

### [Make the brackets match](./Extra/bracket.py) 
Match the parentheses.
- 注意这个题目不是为了做演算并得出结果，而是为了检查并去除多余的括号
- 所以使用一个同样长度的array记录"去除/留下"每个括号
- 需要一个辅助stack，用于暂存左括号

### [Find k minimum given array](./Extra/offer40_k_min.py)
[来源: 剑指 Offer 40. 最小的k个数](https://blog.algomooc.com/040.html)
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入 4、5、1、6、2、7、3、8 这 8 个数字，
则最小的 4 个数字是 1、2、3、4 。
- 暴力解法: sorted(array)[:k]
- quicksort apporch: 因为找出的这 k 个数并不需要按照顺序排列。借助快速排序,不断的缩小排序的区间, 直到左区域=k

### Combine all ints to a min int
[来源: 剑指 Offer 45. 把数组排成最小的数](https://blog.algomooc.com/045.html)
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
- 第一步就先把整型数组转换为字符串数组(因为组合后的整数可能会溢出)。
- 借助quick sort算法进行排序，最后串接所有字符串为一个字符串
- 注意排序时，每一次比较两种拼接，直接字符比较就行，并选小的。比如 "30"+"3" < "3"+"30"

### [Count reversed_pair](./extra/offer51_count_reversed_pair.py)
[来源: 剑指 Offer 51. 数组中的逆序对](https://blog.algomooc.com/051.html)
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
- 借助归并排序的分而治之再两两合并思路
- 只需在合并时计数当前合并的逆序数量，最后全部加起来
- when arr1[0] > arr2[0]: count+=len(arr1) # arr1当前item>arr2当前item，意味着arr1后面的都大于arr2当前item, len是动态变化

### [Fist only one char](./Extra/first_only_one.py)
[来源: 剑指 Offer 50. 第一个只出现一次的字符](https://blog.algomooc.com/050.html)
- very simple

### Count a target that in an arry
[来源: 剑指 Offer 53 - I. 在排序数组中查找数字](https://blog.algomooc.com/053.html)
统计一个数字在排序数组中出现的次数。
- 2分法定位数字，然后以它为中心，前后扩展并计数


### Find the item(int) that appear more than half in an array
[来源: 剑指 Offer 39. 数组中出现次数超过一半的数字](https://blog.algomooc.com/039.html)
- 既然必定有一个数字超过一半的数量，那其实只能有一个
- 打擂台, 扫描每个item，比较当前数量，最后在擂台上的就是答案

### 判断5张牌是不是顺子
[来源: 剑指 Offer 61. 扑克牌中的顺子](https://blog.algomooc.com/061.html)
- 要先分析规则，根据规则实现。估计screen coding不会遇到

### 左旋转字符
[来源: 剑指 Offer 58 - II. 左旋转字符串](https://blog.algomooc.com/058.html)
- 好像这个解题思路化简为繁?

## 动态规划

### 把数字翻译成字符串, 共有多少种?
[来源: 剑指 Offer 46. 把数字翻译成字符串](https://blog.algomooc.com/046.html)
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
- dp list 记录前i个数字有多种翻译方法

### mxn棋盘格，从(1,1)->(m,n)获取礼物的最大价值
[来源: 剑指 Offer 47. 礼物的最大价值](https://blog.algomooc.com/047.html)
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
问从棋盘的左上角直到到达棋盘的右下角，不重复地走，请计算你最多能拿到多少价值的礼物？
- dp matrix (mxn), 记录每个格子的最大值，dp_matrix[m][n]就是答案
- 由于每次只能向下或者向右移动一步,位置 (i,j) 的最优解等于当前位置上方位置(i-1,j)的最优解和左侧位置(i,j-1)的最优解的较大值,再加上当前位置的值.

### [Left self out product](./Extra/left_one_out_product.py)
[来源: 剑指 Offer 66. 构建乘积数组](https://blog.algomooc.com/066.html)
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。 **不能使用除法**
- 如果可以使用除法，则先一遍遍历算出总乘积，然后另一遍除以arr[i]
- 暴力算法为双循环，O(n^2)
- 在公式 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1] 中，实际上可以划分为两个部分，从 0 到 i - 1 和从 i + 1 到 n - 1，因此，想要构建乘积数组后某下标对应元素的值，只需要求出该下标对应原数组中其左边的元素的乘积和其右边的元素的乘积，最后将两个乘积再相乘即可
- 保存会被重复计算的中间结果，具体为：leftA list保存当前元素之外，左边的累乘； rightA list保存当前元素外，右边的累乘。