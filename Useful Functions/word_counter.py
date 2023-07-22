def wordCounter(f):
    d = dict()
    for l in f:
        l = l.split()
        for w in l:
            d[w] = d.get(w,0) + 1
    return(d)

#Example of using the function
file = open('Files To Read/romeo.txt')
print(wordCounter(file))
