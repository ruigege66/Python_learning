from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#构建一个MIMEMultipart邮件
msg = MIMEMultipart("alternative")
#构建一个HTML邮件内容
html_content = """
                <!DOCTYPE html>
                <html lang="en"
                <head>
                    <meta charset="UTF-8">
                    <title>Title</title>
                </head>
                <body>
                    <h1>这是一封HTML格式邮件<h1>
                </body>
                </html>
                """
msg_html = MIMEText(html_content,"html","utf-8")
msg.attach(msg_html)
msg_text = MIMEText("just text content","plain","utf-8")
msg.attach(msg_text)
#发送email地址
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
