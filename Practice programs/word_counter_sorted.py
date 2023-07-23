def wordCounter(f):
    d = dict()
    for l in f:
        l = l.split()
        for w in l:
            d[w] = d.get(w,0) + 1
    lst = list()
    for key,val in d.items():
        newtup = (val,key)
        lst.append(newtup)
    lst = sorted(lst, reverse=True)
    for val,key in lst[:10] :
        print(key,val)

#Example of using the function
file = open('Files To Read/romeo.txt')
wordCounter(file)
