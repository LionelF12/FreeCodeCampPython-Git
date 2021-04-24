try:
    uscore = float(input('Please enter a number: '))
    if uscore <=1.0:
        if uscore >= 0.9:
            print('A')
        elif uscore >=0.8:
            print('B')
        elif uscore >=0.7:
            print('C')
        elif uscore >=0.6:
            print ('D')
        else:
            print ('F')
    else:
        print('ERROR')
except:
    print('ERROR EXCEPT')
