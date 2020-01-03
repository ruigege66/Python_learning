#pack布局案例
import tkinter
baseFrame = tkinter.Tk()
#以下代码都是创建一个组件，然后布局
btn1 = tkinter.Button(baseFrame,text="A")
btn1.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame,text="B")
btn2.pack(side=tkinter.TOP,expand=tkinter.YES,fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame,text="C")
btn2.pack(side=tkinter.RIGHT,expand=tkinter.YES,fill=tkinter.NONE)

btn2 = tkinter.Button(baseFrame,text="D")
btn2.pack(side=tkinter.LEFT,expand=tkinter.NO,fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame,text="F")
btn2.pack(side=tkinter.BOTTOM,expand=tkinter.YES)

btn2 = tkinter.Button(baseFrame,text="G")
btn2.pack(anchor=tkinter.SE)


baseFrame.mainloop()

baseFrame2 = tkinter.Tk()

lb1 = tkinter.Label(baseFrame2,text="账号：")
lb1.grid(row=0,sticky=tkinter.W)
tkinter.Entry(baseFrame2).grid(row=0,column=1,sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame2,text="密码：")
lb2.grid(row=1,sticky=tkinter.W)
tkinter.Entry(baseFrame2).grid(row=1,column=1,sticky=tkinter.E)

button = tkinter.Button(baseFrame2,text="登录").grid(row=2,column=1,sticky=tkinter.E)

baseFrame2.mainloop()
