def computegrade(x):
    try:
        x = float(x)
    except:
        return 'ERROR'
    if x <= 1.0:
        if x >= 0.9:
            return 'A'
        elif x >=0.8:
            return 'B'
        elif x >= 0.7:
            return 'C'
        elif x>= 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return 'Please enter a number'

grade = input('Please enter your grade: ')
print(computegrade(grade))
