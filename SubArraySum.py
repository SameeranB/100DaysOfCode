# This question was solved on leetcode: Question Number - 523

# The Question:

# Given a list of non-negative numbers and a target integer k, 
# write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k,
# that is, sums up to n*k where n is also an integer.

# Runtime - 776ms - Faster than 21.31%
# Memory - 14.2MB - Less than 24.99%


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            if "00" in ''.join(map(str, nums)):
                return True
            else :
                return False

        for i in range(len(nums)):
            currentSum = nums[i]
            for j in range(i+1, len(nums)):
                currentSum+=nums[j]
                if currentSum%k == 0:
                    return True
                
        
        return False
