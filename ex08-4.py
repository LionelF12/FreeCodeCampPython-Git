filename = 'romeo.txt'
fhand = open(filename,'r')

wordlist = []
count = 0
for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordlist:
            wordlist.append(word)
        else: 
            continue

wordlist.sort()
print(wordlist)
print(len(wordlist))
    
