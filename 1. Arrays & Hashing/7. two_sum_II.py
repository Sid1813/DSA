# Find two numbers in the array that add up to the target and return their indices; return indices in 1-based indexing.

# underlying 2 pointer pattern DSA solution :

class Solution:

    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while(left < right):

            if(numbers[left] + numbers[right] < target):
                left += 1

            elif(numbers[left] + numbers[right] > target):
                right -= 1

            else:
                return left + 1, right + 1
            
# slightly updated unordered 2 sum solution :

class Solution:

    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if(complement in seen):
                return (seen[complement]+1, i+1)
            
            seen[num] = i