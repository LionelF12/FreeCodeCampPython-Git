str = 'X-DSPAM-Confidence:0.8475'
# str.find(':')
x = str[str.find(':')+1:]

print(float(x))
print(type(float(x)))
