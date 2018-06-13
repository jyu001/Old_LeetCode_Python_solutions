"""
Given an array of integers, find if the array contains any duplicates. Your function should return
 true if any value appears at least twice in the array, and it should return false if every element 
 is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in nums:
            if i in map:
                return True
            else: 
                map[i] = 1
        return False
        
        
solution = Solution()
nums = [9,0,8,0,1,2,3,4,5,0,6,0]
print solution.containsDuplicate(nums)
