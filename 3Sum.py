
# Day 2 - 13th August 2020
# This question was solved on leetcode: Question Number - 15

# The Question:

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Runtime - 976 ms - Faster than 68.40%
# Memory - 17.4 MB - Less than 34.69%

# Important Takeaway - using 'x in list' is very time consuming... makes the difference between time limit exceeded and better than 60% of responses.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            while(left<right):
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    sol = [nums[i], nums[left], nums[right]]
                    output.append(sol)
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
                
                elif total < 0:
                    left+=1
                
                else:
                    right-=1
        
        
        return output
