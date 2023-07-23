import re
file = open('Files To Read/mbox-short.txt')
reg = '^New Revision: ([0-9]+)'
count = 0
total = 0
for line in file:
    line = line.rstrip()
    s = re.findall(reg,line)
    if len(s) > 0:
        s = int(str(s[0]))
        total = s + total
        count = count + 1
print(int(total/count))