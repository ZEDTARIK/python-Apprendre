# This Python code snippet is calculating the total resistance in a series circuit and the equivalent
# resistance in a parallel circuit.

R1=float(input("Enter the value of R1: "))
R2=float(input("Enter the value of R2: "))
R3=float(input("Enter the value of R3: "))

Res= (R1+R2+R3)
Rpar=(R1*R2*R3)/(R1*R2 + R1*R3 + R2*R3)

print("la valeur de la résistance en série est de : ", format(Res, ".2f"))
print("la valeur de la résistance en paralléle est de : ", format(Rpar, ".2f"))