num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    #forces an exit when we are ready to calculate the sum
    if sval == 'done' :
        break
    #brings us to the top of the loop if someone types a bad value
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    # print(fval)
    #count
    num = num + 1
    #total
    tot = tot + fval

# print('All Done')
print(tot, num, tot/num)
