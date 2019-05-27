#包含一个学生类
#一个say hello函数
#一个打印语句

class Student():
    def __init__(self,name="haha",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))



def sayhello():
    print("欢迎来到图灵学院")

if __name__ == "__main__":
    print("我是木块p01")


