count = 0
total = 0
avg = 0
fileName = input('Enter a file name: ')
try: 
    fhand = open(fileName)
except:
    if(fileName != "na na boo boo"):
        print("File cannot be opened:", fileName)
        exit()
    else: 
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        conf = float(line[19:])
        count = count + 1 
        total = total + conf
print("Average spam confidence:",total/count)
        