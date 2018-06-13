class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 0
            map[i] += 1
        map2 = {}
        for i in map:
            if map[i] not in map2:
                map2[map[i]] = [i]
            else:
                map2[map[i]].append(i)
        count = map.values()
        count.sort()
        ans = []
        for i in range(0,k):
            n = count[len(map) - i -1]
            ans.extend(map2[n])
        return ans
            
            
        
solution = Solution()
print solution.topKFrequent([1,1,1,2,2,3], 3)