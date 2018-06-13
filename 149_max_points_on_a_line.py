# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        for  point in points:
            print point.x, point.y
        maxm = 0
        for i in range(0, len(points) - 1):
            map = {}
            map['same'] = 0
            map['infinity'] = 0
            for j in range(i + 1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    map['same'] = map['same'] + 1
                elif points[j].x == points[i].x:
                    map['infinity'] = map['infinity'] + 1
                    maxm = max(maxm, map['infinity'])
                else:
                    rt = (points[j].y - points[i].y)/(points[j].x - points[i].x)
                    if rt in map:
                        map[rt] = map[rt] + 1
                    else: 
                        map[rt] = 1
                    maxm = max(maxm, map[rt])
                maxm = maxm + map['same']
        print maxm + 1
        
        
a = Point(0,0)
b = Point(1,0)
c = Point(2,0)
d = Point(1,1)
e = Point(2,2)
f = Point(3,3)
g = Point(0,0)

list = [a,b,c,d,e,f,g]

solution = Solution()
solution.maxPoints(list)
        