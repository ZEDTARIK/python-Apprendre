while True:
    n=int(input("entre la valeur de N: "))
    if n >= 0:
        break
if n==0:
    print("La factoriel de 0 est 1")
else:
    F=1
    for i in range(2,n+1):
        F = F * i
print("La factoriel de ",n , "est ", F)


