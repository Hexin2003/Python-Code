#Function to count the objects in a list
def listCounter(l):
    count = 0
    for itervar in l:
            count = count + 1
    return count



#Example of using the fuction
countList = [3, 41, 12, 9, 74, 15]
print("List count:", listCounter(countList))


#Function to add all items in a list together
def listAdder(l):
    total = 0
    for itervar in l:
        total = total + itervar
    return total



#Example of using the function
addList = [3, 41, 12, 9, 74, 15]
print("List total:", listAdder(addList))
