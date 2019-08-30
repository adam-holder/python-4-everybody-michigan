name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hourHistogram = dict()

for line in handle:
    if not line.startswith('From ') : continue
    lineList = line.split()
    dateNeeded = lineList[5]
    #print (dateNeeded)
    timeList = dateNeeded.split(':')
    hourNeeded = timeList[0]
    hourHistogram[hourNeeded] = hourHistogram.get(hourNeeded,0) + 1
#print (hourHistogram)
sortedHistogram = sorted( [ (k,v) for k,v in hourHistogram.items()])
#print (sortedHistogram)
for k,v in sortedHistogram:
    print (k, v)


#HELLO THERE COURSE 3
