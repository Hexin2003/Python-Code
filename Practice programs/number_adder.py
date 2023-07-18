total = 0
count = 0 
avg = 0
while True:
    num = None
    num = input("Enter a Number: ")
    if num == "done":
        avg = total/count
        print(total,count,avg)
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    total = num + total
    count = count + 1
