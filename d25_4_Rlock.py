import threading
import time

#参数定义了最多几个线程可以使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(2):
            print(threading.current_thread().getName() + "get semapore")
        time.sleep(5)
        semaphore.release()
        print(threading.current_thread().getName() + "release semaphore")

def func2():
    print("I am running.....")
    time.sleep(3)
    print("I an done.......")

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num = num+1
            msg = self.name + " set num to "+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

def test():
    for i in range(5):
        t3 = MyThread()
        t3.start()

if __name__ == "__main__":
    t2 = threading.Timer(6,func2) #代表6秒之后开始启动线程func2
    t2.start()
    i = 0
    while True:
        print("{0}*********".format(i))
        time.sleep(3)
        i += 1

    for i in range(8):
        t1 = threading.Thread(target=func,args=())
        t1.start()

    num = 0
    mutex = threading.Lock()

    test()
