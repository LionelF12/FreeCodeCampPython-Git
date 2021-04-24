filename = 'mbox-short.txt'
fhandle = open(filename,'r')
count = 0
for line in fhandle:
    if line.startswith('From '):
        t=line.strip().split()
        t=t[1].split('@')
        count = count+1
        print(t[0])
print('There were '+str(count)+' lines in the file with From as the first word')
