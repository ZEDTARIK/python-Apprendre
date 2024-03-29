N= int(input("Entre la valeur de N: "))
M= N

count = 0
Inverse = 0
while N != 0 :
    Inverse = (Inverse * 10) + (N % 10)
    N = N // 10 
    count += 1
print("Nombre Total de chifre dans le nombre", M, " est", count)
print("L'inverse de chifre", M, "est :", Inverse)
