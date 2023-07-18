name  = "John"
print("Hello")

#Function to print lyrics taking no arguments
def print_lyrics():
    print("I'm a lumberjack")
    print("I work all day and sleep all night")

print_lyrics()

#Function to print a greeting taking an argument
def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    elif lang == 'en':
        return("Hello")

greet('es')
greet('fr')
greet('en')

#Function to return a goodbye using one argument
def bye(lang):
    if lang == 'es':
        return("Adios")
    elif lang == 'fr':
        return("Bye but in french")
    elif lang == 'en':
        return("Bye")
    
print(bye('es'),name)
print(bye('fr'),name)
print(bye('en'),name)