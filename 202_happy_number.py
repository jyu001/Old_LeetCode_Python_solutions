"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        for count in range(0,100):
            sq = 0
            for i in s:
                n = int(i)
                sq = sq + n * n
            if sq == 1:
                return True
            if sq == 4:
                return False
            s = str(sq)
            print s,
        
solution = Solution()
print solution.isHappy(19)
print solution.isHappy(5)
print solution.isHappy(6)
print solution.isHappy(9999)

