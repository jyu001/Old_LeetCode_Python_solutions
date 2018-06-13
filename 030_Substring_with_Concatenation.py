"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        answer = []
        n = len(words)
        for i in range (0,3):
            # first turn s into array of three letter combinations
            list = []
            comb = ""
            for index in range(0,len(s)):
                char = s[index]
                comb = comb + char
                if index % 3 == 2:
                    list.append(comb)
                    comb = ""
            print list
            # now turn list into hash map
            map = {}
            for index in range(0, len(list)):
                comb = list[index]
                map[index] = comb
                if index >= n - 1:
                    detect = 1
                    for word in words:
                        if word not in map.values():
                            detect = 0
                            break
                    if detect == 1:
                        answer.append(index * 3 - 3 + i)
                    del map[index + 1 - n]
            s = s[1:]
        print "the answer for" + s + "is: "
        print answer
                
        
solution = Solution()
solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
solution.findSubstring("barfoothefoobarmanbarafoobarfoofoobar", ["foo", "bar"])





"""
because word length is 3 letters, we only need to iterate 3 cases: 

'bar' | 'foo' | 'the' | 'foo' | 'bar' | 'man'
'arf' | 'oot' | 'hef' | 'oob' | 'arm'
'rfo' | 'oth' | 'efo' | 'oba' | 'rma'

"""