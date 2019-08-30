largest = None
smallest = None
#computes largest and smallest integers based off of human input
while True :
    num = input("Enter an integer: ")
    if num == 'done':
        break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None :
        smallest = inum
        largest = inum
    elif inum < smallest :
        smallest = inum
    elif inum > largest :
        largest = inum
    #print ('S',smallest,'B',largest)
print ('Maximum is',largest)
print ('Minimum is',smallest)
