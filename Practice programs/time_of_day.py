import re
fhand = open('Files To Read/mbox-short.txt')
time = dict()
for line in fhand:
    words = line.rstrip()
    hour = str(re.findall('^From .* ([0-9][0-9]):',words))[2:4]
    if len(hour) > 0:
        time[hour] = time.get(hour,0) + 1
lst = list()
#sorts the dictonary by keys
for k,v in sorted(time.items()):
    print(k,v)
