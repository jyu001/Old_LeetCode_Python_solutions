class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
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
        for i in range (0, 9):
            map = {}
            for index, value in enumerate(listall): # vertical
                if index % 9 == i and value :
                    if value not in map.values():
                        map[index] = value
                    else:
                        print "27"
                        return False
                        break
            map = {}
            for index, value in enumerate(listall): # horizontal
                if index / 9 == i and value :
                    if value not in map.values():
                        map[index] = value
                    else:
                        print i, index, value
                        print "36"
                        return False
                        break

            map = {}
            for index, value in enumerate(listall): # square
                a = index % 9
                b = index / 9
                if (a / 3 + (b / 3) * 3) == i and value :
                    if value not in map.values():
                        map[index] = value
                    else:
                        print "48"
                        return False
                        break
                        
        map = {}
        for index, value in enumerate(listall):    # cross
            if (index % 9 == index / 9 or index % 8 == 0) and value :
                if value not in map.values():
                    map[index] = value
                else:
                    print"58"
                    return False
                    break
        return True
        
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
print solution.isValidSudoku(board)
        
        
        