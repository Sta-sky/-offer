# """
# 斐波那契数列 代码实现


# 思路 ：
#     val = 1、2，时 值为1 
# """

# def FeiBo(num):
#     n = 0
#     if num <= 0:
#         return 0 
#     elif 0 < num <= 2:
#         return 1
#     list = [1,1]    
#     while n< num:
#         val = FeiBo(num-1) + FeiBo(num-2)
#         list.append(val)
#         n +=1
#     return list[-1]

# v=7
# s = FeiBo(v)
# print(s)

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        s = 0
        if n <= 0:
            return 0 
        elif 0 < n <= 2:
            return 1
        while s < n:
            val = self.Fibonacci(n-1) + self.Fibonacci(n-2)
            s +=1
        return val

h = Solution()
print(h.Fibonacci(5))