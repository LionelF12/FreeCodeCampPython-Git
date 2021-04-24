#def chop(listorig):
#    listorig.pop(0)
#    listorig.pop()
#    return listorig
#print(chop(['a','b','c','d']))

def middle(lista):
    return lista[1:-1]

lista = ['a','b','c','d','e']
newlist = middle(lista)

print(newlist)
