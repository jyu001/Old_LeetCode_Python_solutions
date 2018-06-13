class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print nums 
        print "target is " + str(target)
        map = {}
        for index, value in enumerate(nums):
            if target - value in map:
                return[map[target - value], index]
            else:
                map[value] = index

answer = Solution()
print answer.twoSum([2,7,11,15],18)   
