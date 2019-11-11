import re
title = u"<div>name</div><div>age</div>"
p1 = re.compile(r"<div>.*</div>")#贪婪模式
p2 = re.compile(r"<div>.*?<div>")#非贪婪模式
m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())
