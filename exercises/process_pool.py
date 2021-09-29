"""
自定义进程类

进程池创建多进程
"""

from multiprocessing import Pool,Process
import time
import os

class MyProcess(Process):
    def __init__(self, val):
        super().__init__()
        self.val = val
    def f1(self):
        print("this is 步骤 1")

    def f2(self):
        print("this is 步骤 2")

    def run(self):
        self.f1()
        self.f2()


if __name__ == '__main__':
    p = MyProcess(3)
    p.start()
    p.join()



