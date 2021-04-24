
numberbox = []
while True:
    inp = input('Enter a number:')
    if inp == 'done':
        break
    else:
        numberbox.append(int(inp)) 
print(numberbox)
print(max(numberbox))
print(min(numberbox))