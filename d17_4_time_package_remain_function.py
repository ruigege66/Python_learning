import time,datetime

t1 = time.clock()
for i in range(10):
    print(i)
    time.sleep(1)
t2 = time.clock()
print(t2-t1)

t3 = time.localtime()
t4 = time.strftime("%Y{Y}%m{m}%d{d} %H{o}%M",t3).format(Y="年",m="月",d="日",o=":")
print(t4)

d5 = datetime.date(2018,3,3)
print(d5)
print(d5.year)
print(d5.month)
print(d5.day)
