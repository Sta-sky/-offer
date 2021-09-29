# -*- coding:utf-8 -*-
"""
两个栈实现队列
思想 ： 
    一个负责入栈 一个负责出栈
    栈是先进后出    队列特点是先进先出
    
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack2.append(node)
    def pop(self):
        if self.stack1==[]:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return self.stack1.pop()
        return self.stack1.pop()
    

    
    
    


