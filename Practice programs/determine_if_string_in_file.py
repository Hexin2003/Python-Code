#path to file Files To Read\words.txt
file = input("Enter file name:")
fhand = open(file)
wordList = dict()
words = []
for line in fhand: 
    line = line.rstrip()
    word = line.split(' ')
    for num in word:
        wordList[num] = None

checkString = 'Writing programs is a very creatice an rewarding activity'
if checkString in wordList:
    print(checkString)