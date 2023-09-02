'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

    维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
    - （1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
    - （2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
    - （3）重复（1）（2），直到左边索引无法再移动；
    - （4）维护一个结果res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。
    更具体：mapSet记录(更新)遍历过程中各char最后一次出现的位置+1, 遍历的下一个char是否在mapSet中?不在其中则窗口右侧(end指针)加一，如果已在其中，
    说明这个char之前出现过，两种可能：
    1.之前出现过并且在当前window中，start变为之前出现过的(位置+1)
    2.之前出现过但是没有在当前window，start不用变(但更新mapset中这个char的位置+1)

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapSet = {} # mapSet记录遍历过程中各char最后一次出现的(位置+1)
        start, result = 0, 0

        for end in range(len(s)):
        	if s[end] in mapSet: 
                # 说明这个char之前出现过，两种可能：
                # 1.之前出现过并且在当前window中，start变为之前出现过的(位置+1)，相当于缩小window
                # 2.之前出现过但是没有在当前window，start不用变 (但更新mapset中这个char的位置+1)
        		start = max(mapSet[s[end]], start)
        	result = max(result, end-start+1) # end-start+1 = window
        	mapSet[s[end]] = end+1 #记录(更新)当前char的(位置+1)

        return result 

print(Solution().lengthOfLongestSubstring("abcadbcbb"))