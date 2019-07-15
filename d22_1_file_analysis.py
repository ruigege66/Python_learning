#f称之为文件句柄
f = open(r"C:\Users\lenovo1\Desktop\微信公众号运营-Python\新建 Microsoft Word 文档.docx",'r')
#打开之后一定要关闭
f.close()
#案例说明，以写方式打开文件，默认是如果没有这个文件，则会创建

with open(r"C:\Users\lenovo1\Desktop\微信公众号运营-Python\新建 Microsoft Word 文档.docx",'r') as f:
    pass
#下面的语句块开始对文件f进行操作，在本木块中不需要使用close来关闭文件f

with open(r"C:\Users\lenovo1\Desktop\微信公众号运营-Python\新建 Microsoft Word 文档.docx",'r') as f:
    #按行读取内容
    strling = f.readline()
    #磁结构保证能够完整的读取文件直到结束
    while strling:
        print(strling)
        strline = f.readline()
