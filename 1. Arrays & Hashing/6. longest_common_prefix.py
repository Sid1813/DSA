# Longest Common Prefix: Find the longest starting substring shared by all strings in the array.

# Version 2 (Better Solution)

class Solution:
    def longestCommonPrefix(self, words):
        smallest = min(words, key = len)
        for word in words:
            while smallest != word[:len(smallest)]:
                smallest = smallest[:-1]
        return smallest

# Version 1 (First Solution)

class Solution:
    def longestCommonPrefix(self, words):
        lst = []; common_prefix = ""
        smallest = min(words, key = len)
        for i in range(len(smallest)):
            for word in words:
                lst.append(word[i])
            if(len(set(lst)) == 1):
                common_prefix += word[i]
            else:
                return common_prefix
            lst = []
        return common_prefix
                


            





            

