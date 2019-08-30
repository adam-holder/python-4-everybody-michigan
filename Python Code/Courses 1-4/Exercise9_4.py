name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emailHistogram = dict()

for line in handle:
    if not line.startswith('From ') : continue
    lineList = line.split()
    emailNeeded = lineList[1]
    emailHistogram[emailNeeded] = emailHistogram.get(emailNeeded,0)+1

frequantEmail = None
emailOccurance = None

for email,occurance in emailHistogram.items():
    if emailOccurance is None or occurance > emailOccurance:
        frequantEmail = email
        emailOccurance = occurance

print (frequantEmail, emailOccurance)
