"""

矩形覆盖
"""

# 做法一  按波奇菲娜数列
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        list_ = []
        s = 0
        while s <= number:
            if s <= 2:
                res = s
            else:
                res = list_[s - 1] + list_[s - 2]
            list_.append(res)
            s += 1
        return list_[-1]



# 递归写法          （用空间换取时间）
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return  number
        val = self.rectCover(number-1)+self.rectCover(number-2)
        return val


s = Solution()
print(s.rectCover(4))