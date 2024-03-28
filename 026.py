#Programme qui calcule et affiche les diviseurs d’un nombre

N=int(input("Entre Le nombre de N: "))

while N <= 0:
    N=int(input("Entre Le nombre de N "))

print("Les diviseur de", N, "sont: ")

for i in range(1, N+1):
    if N%i == 0:
        print(i, end=" ")
