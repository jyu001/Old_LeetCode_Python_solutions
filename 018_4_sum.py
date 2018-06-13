# possible problems: 
# 1. repeating keys when buiding nums[i] + nums[j], losing nums pair
# 2. if nums[i] + nums[j] and nums[i] + nums[k] sum to target, it is not right answer as nums[i] appears twice
# 3. remove duplicated quadruplets in results
#

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        map = {}
        for i in range(0,len(nums) -1):
            for j in range(i+1, len(nums)):
                a = i * len(nums) + j
                map[a] = nums[i] + nums[j]
                                                # use this way to make an index contain both i and j in one parameter
#        print map
        map2 = {}
        for key, value in map.items():
            if target - value in map2:
                index = 0
                for i, j in map.items():
                    if j == target - value:
                        index = i
                        a = key % len(nums)
                        b = key / len(nums)
                        c = index % len(nums)
                        d = index / len(nums)
                        if (a-b) * (a-c) * (a-d) * (b-c) * (b-d) * (c-d):
                                                # get original num[] numbers back from index
                            list = [nums[a], nums[b], nums[c], nums[d]]                             
                                                # sort and remove repeating answers
                            list.sort()
                            if list not in ans:
                                ans.append(list)
            map2[key] = value
        print ans

answer = Solution()
answer.fourSum([-1, 0, 2, 10, 100, -99], 11)
answer.fourSum([1, 0, -1, 0, -2, 2], 0)