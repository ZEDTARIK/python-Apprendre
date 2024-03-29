L = int(input("Entre la valeur de L (Ligne): "))
C = int(input("Entre la valeur de L (Colonne): "))

# while True:
#     if (L== 0 or L== 1) and (C ==0 or C ==1) :
#         L = int(input("Entre la valeur de L (Ligne): "))
#         C = int(input("Entre la valeur de L (Colonne): "))
#         break

for i in range(1, L+1):
    for j in range(i) :
        print("*", end=" ")
    print("")

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 

for i in range(1, L+1):
    for j in range(1, L-i+1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print("")

#            * 
#          * * 
#        * * * 
#      * * * * 
#    * * * * * 
#  * * * * * * 
    

for i in range(1, L+1):
    for j in range(1, C+1):
        if i == 1  or i == L or j == 1 or j == C :
            print("+", end=" ")
        else :
            print(" ", end=" ")
    print("")

#  + + + + + + 
#  +         + 
#  + + + + + +     