import tkinter

base = tkinter.Tk()
base.wm_title("Label Test")#负责标题
lb = tkinter.Label(base,text="Python label")
lb.pack()#给相应的组件指定布局
base.mainloop()


#支持属性很多background,font,underline等
#第一个参数，制定所属
lb1 = tkinter.Label(base,text="Python AI")
lb1.pack()

lb2 = tkinter.Label(base,text="绿色背景",background="green")
lb2.pack()

lb3 = tkinter.Label(base,text="蓝色背景",background="blue")
lb3.pack()

base.mainloop()

def showLable():
    global baseFrame
    #在函数中定义了一个Label
    #label的父组件是baseFrame
    lb = tkinter.Label(baseFrame,text="显示Label")
    lb.pack()

baseFrame = tkinter.Tk()
#生成一个按钮，command参数指示，当按钮被按下的时候，执行哪个函数
btn = tkinter.Button(baseFrame,text="Show Label",command=showLable)
btn.pack()

baseFrame.mainloop()
