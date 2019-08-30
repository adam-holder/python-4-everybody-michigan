#LARGEST NUMBER
#setting the initial largest_so_far
largest_so_far = -1
#prints the current largest_so_far pre loop
print('Before', largest_so_far)
#if the entry is the largest_so_far, set that number to largest_so_far.
#Then print current largest_so_far and the current the_num
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#Counting
zork = 0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

#Summing - Adding the next "thing" instead of just a count
zork = 0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

#average
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

#filtering
print('Before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print ('Large number', value)
print('After')

#boolean - is there a 3? if there were 1000 numbers, we found a 3.
#break as soon as we find a 3
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3 :
        found = True
        break
    print (found, value)
print('After', found)

#None type (EMPTY SET) - Flag Value for this problem
#Used for smallest number
smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if value is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
