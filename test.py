inputs = '525 6'
val ='85 86 87 88 89 90'



# s = 525
s = 402
# n = 6
n = 3
def num_sum(s:int, n:int):
	if s < n:
		return - 1
	if s % n:
		num = s//n
		fix = int(n / 2)
		data_list = [num -i for i in range(fix)]
		for i in range(fix+1):
			data_list.append(num + i)
		return set(data_list)
	
	if not s % n:
		num = s // n
		fix = int(n / 2)
		data_list = [num - i for i in range(fix+1)]
		for i in range(fix+1):
			data_list.append(num + i)
		return set(data_list)

# print(num_sum(s, n))

#
# def input_info(inp='([]{()})'):
# 	for i in inp:
# 		if '(' == i:
# 			if
#
#
# # 	print(lists)
# #
# # input_info()
# #
# #
# #
from typing import List

"""
给定一个整数数组，找出总和最大的连续数列，并返回总和。
动态规划 解决连续数列中的最大和

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        else:
            for i in range(1, len(nums)):
                print(max(nums[i]+nums[i-1], nums[i]))
                nums[i] = max(nums[i]+nums[i-1], nums[i])
                print(nums[i], '===========')
            return max(nums)
li = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(li))






