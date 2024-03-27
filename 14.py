# This Python code snippet is solving a quadratic equation (équation du second degré) using the
# quadratic formula. Here's a breakdown of what the code does:
import math 

print("équation du second degré :  ")

a= float(input("Enter la valeur de a : "))
b= float(input("Enter la valeur de b : "))
c= float(input("Enter la valeur de c : "))

delta= b**2 - 4*a*c 

if delta < 0 :
    print("Pas de solutions réelles")
elif delta == 0 :
    x = (-b)/(2/a)
    print("la solution est :", x)
else :
    x1 = (-b -math.sqrt(delta)) / (2*a)
    x2= (-b  +math.sqrt(delta)) / (2*a)
    print("Les solutions sont : ", format(x1, ".2f"), " et ", format(x2, ".2f"))
