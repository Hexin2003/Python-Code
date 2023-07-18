maxNum = None
minNum = None
t = []
while True:
    num = None
    num = input("Enter a Number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    t.append(num)
maxNum = max(t)
minNum = min(t)
print("Maximum:", maxNum)
print('Minimum:',minNum)