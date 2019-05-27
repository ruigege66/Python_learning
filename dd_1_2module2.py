import importlib
#想要导入这种以数字开头的或者非python允许格式的包名，可以利用importlib包中的import_module函数
tuling = importlib.import_module("dd_1_1module1")
from dd_1_1module1 import Student
import dd_1_1module1 as liumang
liumang.sayhello()
#忘记加（）了就不通了
stu = Student("dong",25)
stu.say()
