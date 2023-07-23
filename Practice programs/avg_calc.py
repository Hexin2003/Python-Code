total = 0
count = 0
avg = None
while True:
    num = None
    num = input("Enter a Number: ")
    if num == "done":
        if count != 0:
            avg = total/count
        print("Total:", total, "\nAmount of numbers:", count, "\nAverage: ", avg)
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    total = total + num
    count = count + 1

