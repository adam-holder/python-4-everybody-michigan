import re

#I called the file "actualfile.txt"
name = input("Enter file:")
handle = open(name)
numberSum = 0

#This code goes line by line and finds each number in the line using Regular Expressions
#for each line it saves a list in findNumbers (skips the line if there are no results to find)
for line in handle:
    line = line.rstrip()
    findNumbers = re.findall('[0-9]+', line)
    if len(findNumbers) == 0 : continue
    #This loop takes the pieces of each iteration of findNumbers and converts them to
    #integers. It then adds the integers to the running total, numberSum.
    for piece in findNumbers:
        num = int(piece)
        numberSum = numberSum + num
    #USED FOR TESTING
    #print (findNumbers, numberSum)
print(numberSum)
