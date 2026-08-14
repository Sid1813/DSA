# Find two numbers in the array that add up to the target and return their indices.

# O(n) solution

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if(complement in seen):
                return (seen[complement], i)
            
            seen[num] = i

# Brute Force O(n^2) solution

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return (i, j)