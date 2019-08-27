import threading
sum = 0
loopSum = 1000000
lock = threading.Lock()
#先生成一个锁的实例
def myAdd():
    global sum, loopSum
    for i in range(1,loopSum):
        lock.acquire()#这里申请了一把锁
        sum += 1
        lock.release()#注意千万不要忘了释放锁
def myMinu():
    global sum, loopSum
    for i in range(1,loopSum):
        lock.acquire()
        sum -= 1
        lock.release()
if __name__ == "__main__":
    print("Done,,,,,,,{0}".format(sum))
    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMinu,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done,,,,,,{0}".format(sum))
