from email.mime.text import MIMEText

main_content = """
        <!DOCTYPE html>
        <html lang = "en"
        <head>
            <meta charset = "UTF-8">
            <title>实例</title>
        </head>
        <body>
            <h1>这个是做测试用的html<h1>
        </body>
        </html>
        """

msg = MIMEText(main_content,"html","utf-8")

#构建发送者地址和登录信息
from_addr = "1215217867@qq.com"
from_pwd = ""
#构建邮件接受者的信息
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
