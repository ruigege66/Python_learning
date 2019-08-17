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

def main():
    print("Starting at:",time.ctime())
    thread.start_new_thread(loop1,("liuming",))
    #上面我们传参的时候，我用的是：（“liuming”），这里面是没有逗号的，结果编译报错，告诉我，这里面必须传入元组
    #因此，我才在里面加了一个逗号，使其变成一个元组
    thread.start_new_thread(loop2,("zhanglei","liuhao"))
    print("All done at:",time.ctime())



import threading
# t= threading.Thread(target=,args=(,))
# t.start()
# t.join()#等待多线程执行完成
def main2():
    print("Start at :",time.ctime())
    t1 = threading.Thread(target=loop1,args=("王老大",))
    t1.start()#启动多线程
    t2 = threading.Thread(target=loop2,args=("孙子","好吗"))
    t2.start()
    t1.join()
    t2.join()
    print("End at :",time.ctime())
def fun():
    print("Start fun")
    time.sleep(2)
    print("End fun")




if __name__ == "__main__":
    main()
    main2()
    print('Main thread')
    t3 = threading.Thread(target=fun,args=())
    t3.setDaemon(True)
    t3.start()
    time.sleep(1)
    print("Main thread End")
