"""
栈的压入弹出
思想 ：
    先入栈的后出栈，判断 最上层的栈 是否与出栈序列中的第一个是否相等 
    就可以判断出来是否为  次栈的出栈序列

"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return True if not stack else False