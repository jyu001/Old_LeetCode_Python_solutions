"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # idea 1 : build a hashmap for every non 0 dots, key is the index, value is a hash map, {i, j} i is the width, j is depth
        # calculate the max square available from each dot this way:
        # let width = 1, scan the dot below dot x, if it is 1, then depth 1 -> 2, and mark this dot y,
        # let y {i, j} has value 1: 1 too, when we iterate to dot y, it ignores the width 1 scan as key 1 exists
        # let width = w, (all w - 1 dots on the right of dot x is 1)
        # scan depth 2, if for all w-1 dots, it is still 1, then for dot x, change value {2: 1} to {2: 2} and then
        # also mark the value of all w-1, dots on 2nd layer with {w: 1}
        # 
        # idea 2: iterate
        # 1: find 0's, and then devide matrix into up, down, left, right four zones. iterate for each. 
        #
        all = []
        for i in matrix:
            all.extend(i)
        print all
        row = len(matrix)           # number of rows
        col = len(all)/len(matrix)  # number of columns
        # print row
        nums = []
        for index, value in enumerate(all):
            nums.append(int(value))
        print "answer: ", 
        print self.check(nums, col, 0, row, 0, col)
        
    def check(self, nums, ncol, rowu, rowd, coll, colr):
        # nums is the original nums, rowl, colu is minimum index of row, col, rowr, cold are maximum number + 1 or row/col
        if rowu == rowd or coll == colr:
            return 0
        for i in range(rowu, rowd):
            for j in range(coll, colr):
                index = i * ncol + j
                if nums[index] == 0:
                    return max(self.check(nums, ncol, rowu, i, coll, colr), self.check(nums, ncol, i+1, rowd, coll, colr), \
                    self.check(nums, ncol, rowu, rowd, coll, j), self.check(nums, ncol, rowu, rowd, j+1, colr))
        #print rowd, rowu, colr, coll
        return (rowd-rowu)*(colr-coll)
            
        
solution = Solution()
matrix = [    "01101",
              "11010",
              "01110",
              "11110",
              "11111",
              "00000"]
solution.maximalRectangle(matrix)
matrix = [    "111",
              "011",
              "111",]
solution.maximalRectangle(matrix)
