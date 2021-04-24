def computepay(h,r):
    if h > 40:
        pay = (h-40)*1.5*r+(40*r)
    else:
        pay = h*r
    return pay

hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
print(computepay(hours,rate))
