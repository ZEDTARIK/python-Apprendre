print("Programme qui calcule la somme d’une série harmonique")

N=int(input("Entre la valeur de N : "))
S=0

for i in range(1,N+1):
    S= S+1 / i
print("La somme d’une série harmonique est :", format(S, ".2f"))