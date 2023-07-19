fhand = open('Files To Read/mbox-short.txt')
domains = dict()
t = []
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) == 0: continue
    sendHand = words[1]
    sendHand = sendHand.split('@')
    domain = sendHand[1]
    domains[domain] = domains.get(domain,0) + 1
print(domains)