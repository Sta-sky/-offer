# class Solution:
#     def rectCover(self, number):
#
#         if number == 0:
#             count = 0
#             return count
#         elif number == 1:
#             count = 1
#             return count
#         elif number == 2:
#             count =2
#             return count
#         else:
#             count = self.rectCover(number-1)+ self.rectCover(number-2)
#             return count
#
#
#
# s = Solution()
#
# number = 3
# result = s.rectCover(number)
# print(result)

def rectCover (n):
    if n <=0:
        return 0
    if n <= 2:
        return n
    return rectCover(n-1) + rectCover(n-2)

d = 5
s = rectCover(d)
print(s)


#冒泡排序

def bull_sort(list_):
    length = len(list_)
    for i in range(0,length):
        for j in range(0,length-1-i):
            if list_[j] > list_[j]:
                list_[j],list_[j+1] = list_[j+1] ,list_[j]
    return list_

    