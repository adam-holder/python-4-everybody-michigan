hours = input("Enter Hours:")
rate = input("Enter your pay rate:")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, you done goofed and didn't put a number")
    quit()

pay = 0
otHours = 0
otRate = 0

if hours > 40 :
    otHours = hours - 40
    otRate = rate * 1.5
    hours = 40
    pay = (hours*rate) + (otHours*otRate)
else :
    pay = (hours*rate)
print(pay)
