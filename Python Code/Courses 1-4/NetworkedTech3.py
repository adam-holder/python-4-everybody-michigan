import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    #line.decode() gives you a string. All string methods work on it.
    words = line.decode().split()
    for word in words:
        count[word] = counts.get(word, 0) + 1
print (counts)

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    #converts each line of that page to a string and prints it out
    print(line.decode().strip())
