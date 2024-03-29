 #Inverse Number 
N = int(input("Entrez la valeur de N: "))
M= N 
P =N 

inverse = 0

while N !=0 :
    inverse = (inverse *10 ) + (N % 10)
    N = N //10 
print("Inverse de:", M, "est:", inverse)

print("---------------------------------------------------")

# palindrome
if inverse == M :
    print("Le nombre est palindrome", inverse)
else : print ("Le nombre n'est pas palindrome", M)

print("---------------------------------------------------")

# boucle 0 -> 10 
for i in range(0, 11):
    print(i, end= " ")

print("---------------------------------------------------")
      
# Somme Array 
arrays = [10, 8, 2] # 20 
sum = sum(arrays)
print("Somme Array", sum)

print("---------------------------------------------------")

# Nombre Pair / Impair 

if M % 2 == 0: 
    print ("Nombre Pair", M)
else: 
    print ("Nombre Impair", M)

print("---------------------------------------------------")

# Factoriel
F = 1
for i in range(1, 6): 
    F =F * i 

# Nombre parfait 
S = 0 
for i in range(1, P): 
    if P % i == 0: 
        S =S + i
if S == P: 
    print("le nombre est parfait", P)
else : 
    print("le nombre n'est pas parfait")