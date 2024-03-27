# This Python code snippet is a simple calculator program that takes two input values `A` and `B` from
# the user, as well as an operator `Op` (such as +, -, /, *).


A = float(input("Entrez la valeur de A: "))
B = float(input("Entrez la valeur de B: "))
Op=input("Entrez l'operateur : ")

if Op == "+" :
    print("A + B : ", A+B)
elif Op == "-" :
    print("A - B : ", A-B)
elif Op == "/" :
    if B != 0 :
        print("A / B : ", A/B)
    else :
        print("la division sur 0 est impossible")
elif Op == "*" :
    print("A * B : ", A*B)
else :
    print("l'operateur nes pas valide")
