# Remove duplicates from a sorted array in-place and return the count of unique elements.

class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:

        left = 0

        for right in range(1, len(nums)):

            if(nums[left] != nums[right]):
                left += 1
                nums[left] = nums[right]

        return left + 1

        