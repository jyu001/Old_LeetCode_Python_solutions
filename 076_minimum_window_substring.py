class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        for i, v in enumerate(t):
            map[v] = []
        for i, v in enumerate(s):
            if v in map:
                map[v].append(i)

        #print map
        dist = {}
        count1 = 0
        count2 = 0
        count3 = 0
        start = 0
        end = 0
        for x in t:
            count1 = 100
            for lx in map[x]:
                count2 = 0
                for y in t:
                    if y != x:
                        count3 = 100
                        for j  in map[y]:
                            if j > lx and j - lx < count3:
                                count3 = j - lx
                                end = j
                    if count3 > count2 and count3 < 100:
                        count2 = count3
                if count2 < count1 and count2 > 0:
                    count1 = count2
                    start = lx
            dist[count1] = lx
        start = dist[min(dist.keys())]
        end = start + min(dist.keys())
        print s[start:end+1]
        
        
S = "ADOBECODEBANC"
T = "ABC"

solution = Solution()
solution.minWindow(S, T)
