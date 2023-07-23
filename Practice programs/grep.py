import re
file = open('Files To Read/mbox-short.txt')
reg = input('Enter a regular expression: ')
count = 0
for line in file:
    line = line.rstrip()
    s = re.findall(reg,line)
    if len(s) > 0:
        count = count + 1
print('mbox.txt had', count, 'lines that matched',reg)