#path to file Files To Read\words.txt
file = input("Enter file name:")
fhand = open(file)
wordDict = dict()
words = []
for line in fhand: 
    line = line.rstrip()
    word = line.split(' ')
    for num in word:
        wordDict[num] = None
checkWord = "Writing"

if checkWord in wordDict:
    print(checkWord)