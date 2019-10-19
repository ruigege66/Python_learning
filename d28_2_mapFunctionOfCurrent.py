import time,re
import os,datetime
from concurrent import futures

data = ['1','2']
def wait_on(argument):
    print(argument)
    time.sleep(2)
    return "OK"

ex = futures.ThreadPoolExecutor(max_workers = 2)#两个协程池
for i in ex.map(wait_on,data):#类似于正常的map函数
    print(i)

