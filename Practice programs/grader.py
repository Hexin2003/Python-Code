grade = input("Enter score: ")

try:
    grade = float(grade)
except:
    grade = -1

def checkGrade(g):
    if (g > 1) | (grade < 0):
        return("Bad score")
    elif(g >= 0.9):
        return("A")
    elif(g >= 0.8):
        return("B")
    elif(g >= 0.7):
        return("C")
    elif(g >= 0.6):
        return("D")
    elif(g < 0.6):
        return("F")

print(checkGrade(grade))