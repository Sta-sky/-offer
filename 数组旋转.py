"""引入数组的旋转是为了什么
这说明旋转后的数组分成了两个非减排序的数组，
记为array1和array2，array1中的任意元素是大于等于array2中所有数的，
所以array2中的第一个数就是我们要找的旋转数组中最小的数。
"""


# def minNumberInRotateArray(rotateArray):
#     min = rotateArray[0]
#     if len(rotateArray) > 0:
#         for i in range(1, len(rotateArray)):
#             if rotateArray[i] < min:
#                 min = rotateArray[i]
#         return min
#     else:
#         return 0
# arr=[4 ,5 ,6 ,7 ,1 ,2 ,3]
# s = minNumberInRotateArray(arr)
# print(s)

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) <= 0:
            return 0
        else:
            mins = rotateArray[0]
            for i in rotateArray:
                if i < mins:
                    mins = i
            return mins


arr = [4, 5, 6, 7, 1, 2, 3]
s = Solution()
print(s.minNumberInRotateArray(arr))
