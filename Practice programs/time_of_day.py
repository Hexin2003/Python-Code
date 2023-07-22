fhand = open('Files To Read/mbox-short.txt')
time = dict()
t = []
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) == 0: continue
    fullTime = words[5]
    hour = fullTime.split(':')
    hour = hour[0]
    time[hour] = time.get(hour,0) + 1
lst = list()
#sorts the dictonary by keys
for k,v in sorted(time.items()):
    print(k,v)
