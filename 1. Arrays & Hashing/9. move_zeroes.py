# Move all zeroes to the end of the array while maintaining the relative order of non-zero elements.

# 2 pointer solution. Much faster

class Solution:

    def moveZeroes(self, nums: list[int]) -> list[int]:
        
        left = 0

        for right in range(len(nums)):
            if(nums[right] != 0):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            
        return nums

# First_submission. Not time efficient. Pythonic solution

class Solution:

    def moveZeroes(self, nums: list[int]) -> list[int]:
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums

    