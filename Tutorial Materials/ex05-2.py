def test():
    count = 0
    total = 0
    max = None
    min = None

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
        if max == None:
            max = userint
        elif userint > max:
            max = userint
        if min == None:
            min = userint
        elif userint < min:
            min = userint
    if count > 0:
        print(int(total),int(count),int(min),int(max))
    return total

if test() == 16:
    print('16')
