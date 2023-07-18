maxNum = None
minNum = None
while True:
    num = None
    num = input("Enter a Number: ")
    if num == "done":
        print("Max:", maxNum, " Min:", minNum)
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if maxNum == None:
        maxNum = num
    elif maxNum < num:
        maxNum = num
    if minNum == None:
        minNum = num
    elif minNum > num:
        minNum = num