fhandle = open('mbox-short.txt','r')

hourcount = dict()

for line in fhandle:
    if line.startswith('From '):
        time = line.strip().split()[5]
        hour = time.split(':')[0]
        hourcount[hour] = hourcount.get(hour,0)+1

temp = list()

for hour,value in hourcount.items():
    temp.append((hour,value))
    
for hour,value in sorted(temp):
    print(hour,value)