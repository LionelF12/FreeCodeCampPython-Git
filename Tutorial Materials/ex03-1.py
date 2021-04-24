try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    if hours > 40:
        pay = (hours-40)*1.5*rate + 40*rate
    else:
        pay = hours * rate
    print('your pay is',pay)
except:
    print('ERROR please enter numeric input')
