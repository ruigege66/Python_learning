#导入相应的包
import smtplib
from email.mime.text import MIMEText
#MIMEText三个主要参数：1.邮件内容；2.MIME子类型，在此案例中我们用plain表示text类型；3.邮件编码格式
msg = MIMEText("hello ,I am ruigege","plain","utf-8")
#发送email地址，此处地址直接使用我的qq邮箱，密码一般许哟啊临时输入，此处偷懒
from_addr = "1215217867@qq.con"
#此处密码是经过申请设置之后的授权码，不是自己的qq号码密码，相当于github中的privateToken
from_pwd = ""
#收件人信息
#此处使用qq邮箱，我给自己发送吧，就不打扰别人了
to_addr = "1215217867@qq.com"
#输入SMTP服务器地址
#此处根据不同的邮件服务商有不同的值
#现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
#腾讯qq邮箱的smtp地址是smtp.qq.com
smtp_srv = "smtp.qq.com"
try:
    #两个参数：第一个是服务器地址，但一定是bytes格式，所以需要编码；第二个参数是服务器的接受访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)#SMTP协议默认端口25
    #登录邮箱发送
    srv.login(from_addr,from_pwd)
    #发送邮件：三个参数1.发送地址；2.接受地址，必须是List形式；3.发送内容，作为字符串进行发送
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as w:
    print(w)
