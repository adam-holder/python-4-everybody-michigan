fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

runningTotal = 0
lineCount = 0

#loops through the lines of the text to find the lines we need
#takes those lines and finds the colon, strips off the intro and strips the Result
#leaving just the number. Adds the number to a running total and counts the line
#when the loop is finished, it divides the running total by the number of lines to find the average.

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line.strip()) - used to test loop and make sure it was collecting the correct date
    linepos = line.find(':')
    numberEntry = line[linepos+1:]
    numberEntry = float(numberEntry.strip())
    runningTotal = numberEntry + runningTotal
    lineCount = lineCount + 1
averageOfLines = runningTotal/lineCount
print('Average spam confidence:',averageOfLines)
