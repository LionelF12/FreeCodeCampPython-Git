fhandle = open('mbox-short.txt','r')

count = dict()

for line in fhandle:
    if line.startswith('From '):
        line = line.strip()
        day = line.split()[2]
        count[day] = count.get(day,0)+1
print(count)