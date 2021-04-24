fhandle = open('mbox-short.txt')

domaind = {}

for line in fhandle:
    if line.startswith('From '):
        line = line.strip()
        email = line.split()[1]
        domain = email.split('@')[1]
        domaind[domain] = domaind.get(domain,0)+1
print(domaind)
