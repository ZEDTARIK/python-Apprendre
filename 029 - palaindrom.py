N = int(input("Entrez la valeur de N: "))
M= N 
Inverse = 0
while N != 0 :
    Inverse  = (Inverse *10) + (N % 10)
    N  = N // 10
    

if Inverse == M :
    print("le nombre est palindrome")
else :
    print("No le nomber n'est pas Palaindrome")