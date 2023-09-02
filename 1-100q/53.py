'''
	Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

	Example:

	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0

        currSum, result = nums[0], nums[0]

        for index in range(1, len(nums)):
        	currSum = max(nums[index], currSum+nums[index])
        	result = max(result, currSum)

        return result

# 可以这样理解：遍历每个item, 对于当前item，前面的sum是不是当前item的累赘(就是前面的sum是不是>0),
# 如果前面的sum<0，那就舍弃前面的sum，新的sum从当前item开始. 可以保留每移动一步新update后的sum，然后max(list_of_sums)
# [-2,1,-3,4,-1,2,1,-5,4]
# sums=[-2, 1, -2, 4, 3, 5, 6, 1, 5], max(sums)=6
arr=[-2,1,-3,4,-1,2,1,-5,4]
res=Solution().maxSubArray(arr)
print(res)