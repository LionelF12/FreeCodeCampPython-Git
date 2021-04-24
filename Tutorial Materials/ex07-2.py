
fhand = open('mbox.txt','r')

count = 0
totspam = 0 
for line in fhand:
    if line.startswith('X-DSPAM-Conf'):
        count = count + 1
        colonloc = line.find(':')
        number = float(line[colonloc+1:].strip())
        totspam = totspam + number
print(totspam,(totspam/count))