import _thread as thread
import time
def loop1(in1):
    print("Start loop 1 at:",time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("End loop 1 at:",time.ctime())

def loop2(in1,in2):
    print("Start loop 2 at:",time.ctime())
    print("我是参数",in1,"和参数 ",in2)
    time.sleep(4)
    print("End loop 2 at:",time.ctime())

import threading
def main1():
    print("Starting at:",time.ctime())
    t1 = threading.Thread(target=loop1,args=('',))
    t1.setName("THR_1")#给线程重命名
    t1.start()

    t2 = threading.Thread(target=loop2,args=('',''))
    t2.setName("THR_2")
    t2.setDaemon(True)  #主线程运行完了就完了，不用等线程2
    t2.start()

    time.sleep(3)#三秒后两个子线程仍然在运行着，因为他们里面有一个四秒在停着
    for thr in threading.enumerate():#返回的是正在运行的子线程的列表
        print("正在运行的子线程名为：{0}".format(thr.getName()))#读取了该线程的名字

    print("正在运行的子线程数量为：{0}".format(threading.activeCount()))#打印出了线程的数量，包括主线程和两个子线程一共3个线程
    t1.join()#等线程1运行完了再接着向下运行
    print("ALL done at :",time.ctime())

if __name__ == "__main__":
    main1()
