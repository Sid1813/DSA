# Valid Palindrome: Determine whether a string reads the same forward and backward, ignoring non-alphanumeric characters and case.

class Solution:

    def isPalindrome(self, s: str) -> bool:
        
        lst = []
        for character in s:
            if character.isalnum():
                character = character.lower()
                lst.append(character)

        for i in range(len(lst)//2):
            if lst[i] != lst[len(lst)-i-1]:
                return False
        return True