# -*- coding:utf-8 -*-

"""
将列表中的奇数放到列表中偶数的后面。
简单··
"""

class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        if len(array) <= 1:
            return array
        for i in array:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        list_ = odd + even
        return list_


arr = [2,5,6,3,2,1]
s = Solution()
print(s.reOrderArray(arr))
