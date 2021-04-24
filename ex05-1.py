count = 0
average = 0
total = 0

while True:
    userint = input('Enter a number: ')
    if userint == 'done':
        break
    try:
        userint = float(userint)
    except:
        print('bad data')
        continue
    count = count + 1
    total = total + userint
    average = total/count

if count > 0:
    print(int(total),int(count),average)
