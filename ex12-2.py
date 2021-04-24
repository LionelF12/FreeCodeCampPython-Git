import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
url = input('Enter URL - ')
hostname = url.split('/')[2]

mysock.connect((str(hostname),80))

cmd = ('GET ' + str(url) + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

count = 0 
while True:
    data = mysock.recv(500)
    if len(data) < 1:
        break
    if count < 3000:
        print(data.decode())
        count += len(data)
        print(count)

mysock.close()