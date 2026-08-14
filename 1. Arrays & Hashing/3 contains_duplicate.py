# Check whether any number appears more than once in the array.

# DSA solution

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
        
            seen.add(num)
        
        return False

# Pythonic solution

class Solution:
    
    def containsDuplicate(self, nums: list[int]) -> bool:

        if (len(nums) == len(set(nums))):
            return False
        else:
            return True