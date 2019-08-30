hours = input("Enter Hours:")
rate = input("Enter your pay rate:")
hours = float(hours)
rate = float(rate)
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
