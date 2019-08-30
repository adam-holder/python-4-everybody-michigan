fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
emailCount = 0

for line in fh:
    if not line.startswith('From ') : continue
    line = line.rstrip()
    lineList = line.split()
    emailNeeded = lineList[1]
    print (emailNeeded)
    emailCount = emailCount + 1
print (print("There were", emailCount, "lines in the file with From as the first word"))
