A=int(input("Entre la valeur de A: "))
B=int(input("Entre la valeur de B: "))

if A*B>0 :  
    print("A et B en le même Signe")
    A,B= B, A 
    print("la nouvelle valeur de A est :", A)
    print("la nouvelle valeur de B est :", B)
else : 
    print("A et B sont differentes Signe")
    C= A+B
    B= A*B
    A= C
    print("la nouvelle valeur de A est :", A)
    print("la nouvelle valeur de B est :", B)
    

