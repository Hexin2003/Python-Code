def chop(t):
    del t[0]
    del t[-1]
    return(None)

def middle(t):
    safeT = t[1:-1]
    return(safeT)
#Example of using chop
exampleList = [27,21,19,31,45,63,19]
print('list before chop: ', exampleList)
print('this should be None', chop(exampleList))
print('List after chop: ', exampleList,'\n')

#Reset list back to normal
exampleList = [27,21,19,31,45,63,19]
print('List before middle: ', exampleList)
print('New list after middle:', middle(exampleList))
print('Showing the old list was not modified:', exampleList,'\n')
