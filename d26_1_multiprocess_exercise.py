import multiprocessing
from time import sleep,ctime
import os
def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)
class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is {0}".format(ctime()))
            sleep(self.interval)

def info(title):
    print(title)
    print("module name:",__name__)
    #得到父进程的id
    print("parent process:",os.getppid())
    #得到本身进程的id
    print("process id:",os.getpid())

def f(name):
    info("function f")
    print("hello",name)



if __name__ == "__main__":
    p = multiprocessing.Process(target= clock,args=(2,))
    p.start()
    # 从运行就可以看出来主进程已经结束了，但是子线程仍然在运行着
    # 和我们之前讲的线程，有一个最大区别就是线程在主进程里面，主进程结束了，子线程就结束了
    # 子线程从属于进程，子进程与进程之间是并列关系
    p2 = ClockProcess(2)
    p2.start()
    info("main line")
    print("==================================")
    p = multiprocessing.Process(target=f,args=("bob",))
    p.start()
    p.join()
