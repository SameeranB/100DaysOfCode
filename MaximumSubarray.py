# Day 3 - 14th August 2020
# This question was solved on leetcode: Question Number - 53

# The Question:

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


# Runtime - 80 ms - Faster than 43.76%
# Memory - 14.6 MB - Less than 41.68%

# Approach - Greedy -> See if the previous sum makes the total sum better, or does the current one make it better alone... (Refer to Leetcode Discussions)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if sorted(nums)[len(nums)-1] == 0:
            return 0
        
        if sorted(nums)[len(nums)-1] < 0:
            return sorted(nums)[len(nums)-1]
        
#         Now it's a mix of negatives and positives
            
        newNum = maxSum = nums[0]
        
        for i in range(1, len(nums)):
            newNum = max(nums[i], newNum + nums[i])
            maxSum = max(newNum, maxSum)
        
        return maxSum
