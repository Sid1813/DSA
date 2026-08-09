# Find two numbers in the array that add up to the target and return their indices.

class Solution:

    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if(complement in seen):
                return (seen[complement], i)
            
            seen[num] = i