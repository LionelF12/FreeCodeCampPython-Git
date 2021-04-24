fhandle = open('mbox-short.txt','r')

count = dict()

for line in fhandle:
    if line.startswith('From '):
        line = line.strip()
        email = line.split()[1]
        count[email] = count.get(email,0)+1
print(count)