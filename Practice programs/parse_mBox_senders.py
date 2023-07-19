fhand = open('Files To Read/mbox-short.txt')
count = 0
for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split(' ')
    if len(words) == 0: continue
    sender = words[1]
    print(sender)
    count = count + 1

print('There were', count, 'lines in the file with From as the first word')