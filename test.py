string = "ultr53o?n"

def reverse_letter(string):
    lis = list(string)
    res = []
    for char in lis:
        if char.isalpha():
            res.insert(0,char)
    res = ''.join(res)
    return res

print(reverse_letter(string))