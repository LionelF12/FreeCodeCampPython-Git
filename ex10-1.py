fhandle = open('mbox.txt','r')
emailtrack = dict()

for line in fhandle:
    if line.startswith('From '):
        email = line.split(' ')[1]
        emailtrack[email] = emailtrack.get(email, 0 )+ 1
print(emailtrack)

temp = list()
for k,v in emailtrack.items():
    temp.append( (v,k) )

sortedemail = sorted(temp,reverse=True)
x,y = sortedemail[0]
print(y,x)