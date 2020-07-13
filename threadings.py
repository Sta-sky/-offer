"""
线程创建
"""
import time
from threading import Thread
from multiprocessing import Process,Pool

def _time():
    for i in range(10000000):
        print('time——————A')


def _time_():
    for item in range(10000000):
        print("time——————B",item)


if __name__ == '__main__':
    stime = time.time()
    p = Pool(4)
    for i in range(10):
        p.apply_async(_time_,args=(i,))
        print(i)
    _time()
    # _time_()
    #
    th = Process(target=_time)

    th1= Process(target=_time_)
    th.start()
    print(th.is_alive())
    th1.start()
    print(th.is_alive())
    print(th.ident)
    print('*'*100)
    th.join() #
    th1.join()
    p.close()
    p.join()
    etime = time.time()
    print(etime-stime)


# 1.67
# 13.8

