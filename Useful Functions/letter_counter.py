#Function to count letters in a word
def count(w,l):
    count = 0
    for l in w:
        if l == 'a':
            count = count + 1
    return count

#Example of using the function
word = "Bannana"
print(count(word,'a'))