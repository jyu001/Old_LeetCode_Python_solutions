"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        num1 = ""
        order = 0
        for i in s:
            if i not in map:
                order = order + 1
                map[i] = order
            num1 = num1 + str(map[i])
        map = {}
        num2 = ""
        order = 0
        for i in t:
            if i not in map:
                order = order + 1
                map[i] = order
            num2 = num2 + str(map[i])
        print num1, num2 ,
        for i in range (0,len(num1)):
            if num1[i] != num2[i]:
                return False
        return True
        
solution = Solution()

print solution.isIsomorphic("egg","add")
print solution.isIsomorphic("foo","bar")
print solution.isIsomorphic("paper","title")
