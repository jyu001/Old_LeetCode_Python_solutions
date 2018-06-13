class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        #print citations 
        j = 0
        for i in range(0,len(citations)):
            #print i, citations[i]
            if citations[i] <= (len(citations) - i):
                j = citations[i]
        return j
        
solution = Solution()
print solution.hIndex([3, 0, 6, 1, 5,10,7,2,8])
print solution.hIndex([3, 0, 6, 1, 5])