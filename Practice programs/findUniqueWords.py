file = open('Files To Read/romeo.txt')
words = []
for line in file: 
    line = line.rstrip()
    word = line.split(' ')
    for num in word:
        if words.count(num) == 0:
            words.append(num)
words.sort()
print('the list:',words)