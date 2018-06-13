"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        for i in s:
            if i not in map:
                map[i] = 0
            map[i] += 1
        for j in t:
            if j not in map:
                return False
            map[j] -= 1
            if map[j] == 0:
                del map[j]
        return True
        
solution = Solution()

print solution.isAnagram("anagram","nagaram")
print solution.isAnagram("rat","car")