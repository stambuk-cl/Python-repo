hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
ratePlus = rate * 1.5
  
if hours > 40:
    pay = 40 * rate + (hours - 40) * ratePlus
  
else:
    pay = hours * rate
  
print (pay)