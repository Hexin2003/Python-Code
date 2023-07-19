fhand = open('Files To Read/mbox-short.txt')
dayz = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) == 0: continue
    day = words[2]
    dayz[day] = dayz.get(day,0) + 1

print(dayz)