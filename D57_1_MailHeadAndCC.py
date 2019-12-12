from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello world","plain","utf-8")

#用utf-8编码是因为很可能内容包含非英文字符
header_from = Header("从我自己的邮箱发送出去有的<1215217867@qq.com>","utf-8")#就是邮件头，注意点：编解码格式相一致
msg["From"] = header_from
header_to = Header("去我自己的邮箱1215217867@qq.com","utf-8")#填写接收者的信息
msg["To"] = header_to
header_sub = Header("这是我的主题","utf-8")
msg["Subject"] = header_to
#构建发送者地址和登录信息
from_addr = "1215217867@qq.com"
from_pwd = "ysqmojzwkgfciccd"
#构建邮件接收者信息
to_addr = "1215217867@qq.com"
smtp_srv = "smtp.qq.com"
try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as a:
    print(a)

