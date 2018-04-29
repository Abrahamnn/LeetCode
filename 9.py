# 回文数
#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        v = ''
        b = str(x)
        for i in range(len(b)):  
            v=v+b[-(i+1)]
        result=int(v)
        if x == result:
            return True
        else:
            return False
            
 # 和反转没什么区别啊？ 判断少一点
 
 
 
 
       # str_x = str(x)
       # return str_x[::-1] == str_x
       两句话
