print(" S = 1 + 10 + 100 +...+10 OS n")

N=int(input("Entrez la valeur de N: "))
S=0

for i in range(0, N+1):
    S= S + (10**i)
print("Le resultat est : ", S)