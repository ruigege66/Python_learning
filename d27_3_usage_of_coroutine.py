def simple_coroutine():
    print("->start")
    x = yield#这个函数执行到这里停止了，等待着给它赋值，也就是后面的send语句
    print("->recived",x)
#主线程
sc = simple_coroutine()
print(1111)
#可以使用sc.send(None),效果一样
next(sc)#预激
print(2222)
sc.send("zhexiao")

def simple_coroutine2(a):
    print("->start")
    b = yield a#可以看出这个yield相当于return 语句通过后面的send，之后等价于input语句
    print("->recived",a,b)
    c = yield a+b
    print("->recived",a,b,c)

sc2 = simple_coroutine2(5)
aa = next(sc2)
print(aa)
bb = sc2.send(6) #5,6
print(bb)
cc = sc2.send(7) #5,6,7
print(cc)
