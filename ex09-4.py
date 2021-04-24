fhandle = open('mbox.txt')

emaild = {}

for line in fhandle:
    if line.startswith('From '): 
        line = line.strip()
        email = line.split()[1]
        emaild[email] = emaild.get(email,0)+1

bigcount = None
bigword = None
for aaa,bbb in emaild.items():
    if bigcount == None or bbb > bigcount:
        bigcount = bbb
        bigword = aaa
print(bigword,bigcount)
