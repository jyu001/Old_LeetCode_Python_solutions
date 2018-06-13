"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        integ = numerator/denominator
        remain = numerator % denominator
        result = str(integ)
        if remain == 0:
            return str(integ)
        map = {}
        point = []
        while remain:
            remain = remain * 10
            fract = remain / denominator
            remain = remain % denominator
            if remain == 0:
                point.append(fract)
                if len(point):
                    result = result + "."
                for i in point:
                    result = result + str(i)
                return result
            if remain in map:
                repeat = ""
                for i in point:
                    repeat = repeat + str(i)
                result = result + ".(" + repeat + ")"
                return result
            map[remain] = 1
            point.append(fract)
            #print remain
            #print point
                
                
solution = Solution()
print solution.fractionToDecimal(1,2)
print solution.fractionToDecimal(2,1)
print solution.fractionToDecimal(2,3)
print solution.fractionToDecimal(1,7)
print solution.fractionToDecimal(1,77)
print solution.fractionToDecimal(1,777)
print solution.fractionToDecimal(1,7777)


                