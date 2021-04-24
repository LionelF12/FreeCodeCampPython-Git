filename = input('enter a file name: ')
count = 0

if filename == 'na na boo boo':
        print ('NA NA BOO BOO TO YOU')
        quit()
try:
    fhand = open(filename,'r')
except:
    print('File cannot be opened: '+ filename)
    quit()

for line in fhand:
    if line.startswith('Sub'):
        count = count + 1

print ('There were '+str(count)+' subject lines in '+filename)