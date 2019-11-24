import socket

def tcp_clt():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = ("127.0.0.1",8998)
    sock.connect(addr)#链接addr这个地址，建立tcp这个通道
    msg = "I am a good man"
    sock.send(msg.encode())
    rst = sock.recv(500)#接受对方的反馈
    print(rst.decode())
    sock.close()

if __name__ == "__main__":
    tcp_clt()
