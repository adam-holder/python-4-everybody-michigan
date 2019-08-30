score = input("Enter Score: ")

#checks to see if the input is a valid number
try:
    score = float(score)
except:
    print('Please enter a valid number between 0.0 and 1.0')
    quit()

#checks to see if the number is in range
if score < 0 :
    print('This number is below the range.')
    print('Please enter a number between 0.0 and 1.0.')
    quit()
elif score > 1 :
    print('This number is above the range.')
    print('Please enter a number between 0.0 and 1.0.')
    quit()

#since the input is a number and in range it can be graded per the table given
else:
    if score >= 0.9 :
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    else:
        print('F')
