import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

#...Same as...#
#hand = open('mbox-short.txt')
#for line in hand:
    #line = line.rstrip()
    #if line.startswith('From:'):
        #print(line)
#...Same as...#



#I'm looking for X followed by any character any number of times followed by a :
# ^X.*:
#fine-tuning...
# ^X-\S+:
#This means I'm looking for a line starting with X- followed by none whitespace characters
#one or more times followed by a colon

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
