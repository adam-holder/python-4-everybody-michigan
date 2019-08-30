fname = input ("Enter file name: ")
fh = open(fname)
splitRomeo = list()
for line in fh:
    line = line.rstrip()
    wordTest = line.split()
    for word in wordTest:
        if word not in splitRomeo:
            splitRomeo.append(word)
splitRomeo.sort()
print (splitRomeo)
