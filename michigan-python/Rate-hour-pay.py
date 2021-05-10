def computepay(h,r): #Se define computepay para utilizarlo mas adelante y las condiciones
    if h > 40:
        pa = 40 * r + (h-40)*1.5*r
    else:
        pa = h * r
    return pa

hrs = input("Enter Hours:") #Input
h = float(hrs) #Se transforma en float
rate = input("Enter Rate") #Input
r = float(rate) #Se transforma en float
p = computepay(h,r)

print("Pay",p)