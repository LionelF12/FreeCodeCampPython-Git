
fhand = open('mbox-short.txt','r')

for line in fhand:
    if line.startswith('X-DSPAM-Conf'):
        print(line.upper().rstrip())