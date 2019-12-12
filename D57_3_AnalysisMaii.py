#导入相关的包
#poplib负责从MDA到MUA下载
import poplib
#以下包负责相关邮件结构解析
from email.parser import Parser
from email.header import Header
from email.utils import parseaddr
#得到邮件的原始内容
#这个过程主要负责从MDA到MUA的下载并且使用Parse粗略解析
def getMsg():
    #准备相应的信息
    email = "1215217867@qq.com"
    #邮箱的授权码
    pwd = ""
    #pop3服务器地址
    pop3_srv = "pop.qq.com"#端口995

    #ssl代表安全通道
    srv = poplib.POP3_SSL(pop3_srv)
    #user代表email地址
    srv.user(email)
    #pass_代表密码
    srv.pass_(pwd)

    #以下操作根据具体业务具体使用
    #stat返回的是邮件数量以及占用空间
    #注意stat返回了一个tuple格式
    msgs,counts = srv.stat()
    print("Message:{0},Size:{1}".format(msgs,counts))

    #list返回所有邮件编号列表
    #mails是所有邮件编号列表
    rsp,mails,octets = srv.list()
    #可以查看返回的mails列表，类似于[b"1 82923",b"23 2184",.....]
    print(mails)

    #获取最新一封邮件，追忆，邮件索引是从1开始的，最新代表索引号最高
    index = len(mails)
    #retr负责返回一个具体索引号的一封信的内容，此内容不具有可读性
    #lines存储邮件的最原始文本的每一行
    rsp,lines,octets = srv.retr(index)

    #获取整个邮件的结构体
    msg_count = b"\r\n".join(lines).decode("utf-8")
    #解析出邮件整个结构体
    #参数是解码后的邮件整体
    msg = Parser().parsestr(msg_count)#这一行代表解码

    #关闭链接
    srv.quit()
    return msg

if __name__ == "__main__":
    #得到邮件的原始内容
    msg = getMsg()
    print(msg)
    #精确解析邮件内容
    # parseMsg(msg,0)


