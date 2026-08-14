# Valid Anagram: Determine whether two strings contain the same characters with the same frequencies.

class Solution:
    
    def isAnagram(self, word1: str, word2: str) -> bool:

        dict1 = {}; dict2 = {}

        for character in word1:
            if character in dict1:
                dict1[character] += 1
            else:
                dict1[character] = 1

        for character in word2:
            if character in dict2:
                dict2[character] += 1
            else:
                dict2[character] = 1

        if dict1 == dict2:
            return True
        else:
            return False
    