"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = {}
        ans = []
        if n == 1:
            return "please input a number larger than 1"
        for x in range(2,n):
            m = math.sqrt(n)
            check = 1
            for j in map:
                if j < m: 
                    if x%j == 0:
                        check = 0
                        break
            if check:
                map[x] = 1
                ans.append(x)
        return len(ans)
            
solution = Solution()

import math

print solution.countPrimes(6)
print solution.countPrimes(10000)