import re
#查找数字
p = re.compile(r"\d+")
#在字符串“ongahjeuf125”中及逆行查找，按照规则p指定的正则进行查找

m = p.match("ong125fdsgdsf48515",3,20)#后面的参数序号3到6的搜索范围
print(m)
#上述代码说明
#1.match可以输入参数表示起始位置
#2.查找到的结果只包含一个，表示第一次进行匹配成功的内容
print(m[0])#直接打印出了匹配的内容
print(m.start(0))#打印匹配内容从哪里开始的
print(m.end(0))#打印匹配内容从哪里结束的

#参数中re.I代表忽略大小写
p1 = re.compile(r"([a-z]+) ([a-z]+)",re.I)
m1 = p1.match("I am relly good man")
print(m1)
print(m1.group(0))
print(m1.start(0))
print(m1.end(0))
print("===================")
print(m1.group(1))
print(m1.start(1))
print(m1.end(1))
print("===================")
print(m1.group(2))
print(m1.start(2))
print(m1.end(2))
print("===================")
print(m1.groups())


p2 = re.compile(r"\d+")
m2 = p2.search("one12two34three567four")
print(m2.group())
m3 = p2.findall("one12two34three567four")
print(type(m3))
print(m3)

p3 = re.compile(r"(\w+) (\w+)")
s = "hello 123 wang 456 jfowe,i jodf "
ret = p3.sub(r"Hello world",s)
print(ret)

title =  "世界 你好，hello moto"
p4 = re.compile(r"[\u4e00-\u9fa5]+")
rst = p4.findall(title)
print(rst)
