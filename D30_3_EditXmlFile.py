import xml.etree.ElementTree as et

tree = et.parse(r"D30_4_XmlSchool.xml")
root = tree.getroot()#拿到根元素的对象
print(root)#改成root.text，显示的是空值，因为根元素确实是空值，它里面有元素
for e in root.iter("Name"):#拿到所有Name的元素，并且把元素的值打印出来
    print(e.text)

for stu in root.iter("Student"):
    name = stu.find("Name")
    if name != None:
        name.set("test","wodejgoafewf")#这里设置name这个元素中的属性为test的属性值为那一行字符串
        print(name)

stu = root.find("Student")      #找到第一个Student这个元素

#下面三行分别代表创建一个ADDer元素，然后设置这个元素的属性，最后修改这个元素的值
e = et.Element("ADDer")
e.attrib = {"a":"b"}
e.text = "顺便改的"

#把上面创建的元素加入到我们的Student之中
stu.append(e)

#最后写入到这个XML之中
tree.write(r"D30_4_XmlSchool.xml")
