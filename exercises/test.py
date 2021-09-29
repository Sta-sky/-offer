# # 1,有一个整数数组,现在要去掉重复数字,每个数字只保留一个,输出去重后的数组,但是需要按照数字在原数组出现的次数从高到低排序,相同次数的按原顺位输出。
# # 例:[1,3,3,3,2,4,4,4,5]
# # 输出:3,4,1,2,5

# lists = [1,3,3,3,2,4,4,4,5]
#
# def renum(lists):
# 	dict_val = {}
# 	for val in set(lists):
# 		dict_val[val] = lists.count(val)
# 	res = sorted(dict_val.items(), key=lambda item: item[1], reverse=True)
# 	return [val[0] for val in res]
#
# print(renum(lists))



# # 2,有一堆石子,一次编号1-100围成圈,给定一个数K,从1开始数K个,将此石子踢出,继续报数,最后当石子总数小于K时,输出最后剩余石子编号。
# # 例:K为3
# # 输出:58,91

def removeshitou(k = 4):
	lists = [i for i in range(1, 101)]
	num = k
	while True:
		if len(lists) < num:
			break
		if len(lists)-1 > k:
			lists.pop(k)
		k += k
		if k>len(lists):
			k = k - len(lists)
	return lists





# # 3,有一个正整数数组,给定一个目标值S,求有多少个连续区间的和大于等于S
# # 例:数组 3,4,7  目标S为7
# # 输出:4
# #
# # 4,上台阶问题,一个阶梯有N个台阶,每次只能上一步或者3步,求一共有多少种不同的方式上台阶
# # 例:N=50
# # 输出:122106097

def sum_stairs_Fibo(sum):
    """
    非递归算法,斐波那契数列
    台阶数：1、2、3、4、5、6
    走法数：1、2、4、7、13、24
    :param sum:
    :return:
    """
    a,b = 1,3
    while sum-1>0:
        a,b = b,a+b
        sum -= 1
    return a
# #
# # 5,字符串解压缩,有一个字符串,全部由小写英文字符组成,现给出压缩字符串,求其原串
# # 例:
# # 输出:ddddff

s = '4dff'
def info(strings):
	new_word = []
	for index, i in enumerate(strings):
		print(i)
		if i.isdigit():
			res = (int(i) -1) * strings[index + 1]
			new_word.append(res)
		else:
			new_word.append(i)
	return ''.join(new_word)




# #
# # 6,每个人都有一个能力值,有一个活动要求参赛队伍能力值最低为M,每个队伍可以由1或者2个人组成,求计算最多可以组成多少符合要求的队伍
# # 例:3 1 5 7 9
# #  M=8
# # 输出:3

def sum_person(lists=[3, 1, 5, 7, ], m = 8):
	count = 0
	for i in lists:
		for j in range(len(lists)):
			if j < len(lists) - 1:
				if i + lists[j] == m:
					count += 1
	return  count
print(sum_person())


# # 7,有一个字符串只包含大写字母,求其连续相同字母子串中,长度第K长的子串长度,相同字母只取最长那个子串。
# # 例:AAAAHHHBBCDHHHH
# # K=3
# # 输出:2
class Solution:
	def solve(self, s):
		if len(s)==0:
			return 0
		ct=1
		tem=1
		for i in range(len(s)-1):
			if s[i]==s[i+1]:
				tem+=1
			else:
				ct = max(tem,ct)
				tem=1
		return ct

ob = Solution()
# print(ob.solve("AAAAHHHBBCDHHHH"))


from typing import List, AnyStr
# 数独
# # 8 https://leetcode-cn.com/problems/valid-sudoku/?um_channl=huawei?um_from_appkey=5fcda41c42348b56d6f8e8d5

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # 0: row, 1: column, 2: square
#         record = {0:defaultdict(set), 1:defaultdict(set), 2:defaultdict(set)}
#         n = len(board)
#         m = sqrt(n)
#         for i in range(n):
#             for j in range(n):
#                 if board[i][j] == '.':
#                     continue
#                 if board[i][j] in record[0][i] or board[i][j] in record[1][j]:
#                     return False
#                 sq = i // m * m + j // m
#                 if board[i][j] in record[2][sq]:
#                     return False
#                 record[0][i].add(board[i][j])
#                 record[1][j].add(board[i][j])
#                 record[2][sq].add(board[i][j])
#         return True


# # 9 . 单词搜索
# # https://leetcode-cn.com/classic/problems/longest-word-in-dictionary-through-deleting/description/


# 
# class Solution:
# 	def findLongestWord(self, s: str, dictionary: List[str]) -> str:
# 		# sorted 中 key 是升序排序的,如果想要让 word 长度比较长的排在前面,可以取反 -len(x)
# 		sorted_dictionary = sorted(dictionary, key=lambda x: [-len(x), x])
# 		
# 		for w in sorted_dictionary:
# 			# 两个指针,分别指向 s 和 w
# 			p = 0
# 			q = 0
# 			while q < len(s):
# 				if s[q] == w[p]:
# 					p += 1
# 				
# 				if p == len(w):
# 					return w
# 				
# 				q += 1
# 		return ""
# 
# s = "abpcplea"
# dictionary = ["ale","apple","monkey","plea"]
# 
# info = Solution()
# print(info.findLongestWord(s,  dictionary))
# i = 'a'
# print(s.find(i))
# if s.find(i) != -1:
# 	print('======')



# # 10
# # https://leetcode-cn.com/problems/word-search/?um_channl=huawei?um_from_appkey=5fcda41c42348b56d6f8e8d5
#
#
# # 输入：
# # 输出：
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 使用深度优先搜索
        if not board:   # 边界条件
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0: # 如果单词已经检查完毕
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:  # 如果路径出界或者矩阵中的值不是word的首字母,返回False
            return False
        tmp = board[i][j]  # 如果找到了第一个字母,检查剩余的部分
        board[i][j] = '0'
        res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j+1,word[1:]) or self.dfs(board, i, j-1, word[1:]) # 上下左右四个方向搜索

        board[i][j] = tmp  # 标记过的点恢复原状,以便进行下一次搜索
        return res

test = Solution()
print(test.exist(board, word))
