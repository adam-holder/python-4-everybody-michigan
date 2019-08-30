counts = dict()
#list of names
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    #We can use get(item, default value). In the example
    #we use a default value of zero. Get looks at the dictionary which starts
    #as blank here and attempt to find "item" if it cannot, it assigns
    #the default value.

    #This code takes the value in name and either makes a new entry or updates
    #an old entry.
    counts[name] = counts.get(name,0) + 1
print(counts)


name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print (bigword, bigcount)
