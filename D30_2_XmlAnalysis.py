import xml.dom.minidom
#负责解析xml文件的包
from xml.dom.minidom import parse

#使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("D30_1_XmlNameSpace.xml")
print(DOMTree)#将该XML文件定义为一个对象
#得到文档对象
doc = DOMTree.documentElement#打印出了带有根目录的名字的对象
print(doc)

#显示子元素
for ele in doc.childNodes:
    if ele.nodeName == "Age":
        print("=======Node:{0}=======".format(ele.nodeName))
        print(doc.childNodes)
        print(doc.childNodes[0].nodeValue)
    if ele.nodeName == "Age":
        print(ele.getAttribute("jio"))#获取某一节点的属性值

import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("D30_1_XmlNameSpace.xml")
nodes = root.getiterator()
for node in nodes:
    print("{0}---{1}".format(node.tag,node.text))

print("===========================================")
ele_room_name = root.find("Location")
print(type(ele_room_name))
print("{0}----{1}".format(ele_room_name.tag,ele_room_name.text))
print("===========================================")
ele_room_name2 = root.findall("{http://my_room}Name")#这里如果使用“room:Name”是解析不出来的
print(ele_room_name2)
for ele in ele_room_name2:
    print("{0}----{1}".format(ele.tag,ele.text))
ele_room_name2 = root.findall("room:Name")
print(ele_room_name2)
for ele in ele_room_name2:
    print("{0}----{1}".format(ele.tag,ele.text))
