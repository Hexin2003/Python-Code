data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#Finds the position of the @ symbol
atpos = data.find('@')
print(atpos)
#finds the first space after the position of the @ symbol
sppos = data.find(' ',atpos)
print(sppos)
#prints a string slice containing all data 
#between the first @ symbol and the next blank space after that
host = data[atpos+1:sppos]
print(host)

#Parsing Practice
data = 'X-DSPAM-Confidence:0.8475'
colonpos = data.find(':')
floatpos = data[colonpos+1:]
num = float(floatpos)
print(num)

