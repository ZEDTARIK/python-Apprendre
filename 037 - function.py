# def Table_Multuplication(N):
#     for i in range(1, 11):
#         print(i, " * ", N , " = ", i*N)
#     print()

# while True:
#     N = int(input("Saisir un nombre : "))
#     if N > 0:
#         break

### Testing
#Table_Multuplication(3)


########################################################################

def Cube(C):
    return C*C*C 

for i in range(1, 1000):
    print("Le resultat de Cube de ", i, " est :", Cube(i))