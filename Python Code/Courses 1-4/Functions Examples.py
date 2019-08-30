#lang is a parameter. A parameter is a variable which we use
#in the function definition. It is a "handle" that allows the code in the
#fuction to access the arguments for a particular function invocation.
def greet(lang):
    if lang == 'es':
        print ('Hola')
    elif lang == 'fr':
        print ('Bonjour')
    else:
        print ('Hello')

def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print (x)
