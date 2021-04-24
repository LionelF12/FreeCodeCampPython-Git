import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = 0
for line in fhandle:
    line = line.decode().strip()
    for characters in line:
        while count < 3000:
            count += 1
            break
    print(count,line)
print('Total Count: ', count)
