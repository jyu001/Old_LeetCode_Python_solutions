"""
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""



class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        list = []
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if j - i:
                    new = words[i] + words[j]
                    n = len(new)
                    check = True
                    for k in range(0,len(new)/2):
                        if new[k] != new[n-k-1]:
                            check = False
                            break
                    if check:
                        list.append([i,j])
        return list
        
        
solution = Solution()
print solution.palindromePairs(["bat", "tab", "cat"])
print solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])