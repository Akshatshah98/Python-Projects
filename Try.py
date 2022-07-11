from decimal import *
x = int(input("Enter your number: "))
x += 1
getcontext().prec = x
pi = Decimal(22)/ Decimal(7)
print(pi)
