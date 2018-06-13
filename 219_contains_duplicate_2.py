"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j 
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        k = k + 1               # for distance 2, need to scan substring length of 3
        for i in range(0, k):
            a = nums[i]
            if a not in map:
                map[a] = 1
            else:
                return True
        for i in range(0, len(nums) - k):
            del map[nums[i]]
            a = nums[i+k]
            if a not in map:
                map[a] = 1
            else: 
                return True
        return False
        
solution = Solution()
nums = [0,1,2,5,2,1,8]

print solution.containsNearbyDuplicate(nums, 1)
print solution.containsNearbyDuplicate(nums, 2)
print solution.containsNearbyDuplicate(nums, 3)
print solution.containsNearbyDuplicate(nums, 4)
print solution.containsNearbyDuplicate(nums, 5)
