class Solution(object):
    def lengthOfLongestSubstring_string(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxstring = s[0]
        substring = s[0]
        for i in range (1,len(s)):
            while s[i] in substring:
                if len(substring) > len(maxstring):
                    maxstring = substring
                    #print "*13", i, s[i], substring, maxstring
                #else:
                    #print "*15", i, s[i], substring, maxstring
                substring = substring[1:]  
            substring = substring + s[i]
            #print "*18", i, s[i], substring, maxstring
        return(maxstring)
        
    def lengthOfLongestSubstring(self, s): # hash table
        """
        :type s: str
        :rtype: int
        """
        map = {}
        max = 0
        count = 0 # as the lower index of the selected substring
        substr = ""
        for index, value in enumerate(s): # index as the upper index of selected substring
            while value in map.values():
                if len(map) > max:
                    max = len(map)
                    substr = map.values()
                del map[count]
                count = count + 1
                #print "37", index, value, map
            map[index] = value
            #print "39", index, value, map
        return(substr)
                
                
        
answer = Solution()
print answer.lengthOfLongestSubstring("abcabcbb")    # "abc"
print answer.lengthOfLongestSubstring("abcadbacbb")  # "bcad"
print answer.lengthOfLongestSubstring("abcadbacebb") # "dbace"
