import socket

def tcp_srv():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#其哪一个参数为ipv4,后一个参数为TCP固定参数
    addr = ("127.0.0.1",8998)#ip地址和端口号

    sock.bind(addr)#绑定addr
    sock.listen()#监听接入的访问socket

    while True:
        #接受访问的socket，可以理解为接受访问即建立一个通讯的链接通路，accept返回的元组第一个元素赋给skt,第二个元素赋给addr
        skt,addr = sock.accept()#第一个元素是socket，第一个元素就是发送方的地址
        #接受对方的发送内容，利用接受到的socket接受内容
        msg = skt.recv(500)#500代表接收使用的buffersize，理解为接受内容的大小
        msg = msg.decode()#接受到的是bytes格式内容，想得到str格式的，需要进行解码
        #下面三行代表反馈的信息
        rst = "Received msg:{0} from {1}".format(msg,addr)
        print(rst)
        skt.send(rst.encode())
        #关闭socket
        skt.close()

if __name__ == "__main__":
    print("Startint tcp server.......")
    tcp_srv()
    print("Ending tcp server.........")
