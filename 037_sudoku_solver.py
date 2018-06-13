class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        listall = []
        n = 0
        for lista in board:
            for index, value in enumerate(lista):
                if value != ".":
                    #count = index + n * 9 
                    num= int(value)
                    listall.append(num)
                else: 
                    listall.append(0)
            n = n + 1
#        print listall
        map = {}
        for i in range (0, 81):
            if listall[i] == 0:
                map[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        solved = 0
        while len(map) > 0: 
            for i in map:
                for index, value in enumerate(listall): # vertical
                    if index % 9 == i % 9 and value in map[i] :
                        map[i].remove(value)
                for index, value in enumerate(listall): # horizontal
                    if index / 9 == i / 9 and value in map[i]  :
                        map[i].remove(value)
                for index, value in enumerate(listall): # square
                    a = index % 9
                    b = index / 9
                    if (a / 3 + (b / 3) * 3) == ((i % 9)/3 + ((i / 9)/3) * 3 ) and value in map[i]  :
                        map[i].remove(value)

                if len(map[i]) == 1:
                    n = map[i][0]
                    listall[i] = n
                    del map[i]
                    solved = solved + 1
                    #print "solved number #" + str(solved) + ": " +str(i) + " " + str(n)
                    break
        
        #print map
        #print "not solved number: " + str(len(map))
        
        for i in range(0,9):
            for j in range(0,9):
                n = i * 9 + j
                if listall[n] != 0:
                    print listall[n],
                else: 
                    print " ",
            print 
        
        
        
        
        
        
        
solution = Solution()
board = [["5","3",".",".","7",".",".",".","."], \
         ["6",".",".","1","9","5",".",".","."], \
         [".","9","8",".",".",".",".","6","."], \
         ["8",".",".",".","6",".",".",".","3"], \
         ["4",".",".","8",".","3",".",".","1"], \
         ["7",".",".",".","2",".",".",".","6"], \
         [".","6",".",".",".",".","2","8","."], \
         [".",".",".","4","1","9",".",".","5"], \
         [".",".",".",".","8",".",".","7","9"], ]
solution.solveSudoku(board)
        
        
                
"""
# this problem ignored the diagonal and cross corner lines:


                if i % 9 == i /9:
                    for index, value in enumerate(listall):    # cross
                        if index % 9 == index / 9 and value in map[i]  :
                            map[i].remove(value)
                            if i == 10:
                                print index%9, index/9, i
                if i % 8 == 0 and i !=0 and i != 80:
                    for index, value in enumerate(listall):    # cross
                        if index % 8 == 0 and index !=0 and index != 80 and value in map[i]  :
                            map[i].remove(value)
                            if i == 10:
                                print index%9, index/9, i
"""
                