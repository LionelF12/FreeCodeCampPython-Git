import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
url = input('Enter URL - ')
hostname = url.split('/')[2]

mysock.connect((str(hostname),80))

cmd = ('GET ' + str(url) + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()