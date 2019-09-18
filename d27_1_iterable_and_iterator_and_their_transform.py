from collections import Iterable,Iterator

l = [i for i in range(5)]  #可迭代
print(isinstance(l,Iterable))#判断是否可迭代
print(isinstance(l,Iterator))#判断是否是一个迭代器

s_iter = iter(l)#将其转换为可以迭代的和迭代器
print(isinstance(s_iter,Iterable))#判断是否可迭代
print(isinstance(s_iter,Iterator))#判断是否是一个迭代器
for idx in l:
    print(idx)

#range是一个迭代器
for i in range(5):
    print(i)
