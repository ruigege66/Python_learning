import threading,time
import _thread as thread
#利用time生成两个函数
def loop1():
    print("Start loop 1 at:",time.ctime())
    time.sleep(4)
    print("End loop 1 at :",time.ctime())
def loop2():
    print("Start loop 2 at :",time.ctime())
    time.sleep(2)
    print("End loop 2 at :",time.ctime())
def main():
    print("Start at :",time.ctime())
    thread.start_new_thread(loop1,())#这里里面的第二个位置是用来传递参数的，因为咱们的函数刚好没有参数，因此咱们传递了一个空参数
    thread.start_new_thread(loop2,())
    print("End at :",time.ctime())
if __name__ == "__main__":
    main()
