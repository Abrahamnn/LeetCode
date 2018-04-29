#给定一个 32 位有符号整数，将整数中的数字进行反转

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x <10:
            return x 
        x1 = abs(x)
        b = str(x1)
        if len(b) > 10:
            return 0
        v = ''
        for i in range(len(b)):
            v = v+b[-(i+1)]
        result = int(v)
        if x < 0:
            result = -result
            
        if -2147483648 < result < 2147483647:
            return result
        else:
            return 0
            
#大佬：

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        abs_x = int(str(abs(x))[::-1])
        abs_x = abs_x if x > 0 else -abs_x

        if abs_x < -2147483648 or abs_x > 2147483647:
            return 0
        return abs_x
