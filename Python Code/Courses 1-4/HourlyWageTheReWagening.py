#function to compute gross pay given the amount of hours and rate of pay
def computepay(hours,rate):
    if hours > 40 :
        otHours = hours - 40
        otRate = rate * 1.5
        hours = 40
        pay = (hours*rate) + (otHours*otRate)
    else :
        pay = (hours*rate)
    return pay

#user input of hours and rate
ihours = input("Enter Hours:")
irate = input("Enter your pay rate:")

#error checking for input
try:
    ihours = float(ihours)
    irate = float(irate)
except:
    print("Error, you did not enter a number")
    quit()

p = computepay (ihours, irate)
print (p)
