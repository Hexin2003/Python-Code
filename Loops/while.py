n = 5
print("Example of a normal while loop:")
#Runs five iterations printing the iteration variables then ends the loop and prints Blastoff
while n > 0 :
    print(n)
    # It is important to iterate the varible in the coditional to avoid an infiinite loop
    n = n - 1 
print("Blastoff")

print("Example of an infinite loop with breaks and continues")
while True:
    n = input("Type something here: ")
#Use breaks to stop the code from iterating
    if n == "done":
        print("Done")
        break
#Use continue to stop iterating and move back to the top of the loop
    if n[0] == "#":
        continue
    print(n)