filename = 'words.txt'
fhandle = open(filename,'r')
x = dict()

for line in fhandle:
    words = line.split()
    for word in words:
        x[word.lower()] = x.get(word.lower(),0) + 1
print(x)
print('writing' in x.keys())
