def gen():
    for c in "AB":
        yield c

#list直接用生成器作为参数
print(list(gen()))
def gen_new():
    yield from "AB"

print(list(gen_new()))

from collections import namedtuple
#解释：
#1.外层for循环每次迭代会新建一个grouper实例，赋值给coroutine变量；grouper是委派生成器生成
#2.调用next(coroutine),预激委派生成器grouper，此时进入while True循环，调用子生成器average
#3.内层for循环调用coroutine.send(value),直接把值传给子生成器average，同时，当前的grouper
#4.内层循环结束后，grouper实例依旧在yield from表达式处暂停，因此，grouper函数定义体中
#5.coroutine.send(None)终止averager子生成器，子生成器抛出StopIteration异常并将返回的数
ResClass = namedtuple("Res","count average")

#子生成器
def average():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        #None是哨兵值
        if term is None:
            break
        total += term
        count += 1
        average = total/count

    return ResClass(count,average)

#委派生成器
def grouper(storages,key):
    while True:
        #获取averager()返回的值
        storages[key] = yield from average()

#客户端代码
def abc():
    process_data = {
        "boys_2":[39.0,40.8,43.2,43.1,38.6,41.4,40.6,36.3],
        "boys_1":[1.38,1.5,1.32,1.25,1.37,1.48,1.25,1.49,1.46]
    }
    storages = {}
    for k,v in process_data.items():
        #获取协程
        coroutine = grouper(storages,k)
        #预激协程
        next(coroutine)

        #发送数据到协程
        for dt in v:
            coroutine.send(dt)

        #终止协程
        coroutine.send(None)
    print(storages)
#run
if __name__ == "__main__":
    abc()
