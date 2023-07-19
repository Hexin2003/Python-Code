
def charCounter(w):
    d = dict()
    for c in w:
        d[c] = d.get(c,0) + 1
    return(d)

#Example of using the function
word = 'Brontosaurus'
print(charCounter(word))
