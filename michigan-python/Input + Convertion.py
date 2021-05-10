#Se crean los inputs
rate = input("Enter Rate:")
hrs = input("Enter Hours:")

#Se toman los valores y se convierten en float ambos por que string y float no se pueden multiplicar directamente
pay = float(rate) * float(hrs)

#Se imprime el resultado de pay
print("Pay:",pay)