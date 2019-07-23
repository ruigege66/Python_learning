#打开文件，三个字符一组读出来内容，然后显示在屏幕上，每读一次，停一秒
import time
with open(r"test01.txt",'r') as f:
    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read(3)
    strChar2 = f.read(3)
    pos = f.tell()

    while strChar2:
        print(pos)
        print(strChar2)

        strChar2 = f.read(3)
        pos = f.tell()
with open(r"test01.txt",'a') as l:
    l.write("优秀1 \n非常优秀1")
    b = ["优秀2","非常优秀2","jsfdk"]
    l.writelines(b)
import pickle
with open(r"test01.txt","wb") as k:
    age = 24
    pickle.dump(age,k)

with open(r"test01.txt","rb") as j:
    age=pickle.load(j)
    print(age)
