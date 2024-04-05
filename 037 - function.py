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

# def Cube(C):
#     return C*C*C 

# for i in range(1, 1000):
#     print("Le resultat de Cube de ", i, " est :", Cube(i))

########################################################################

# Nombre premier est de n’être divisible que par deux entiers distincts, 1 et lui-même
# def NombrePremier(N):
#     estpremier=1
#     for i in range(2, int(N//2)+1):
#         if N%i==0:
#             estpremier=0
#             break
#     if estpremier==1:
#         print(N, " est premier")
#     else:
#         print(N, " n'est pas premier")

# while True:
#     N = int(input("Saisir un nombre : "))
#     if N > 0:
#         break
#NombrePremier(N)

# for i in range(1, 21):
#     NombrePremier(i)

########################################################################

# def Compte(N):
#     Nbr= 0
#     while N!= 0:
#         N = int(N/10)
#         Nbr += 1
#     return Nbr

# N = int(input("Saisir un nombre : "))
# print("Le nombre total de chiffre dans le nombre ", N, " est de ", Compte(N), " chiffre")    

import unittest

def Compte(N):
    Nbr = 0
    if N < 0:
        N = -N
    while N != 0:
        N = int(N / 10)
        Nbr += 1
    return Nbr

class TestCompteFunction(unittest.TestCase):

    def test_count_digits(self):
        self.assertEqual(Compte(123), 3)
        self.assertEqual(Compte(0), 0)
        self.assertEqual(Compte(1000), 4)
        self.assertEqual(Compte(1234567890), 10)
        self.assertEqual(Compte(-123), 3)  # Negative numbers are also valid

if __name__ == '__main__':
    unittest.main()
########################################################################