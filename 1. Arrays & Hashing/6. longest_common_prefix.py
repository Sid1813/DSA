# Longest Common Prefix: Find the longest starting substring shared by all strings in the array.

# Version 2 (Better Solution)

class Solution:

    def longestCommonPrefix(self, words: list[str]) -> str:

        smallest = min(words, key = len)
        for word in words:
            while smallest != word[:len(smallest)]:
                smallest = smallest[:-1] # smallest[:-1] --> Python string slicing to obtain everything but the last letter in smallest
        return smallest

# Version 1 (First Solution)

class Solution:

    def longestCommonPrefix(self, words: list[str]) -> str:

        lst = []; common_prefix = ""
        smallest = min(words, key = len)

        for i in range(len(smallest)): # len(smallest) because common prefix CANNOT be longer than the smallest word in words
            for word in words:
                lst.append(word[i]) # This inner loop iterates through all words and appends letter at index 0,1,2... len(word)-1 of each word in list - words
            if(len(set(lst)) == 1):
                common_prefix += word[i] # if the if condition holds true, that clearly means that the letter at i index is same/common for all words, therefore add it to common prefix
            else:
                return common_prefix # if the above if condition does NOT hold true, that means there is a mismatch in letters between the words at index i. Therefore we return whatever common prefix we have so far
            lst = [] # This is to ensure list - lst starts from scratch to now compare the letters at the next index of each word in words
        return common_prefix # This return is for, if the else statement had not been triggered even once thoughout all iterations of the loop i.e if the smallest word in words IS the common prefix amongst every word in words
                


            





            

