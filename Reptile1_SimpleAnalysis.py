from urllib import request
import chardet
"""
使用urllib,request请求一个网页内容，并把内容打印出来
"""
if __name__ == "__main__":
    url = "https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=984602018"
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)
    #返回结果读取出来
    html = rsp.read()
    print(type(html))##bytes类型
    print("=========================")

    cs = chardet.detect(html)#利用chardet来检测这个网页使用的是什么编码方式
    print(cs)
    print(type(cs))
    #使用get方法是为了避免如果取不到值报错，程序就崩溃了
    html = html.decode(cs.get("encoding","utf-8"))#取cs字典中encoding属性，如果取不到，那么就使用utf-8
    print(html)

"""
利用request下载页面
"""
