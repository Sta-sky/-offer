"""
消息队列实现同进程通信
"""
import random
import sys
import time
from multiprocessing  import Process,Queue



class Stack_list:
    def stack_insert(self,value,q):
        if value is not  None:
            q.put(value)
            return '插入:'+ str(value)

    def stack_pop(self,q):
        try:
            f = q.get(timeout=2,block=True)
            return "取出："+str(f)
        except Exception as e:
            print(e)
            print('队列为空 ，任务完成')


s = Stack_list()
q = Queue()


def _stack(q):
    for i in range(0, 40, 2):
        time.sleep(random.uniform(0,1))
        print(s.stack_insert(i,q))


def spop(q):
    for i in range(100):
        time.sleep(random.uniform(1,2))
        print(s.stack_pop(q))


if __name__ == '__main__':
    p = Process(target=_stack,args=(q,))
    p1 = Process(target=spop,args=(q,))
    p.start()
    p1.start()

    p.join()
    p1.join()




