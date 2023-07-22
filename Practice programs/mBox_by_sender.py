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

lst = list()
for k,v in sender.items():
    #creates a list of tuples with the
    #key:value pairs in reverse order
    lst.append( (v,k) )
#sorts the list with from high to low
lst = sorted(lst,reverse=True)
# resets the list to proper key:value order
for v,k in lst[:1]:
    print(k,v)



#Old code showing how to use a max loop
#to find the greatest number of messages
'''for key in sender:
    if sender.get(key,0) > most:
        most = sender.get(key,0)
        sendHand = key
print(sendHand, most)'''