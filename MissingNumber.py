# Day 4 - 15th August 2020
# This question was solved on leetcode: Question Number - 268

# The Question:

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Runtime - 148 ms - Faster than 62.34%
# Memory - 15.2 MB - Less than 20.06%


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                return nums[i]-1
        
        if nums[0]!=0:
            return 0
        else:
            return nums[len(nums)-1] + 1
