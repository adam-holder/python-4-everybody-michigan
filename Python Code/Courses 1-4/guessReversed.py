import random
import time

guessesGiven = 0
currentGuess = random.randint(6,14)
currentGuessStr = str(currentGuess)
drinksTotal = 0
lowerRange = 1
upperRange = 20

def intro():
    print('\"Hello.\"')
    time.sleep(3)
    print('\"Do I know you?\"')
    time.sleep(3)
    print('''The mysterious voice drifting from the shadows beckons you forward.\nNothing but a smug smile can be seen from under a dark cloak''')
    time.sleep(5)
    screenclear()
    print('\"What is your name?\"')
    myName = input()
    time.sleep(3)
    print('''The figure pauses and looks up. From underneath the hood,\na familiar face looks up to greet you. ''')
    time.sleep(5)
    screenclear()
    print('Ah yes...' + myName + '...I have been expecting you old friend.')

def screenclear():
    print('\n'*100)

def answer():
    print('\"Did I get it?\"')
    if currentGuess == chosenNumber:
        print('Krag reads your face. He smiles.\n\n\"That was fun.\"')
    elif currentGuess < chosenNumber:
        #guess too low
        drinksTotal=drinksTotal+1
        lowerRange = currentGuess + 1
    elif currentGuess > chosenNumber:
        #guess too high
        drinksTotal=drinksTotal+1
        upperRange = currentGuess - 1

def guessAgain():
    currentGuess = random.randint(lowerRange,upperRange)
    print('\"Damn it...Alright my next guess is' + currentGuess)



#def restart():
    #alternate starting intro


#Plan
#Text intro. Think of a number between 1-20
#Prompts if they are ready for Comp to guess
#Makes a guess somewhere between 5-15 using random integer. Saves old guess to variable.
#Checks to see if number is right, low or high. (function maybe?)
#Based off of previous guess, if high guess from number guessed-1 to 1. If low guess from number guessed+1 to 20
intro()
print('''\"KRAG, Are ya gonna order or just stand there?\"\n\nBess starred at him, wiping down the counter.\n\nKrag walks over and motions to the seat next to you.\n\"Pop a squat\"''')
print('''\"Let's have some fun.\"\nKrag motions to Bess and puts out 6 fingers releasing some silver from the remaining curled fingers.\nShe looks up to see his cheeky smile, rolls her eyes and begins to pour 6 glasses.\n\n\n''')
print('''\"Think of a number between....uh....let's say 1 and uhhh 20.\"\n\n\"I'll guess. For each one I get guess I get wrong, I'll take a drink....Don't you cheat...\"\n\n\"Here write it down\"\n\nHe hands you a small piece of parchment.''')
print('You have a piece of parchment in front of you. Write a whole number between 1-20')
chosenNumber = input()
chosenNumber = int(chosenNumber)

print('\"Alright, you ready?\"\n\n\"My first guess is ' + currentGuessStr + '\"')


for guessesGiven in range(6):
    answer()
    if currentGuess != chosenNumber:
        guessAgain()
