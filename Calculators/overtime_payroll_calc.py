import math
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
OTr = rate * 1.5
def computepay(h,r):
    if h <= 40:
        return(h*r)
    elif h > 40:
        return((h - 40) * OTr + 40*r)       

print("Pay:", computepay(hours,rate) )
