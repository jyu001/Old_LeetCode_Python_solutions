class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(0,len(nums) -1):
            target = 0 - nums[0]
            nums = nums[1:]
            map = {}
            for index, value in enumerate(nums):
                if target - value in map:
                    print -target, target - value, value
                else:
                    map[value] = index

answer = Solution()
answer.threeSum([-1, 0, 1, 2, -1, -4])