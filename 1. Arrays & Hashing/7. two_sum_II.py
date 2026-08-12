# Find two numbers in the array that add up to the target and return their indices; return indices in 1-based indexing.

class Solution:

    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if(complement in seen):
                return (seen[complement]+1, i+1)
            
            seen[num] = i