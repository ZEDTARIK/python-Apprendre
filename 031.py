N =int(input("Entrez la valeur de N : "))

order= 0
b = 0 

while N !=0 :
    reste = N % 2
    p = 10 ** order
    b= b + reste * p 
    order  = order + 1
    N = N // 2

print(b)