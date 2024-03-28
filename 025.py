# This Python code calculates the sum of the squares of the first N odd numbers.
N=int(input("Calculer la somme des carres de N premiers nombres impairs : "))
S=0
J=1
for i in range(N):
    S= S + ( J ** 2)
    J= J+2  #Impair

print("Le resultat est :", S)

# 8 ->  680