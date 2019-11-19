import socket
def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = "you are very cool"

    #发送的数据必须是bytes格式
    data = text.encode()
    #发送
    sock.sendto(data,("127.0.0.1",7852))
    data,addr =sock.recvfrom(200)

    data = data.decode()
    print(text)

if __name__ == "__main__":
    print("Start Client")
    clientFunc()
    print("End Client")
