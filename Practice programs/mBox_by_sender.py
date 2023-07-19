fhand = open('Files To Read/mbox-short.txt')
sender = dict()
t = []
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) == 0: continue
    sendHand = words[1]
    sender[sendHand] = sender.get(sendHand,0) + 1
most = 0
sendHand = None
for key in sender:
    if sender.get(key,0) > most:
        most = sender.get(key,0)
        sendHand = key
print(sendHand, most)