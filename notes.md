# Notices
> 如果找不到好的方法，要马上转入做 brute force solution

* [剑指 Offer](https://blog.algomooc.com/)(java, 题目不完全同leetcode对应) 
* [java leetcode中文](https://github.com/MisterBooo/LeetCodeAnimation)
* 结合本repository看python实现([forked from](https://github.com/Garvit244/Leetcode)): Python solution of problems from [LeetCode](https://leetcode.com/).
* 大部分额外添加的题目在Extra中
  
# 其他python相关leetcode资源:
* https://zhenyu0519.github.io/categories/#Linked-List
* https://github.com/youngyangyang04/leetcode-master

# Data structure and general algo in Python
* [TheAlgorithms in python](https://github.com/TheAlgorithms/Python)
* [Python 标准内置类1](https://www.cnblogs.com/paulwhw/articles/12304977.html)
* [Python 标准内置类2](https://zhuanlan.zhihu.com/p/69487899)
* [自己手动实现](https://nemo.cool/254.html)

#### [1. BST (binary search tree)](Extra/bst.py)
二叉搜索树是一棵有序的二叉树: 1、若它的左子树不为空，那么左子树上的所有值均小于它的根节点; 2、若它的右子树不为空，那么右子树上所有值均大于它的根节点; 3、它的左子树和右子树也都是二叉搜索树

#### [2. Heap (堆)](Extra/heap.py)
堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。

#### [3. Time complexities of sort algorithms](https://segmentfault.com/a/1190000021638663)

#### [4. Quick Sort](./Extra/quick_sort.py)

#### [5. Merge Sort](./Extra/merge_sort.py)

# Questions:
前几道经典题的动画解析: https://github.com/MisterBooo/LeetCodeAnimation

## Extra
### 202306
[stock profits](./Extra/202306/stock.py)
### 202309
[reduce_abc.py](./Extra/202309/reduce_abc.py)
[cache_fibonacci.py](./Extra/202309/cache_fibonacci.py)
[simple torch gradient](./Extra/202309/simple_torch.py)
[use argparse](./Extra/202309/use_argparse.py)
### 202310
[56_merge_intervals.py](./Extra/202310/56_merge_intervals.py)
[987_vertical_order_traversal_bt.py](./Extra/202310/987_vertical_order_traversal_bt.py)
[1265_Print_Immutable_Linked-List_in_Reverse.py](./Extra/202310/1265_Print_Immutable_Linked-List_in_Reverse.py)

## Finance
[Calculate compound rate](./Finance/calculate_compound_rate.py)

## Leetcode
### [Leetcode NO.1 TwoSum](./1-100q/01_TwoSum.py)
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
![TwoSum](https://camo.githubusercontent.com/c8a78a4da1b40f98100cec12b6dc724e6159ab9859135dab3b87473e7374353e/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f61763437762e676966)
- map辅助，扫描一遍，看(target-arr[i])是否在map中
- 如果是已排序，并且不用map辅助，可以先2分法找到<=target的index作为right指针，然后只在前半部分找。left->, <-right [参考: 剑指 Offer 57. 和为s的两个数字](https://blog.algomooc.com/057.html)
- 但是如果使用map辅助，不管是不是排序了的array，第二个解法似乎不占优势。

### [Leetcode NO.2 AddTwoNumbers (linked list)](./1-100q/02.py)
题目来源于 LeetCode 上第 2 号问题：两数相加。题目难度为 Medium，目前通过率为 33.9%. 
给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
![NO.2](https://camo.githubusercontent.com/56a78d49fe71daeb64a888d5167e0e924127f94ff670c48871825ce634c38820/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f667a3933332e676966)

### [Leetcode NO.3 Longest Substring Without Repeating Characters](./1-100q/03.py) 给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。
建立一个256位大小的整型数组 freg (python为map)，用来建立字符和其出现位置之间的映射。维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
- （1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
- （2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
- （3）重复（1）（2），直到左边索引无法再移动；
- （4）维护一个结果res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。

更具体：mapSet记录(更新)遍历过程中的各char，值为最后一次出现的位置+1, 遍历的下一个char是否在mapSet中? 不在其中则窗口右侧(end指针)加一; 
如果已在其中，说明这个char之前出现过，更新start = max(mapSet[s[end]], start)，这statement包含两种可能：
1. 之前出现过并且在当前window中，start变为之前出现过的(位置+1)，相当于缩小window.
2. 之前出现过但是没有在当前window，start不用变(但更新mapset中这个char的位置+1)
![NO.3](https://camo.githubusercontent.com/4d78fd6ac2ffe9559d2188efb0dd57a95f5aeb3c831653ce186777eb5ed298b9/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f76786137662e676966)

### [Leetcode NO.9 Palindrome Number](./1-100q/09.py)
判断一个整数是否是回文数:
loop循环, 每次num去头去尾. 去头num % 10 ** (l - i + 1), 去尾// 10 ** (i - 1), 然后比较num的头==尾(num // 10 ** (l - 1) == num % 10)
![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/v3tkl.gif)

### [Leetcode NO.53 Max sum of contiguous subarray](./1-100q/53.py) 
[参考: 剑指 Offer 42. 最大和的连续子数组](https://blog.algomooc.com/042.html)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- 可以这样理解：遍历每个item, 对于当前item，前面的sum是不是当前item的累赘(就是前面的sum是不是>0),
- 如果前面的sum<0，那就舍弃前面的sum，新的sum从当前item开始. 可以保留每移动一步新update后的sum，然后max(list_of_sums)
![NO.53](https://camo.githubusercontent.com/4d78fd6ac2ffe9559d2188efb0dd57a95f5aeb3c831653ce186777eb5ed298b9/68747470733a2f2f626c6f672d313235373132363534392e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f626c6f672f76786137662e676966)

## Company exams
### [1. Smallest missing](./Extra/smallest_missing.py)
Given a list of positive integers (greater than 0), find the smallest missing one from the list range.
Example: list = [2,4,6], your function will return 3, which will be the smallest one in this case.
- min( set(list( range( min(l),max(l)+1 ) )) - set(l) )
- 正常解法1: 如果是已排序的array, 2分法比较中间item的值和index的大小：如果相等说明前面是连续的，则继续2分法找后面；如果大于，说明前面不连续，则继续2分法找前面，这时不需要管后面连续不连续。
- 正常解法2: 如果是未排序的array, 参考quick sort, 在每次完成pivot排序后，判断pivot的值和它的index，如果value==index+1则说明左边正常，要去右边找，不然左边找。
- [参考: 剑指 Offer 53 - II. 0～n-1中缺失的数字](https://blog.algomooc.com/0532.html)

### [2. Palindrome](./Extra/palindrome.py) 
Palindrome: word, phrase, or sequence that reads the same backward as forward, e.g., madam or nursesrun. Given a string, find the longest substring which is palindrome. For example, if the given string is “isevilolivealive”, the output should be “evilolive”.
- 以每个char为中心，判断左右char是否相同并向外扩展。分单中心字符和双中心字符（也可以采用间隔插入一个字符比如|来变为只按单中心字符类型)
- 动态规划解法: dp[i,j]=dp[i+1,j-1] if str[i]==str[j] else 0
- [manacher](https://www.cxyxiaowu.com/2869.html)

### [3. Max pair](./Extra/max_pair.py) 
return the number that it's the maximun pair in the array.
[1, 2, -3,3,2,-2 -4] -> 3, because 3 and -3 are max pair in the array. no found returns 0
- sorted(list), 然后循环遍历 if -item in list?
- 注意如果第一个item>0 则马上返回0

### [4. Mini remove](./Extra/minimum_remove.py) 
There is an array A of N integers sorted in non-decreasing order. in one move, you can either remove an integer from A or insert an integerbefore or after any element of A. The goal is to achieve an array in which all values X that are present in the array occur exactly X times.The function should return the minimum number of moves after which every value X in the array occurs exactly X times. Note that it's permissible to remove some values entirely, if appropriate.
- collections.Counter(int list)
- sum( for each int, min( add/remove times for keep it: abs(k-v), completely remove it: v ) )

### [5. Implement power function](./Extra/pow.py) 
Implement power(a,b) function only using +-*/
- 先写一个子函数, 子函数用于“翻倍乘法”, 次数为2^i<b
- 循环这个子函数，b每次为上一次翻倍乘法后剩下的次数。
- 注意特例b=0,1,2,负数

### [6. Make the brackets match](./Extra/bracket.py) 
Match the parentheses.
- 注意这个题目不是为了做演算并得出结果，而是为了检查并去除多余的括号
- 所以使用一个同样长度的array记录"去除/留下"每个括号
- 需要一个辅助stack，用于暂存左括号

### [7. Merge two arrays](./Extra/merge_two_arrays.py) 
Merge two sorted arrays, return the array with unique items.
- simple

### [8. Cut woods](./Extra/cutting_woods.py) 
[Leetcode: cut woods](https://leetcode.com/discuss/interview-question/354854/)
We have n pieces of wood, with known lengths (integer array L). We need k pieces of wood with equal length. What's the maximum integer length?.
- 笨办法: max_value=max(L), 然后开始O(n^2) loop, max_value递减，看能不能达到k个
- 改进一点: max_value=sum(L) // k , 然后从max_value递减开始尝试
- 使用2分法: 
- 原始2分法是, 给你一个数字，在一个有序数组中找到它的位置
- 这里是递增有序数组[1..max_v], 你要找到满足一定条件的item, 并且可以根据条件值分两边再找
- 当当前value的划分计数大于k时，说明要在右边找，如果小于则在左边找。
- 这里对L从大到小排序会让平均复杂度降低

### [9. Minimize heaviest first box](./Extra/minimize_heaviest_first_box.py)
将一个integer array拆分为两个array，返回第一个array。
要求第一个array的sum大于第二个的同时个数最少。
arr1和arr2不能有交集，并且完全划分原array
- 要慎用python的一些函数，比如这里每次都用sum函数的话, 数量大的array就会超时
- 从小到大排序，然后从最后一个元素开始遍历，查看每次分割，右边sum是不是大于左边sum
- 排序后可以使用二分法

### [10. Related group num](./Extra/related_group_num.py)
一个nxn matrix表示row元素i是否有送东西给col元素j, 1表示送，0表示没有送, m[i,i]=1
求联通子图个数 （就是有送东西关系的连接为一个子图)
- 通过set(idx)开始, sets_map[idx]->init_set, 扫描每行每列，不断合并set，最后set个数就是答案
- sets_map[i].update(sets[j]); sets_map[j]=sets_map[i];

### [11. Max exponential series length](./Extra/max_exponential_series.py)
输入integer数组, 输出能形成[x1, x2=x1*x1, x3=x2*x2, ...], x_i in input arr 的这种数组的最大长度
- 先排序，先形成map[item]=item
- 遍历每个item，查cur*=cur 是否在map中，找出最大的count
- 优化: 因为排过序，所以最外层loop的item如果曾经被count过，就直接跳过。

### [12. Find total imbalance](./Extra/find_total_imbalance.py)
Input integer array, all item are unique，
找出所有连续sub-array（至少2个，并不打乱原始顺序）下，跳跃数量.
example: [4,1,3,2], 
all consecutive array = [ [4,1], [1,3], [3,2], [4,1,3], [1,3,2], [4,1,3,2] ]
jump_count  =               1    + 1     + 0    + 1      + 0      + 0  = 3
这里的跳跃数量指，某个数组在变成排序后，不连续的次数, 
example: [4,1,3,2] -> [1,2,3,4] -> 0 jump; [4,1] -> [1,4] -> 1 jump.
- 借鉴merge_sort, 循环做两两合并，合并的时候计算跳跃数；
- 同merge_sort最大的区别，不能二分法

### [13. Sum is closest to zero](./Extra/sum_closest_to_zero.py)
An Array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero.
For the below array, program should print -80 and 85.
Solution:
- 最重要的是先按绝对值排序
- quicksort: O(nlogn)

## 剑指 Offer
### 1. 找出数组中重复的数字
[来源: 剑指 Offer 03. 数组中重复的数字](https://blog.algomooc.com/003.html)
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
- map辅助,使索引与值一一对应，即索引 0 的值为 0，索引 1 的值为 1。而一旦某个索引的值不只一个，则找到了重复的数字，也即发生了 哈希冲突

### 2. 二维数组中的查找
[来源: 剑指 Offer 04. 二维数组中的查找](https://blog.algomooc.com/004.html)
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
- 仔细观察矩阵，可以发现：左下角元素为所在列最大元素，所在行最小元素
- 如果 左下角元素 大于了目标值，则目标值一定在该行的上方， 左下角元素 所在行可以消去。
- 如果 左下角元素 小于了目标值，则目标值一定在该列的右方， 左下角元素 所在列可以消去。

具体操作为从矩阵左下角元素开始遍历，并与目标值对比：
- 当 matrix[i][j] > target 时： 行索引向上移动一格（即 i--），即消去矩阵第 i 行元素；
- 当 matrix[i][j] < target 时： 列索引向右移动一格（即 j++），即消去矩阵第 j 列元素；
- 当 matrix[i][j] == target 时： 返回 true。
- 如果越界，则返回 false。

### 3. 用两个栈实现一个队列
[来源: 剑指 Offer 09. 用两个栈实现队列](https://blog.algomooc.com/009.html)
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
- 用两个stack实现
- 入队操作: 如果是栈的插入操作，那我们可以把元素都先插入到 stack1 中，也就实现了队列的 入队操作 。stack1.push(value)
- 出队操作: 
- 1.当 stack2 中不为空时，直接操作，此时在 stack2 中的栈顶元素是最先进入队列的元素，返回该元素即可, stack2.pop()；
- 2.如果 stack2 为空且 stack1 也为空，返回 -1；
- 3.如果 stack2 为空且 stack1 不为空，首先需要把 stack1 中的元素逐个弹出并压入到 stack2中: loop stack2.push(stack1.pip()))，然后返回stack2 的栈顶元素即可: stack2.pop()。

### 4. 旋转数组的最小数字
[来源: 剑指 Offer 11. 旋转数组的最小数字](https://blog.algomooc.com/011.html)
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为 1。
- 被旋转过的数字，存在一个差异大于1的异常分割点，异常点的右边就是最小值
- 2分法查找，如果mid > right,意味着异常点肯定是发生在 [ mid + 1 , right ] 这个区间的
- 如果mid < right, 异常点发生在 [ left , mid ] 这个区间

### 5. 判断在一个矩阵中是否存在一条包含某字符串所有字符的路径
[来源: 剑指 Offer 12. 矩阵中的路径](https://blog.algomooc.com/012.html)
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。

如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"], ["s","f","c","s"], ["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

- 两层循环，最外层遍历矩阵所有字符,针对每个匹配到str首字符的情况，进入下一层循环
- 内层循环，根据str下一个字符（recursive方式）游走（上左下右），
- 为了保证不重复访问节点，可以将这条路径上已经访问过的节点，修改为不在 str 当中的一个字符
- 修改完后会出现一种情况，当前的节点元素与目标元素相匹配，但是在它的四个方向的节点中都找不到可以匹配到目标下一元素的节点。这时需要把这个点回退(recursive自动退回)，根据之前的操作，当前的节点被修改为了 #，所以为了能够回退成功，再回退操作前需要重新将 # 修改回原来的元素。

### 6. 调整数组顺序使奇数位于偶数前面
[来源: 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://blog.algomooc.com/021.html)
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
- left, right 指针，走走停停，互相交换
- while left<right:
- in loop: while(left < right && (nums[left] & 1) == 1) left++;
- in loop: while(left < right && (nums[right] & 1) == 0) right--;
- in loop: nums[left] <-> nums[right];

### 7. 包含min函数O(1)的栈
[来源: 剑指 Offer 30. 包含min函数的栈](https://blog.algomooc.com/030.html)
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数，在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
- 要求O(1)，那么只能使用辅助空间进行存储，这是一种空间换时间的思想
- 设置两个栈：普通栈和辅助栈
- push 操作: 普通栈：直接添加 push 进来的值,辅助栈：每次 push 一个新元素的时候，将普通栈中最小的元素 push 进辅助栈中
- pop 操作: 普通栈：直接移除普通栈中的栈顶元素, 辅助栈：判断普通栈中刚刚移除的栈顶元素值是否和此时辅助栈中的栈顶元素相同，如果是则将辅助栈中的栈顶元素移除，否则不执行操作，这样的目的是为了让辅助栈中的栈顶元素始终是普通栈中的最小值
- getMin 操作:返回辅助栈的栈顶元素


### 8. [Find k minimum given array](./Extra/offer40_k_min.py)
[来源: 剑指 Offer 40. 最小的k个数](https://blog.algomooc.com/040.html)
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入 4、5、1、6、2、7、3、8 这 8 个数字，
则最小的 4 个数字是 1、2、3、4 。
- 暴力解法: sorted(array)[:k]
- quicksort apporch: 因为找出的这 k 个数并不需要按照顺序排列。借助快速排序,不断的缩小排序的区间, 直到左区域=k

### 9. Combine all ints to a min int
[来源: 剑指 Offer 45. 把数组排成最小的数](https://blog.algomooc.com/045.html)
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
- 第一步就先把整型数组转换为字符串数组(因为组合后的整数可能会溢出)。
- 借助quick sort算法进行排序，最后串接所有字符串为一个字符串
- 注意排序时，每一次比较两种拼接，直接字符比较就行，并选小的。比如 "30"+"3" < "3"+"30"

### 10. [Count reversed_pair](./Extra/offer51_count_reversed_pair.py)
[来源: 剑指 Offer 51. 数组中的逆序对](https://blog.algomooc.com/051.html)
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
- 借助归并排序的分而治之再两两合并思路
- 只需在合并时计数当前合并的逆序数量，最后全部加起来
- when arr1[0] > arr2[0]: count+=len(arr1) # arr1当前item>arr2当前item，意味着arr1后面的都大于arr2当前item, len是动态变化

### 11. [First only one char](./Extra/first_only_one.py)
[来源: 剑指 Offer 50. 第一个只出现一次的字符](https://blog.algomooc.com/050.html)
- very simple

### 12. Count a target that in an arry
[来源: 剑指 Offer 53 - I. 在排序数组中查找数字](https://blog.algomooc.com/053.html)
统计一个数字在排序数组中出现的次数。
- 2分法定位数字，然后以它为中心，前后扩展并计数


### 13. Find the item(int) that appear more than half in an array
[来源: 剑指 Offer 39. 数组中出现次数超过一半的数字](https://blog.algomooc.com/039.html)
- 既然必定有一个数字超过一半的数量，那其实只能有一个
- 打擂台, 扫描每个item，比较当前数量，最后在擂台上的就是答案

### 14. 判断5张牌是不是顺子
[来源: 剑指 Offer 61. 扑克牌中的顺子](https://blog.algomooc.com/061.html)
- 要先分析规则，根据规则实现。估计screen coding不会遇到

### 15. 左旋转字符
[来源: 剑指 Offer 58 - II. 左旋转字符串](https://blog.algomooc.com/058.html)
- 这个题有问题，好像这个解题思路化简为繁了? 实际只需str[k:]+str[:k]

## 16. 其他linkedList操作和Tree
[参考<剑指 Offer>相关](https://blog.algomooc.com/)

## 动态规划

### 1. 把数字翻译成字符串, 共有多少种?
[来源: 剑指 Offer 46. 把数字翻译成字符串](https://blog.algomooc.com/046.html)
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
- dp list 记录前i个数字有多种翻译方法
- 如果i-1和i的组合在10和25之间，说明翻译方法除了i本身，还要加上i-1: dp[i] = dp[i - 1] + dp[i - 2]
- 不然dp[i]=dp[i-1]
- 返回dp[-1]

### 2. m*n棋盘格，从(1,1)->(m,n)获取礼物的最大价值
[来源: 剑指 Offer 47. 礼物的最大价值](https://blog.algomooc.com/047.html)
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
问从棋盘的左上角直到到达棋盘的右下角，不重复地走，请计算你最多能拿到多少价值的礼物？
- dp matrix (mxn), 记录每个格子的最大值，dp_matrix[m][n]就是答案
- 由于每次只能向下或者向右移动一步,位置 (i,j) 的最优解等于当前位置上方位置(i-1,j)的最优解和左侧位置(i,j-1)的最优解的较大值,再加上当前位置的值.

### 3. [Left self out product](./Extra/offer_66_left_self_out_product.py)
[来源: 剑指 Offer 66. 构建乘积数组](https://blog.algomooc.com/066.html)
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。 **不能使用除法**
- 如果可以使用除法，则先一遍遍历算出总乘积，然后另一遍除以arr[i]
- 暴力算法为双循环，O(n^2)
- 在公式 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1] 中，实际上可以划分为两个部分，从 0 到 i - 1 和从 i + 1 到 n - 1，因此，想要构建乘积数组后某下标对应元素的值，只需要求出该下标对应原数组中其左边的元素的乘积和其右边的元素的乘积，最后将两个乘积再相乘即可
- 保存会被重复计算的中间结果，具体为：leftA list保存当前元素之外，左边的累乘； rightA list保存当前元素外，右边的累乘。

### 4. [回文动态规划 Palindrome](./Extra/palindrome.py) 
- dp[i,j]=dp[i+1,j-1] if str[i]==str[j] else 0

### 5. [厉害了我的杯](https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247484557&idx=1&sn=739d80488fe1169a9c9ca26ecfcdfba6&chksm=fa0e6b0ccd79e21a1c2b0d99db69f6206cddddfe2367742e9de1d7d17ec35a5ce29fa4e30d63&token=110841213&lang=zh_CN#rd)

### 5. [Longest common string](./Extra/LCS.py)
![LCS example](https://www.geeksforgeeks.org/wp-content/uploads/Longest-Common-Subsequence.png)
- Consider the input strings “AGGTAB” and “GXTXAYB”. Last characters match for the strings. So length of LCS can be written as: 
L(“AGGTAB”, “GXTXAYB”) = 1 + L(“AGGTA”, “GXTXAY”) 
- Consider the input strings “ABCDGH” and “AEDFHR. Last characters do not match for the strings. So length of LCS can be written as: 
L(“ABCDGH”, “AEDFHR”) = MAX ( L(“ABCDG”, “AEDFHR”), L(“ABCDGH”, “AEDFH”) )
