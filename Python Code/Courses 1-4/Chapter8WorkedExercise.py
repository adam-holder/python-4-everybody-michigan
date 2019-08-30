han = open('mbox-short.txt')

#Ver1
for line in han:
    line = line.rstrip()
    #print('Line:',line)
    wds = line.split()
    #print('Words:',wds)
    # Guardian Path
    if len(wds)<1:
        continue
    if wds[0] != 'From' :
        print ('Ignore')
        continue
    print (wds[2])

#Ver2
for line in han:
    line = line.rstrip()
    wds = line.split()
    #Guardian a bit stronger
    if len(wds)<3:
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2])

#Ver3
for line in han:
    line = line.rstrip()
    wds = line.split()
    #Guardian in a compound statement. ORDER MATTERS. Flip the order and
    #the statement fails because wds[0] != 'From' : fails.
    if len(wds)<3 or wds[0] != 'From' :
        continue
    print(wds[2])
 
