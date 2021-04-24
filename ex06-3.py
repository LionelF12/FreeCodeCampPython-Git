def count(a,b):
    tcount = 0
    lcount = 0
    for i in a:
        if len(b)==1:
            tcount = tcount + 1
            if i == b:
                lcount = lcount + 1
        elif len(b) != 1:
            print('ERROR one letter only')
            break
    print('total letters: ',tcount, 'total good letter:', lcount)

x = input('enter a word: ')
y = input('enter your letter choice: ')

count(x,y)
