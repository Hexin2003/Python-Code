import string
file = open('Files To Read/words.txt')
d = dict()
for l in file:
    l = l.rstrip()
    l = l.strip()
    l = l.translate(l.maketrans('','',string.punctuation))
    l = l.lower()
    for c in l:
        if c == '\n' or c == ' ': continue
        d[c] = d.get(c,0) + 1
lst = list()
for k,v in d.items():
    lst.append((v,k))
lst = sorted(lst,reverse=True)
print(lst)
