import re
file = open('Files To Read/data_for_regex_assignment.txt')
reg = '[0-9]+'
total = 0
for line in file:
    line = line.rstrip()
    #returns a list
    s = re.findall(reg,line)
    #if the list contains anything convert each index to an 
    #integer and add it to total
    if len(s) > 0:
        for i in s:
            i = int(i)
            total = i + total
print(total)