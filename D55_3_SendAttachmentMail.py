from email.mime.text import MIMEText#构建附件使用
from email.mime.multipart import MIMEBase,MIMEMultipart#构建基础邮件使用

mail_mul = MIMEMultipart()#构建一个邮件对象
mail_text = MIMEText("Hello,I am liudana","plain","utf-8")#构建邮件正文
mail_mul.attach(mail_text)#把构建好的邮件正文附加到邮件中
#构建附件，需要从本地读入附件
#打开一个本地文件
#以rb格式打开
with open("00.TestCasePython.py","rb") as  f:
    s = f.read()
    #设置附件的MIME和文件名
    m = MIMEText(s,"base64","utf-8")#类型是base64，这是邮件正文的格式，这里只需要记住就可以了
    m["Content-Type"] = "application/octet-stream"
    #需要注意
    #1.attachment后分号位英文状态
    #2.filename后面需要引号包裹，注意与外面引号错开
    m["Content-Disposition"] = "attachment;filename = '00.TestCasePython.py'"
    #添加到MIMEMultipart
    mail_mul.attach(m)

#构建发送者地址和登录信息
from_addr = "1215217867@qq.com"
from_pwd = "ysqmojzwkgfciccd"
#构建邮件接受者的信息
to_addr = "1215217867@qq.com"
smtp_srv = "smtp.qq.com"
try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],mail_mul.as_string())
    srv.quit()

except Exception as a:
    print(a)
