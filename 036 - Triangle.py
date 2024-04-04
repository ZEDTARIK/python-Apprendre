Ligne = int(input("Entrez le nombre de Ligne : "))
Colonne = int(input("Entrez le nombre de Colonne : "))

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# * * * * * * * * * * * 

# for i in range(1, Ligne+1):
#     for j in range(1, Ligne-i+1):
#         print("  ", end="")
#     for j in range(1, 2*i-1+1):
#         print("* ", end="")
#     print() 

#########################################################


#           * 
#         *   * 
#       *       * 
#     *           * 
#   *               * 
# * * * * * * * * * * * 

# for i in range(1, Ligne+1):
#     for j in range(1, Ligne-i+1):
#         print("  ", end="")
#     for j in range(1, 2*i-1+1):
#         if j == 1 or j == 2*i-1 or i ==Ligne :
#             print("* ", end="")
#         else :
#             print("  ", end="")
#     print()    

#########################################################

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# p = 1
# for i in range(1, Colonne*2-1+1) :
#     for j in range(1, p+1):
#         print("* ", end="")
#     if i < Colonne : p+=1
#     else : p-=1
#     print()
#########################################################


#           * 
#         * * * 
#       * * * * * 
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

# espace = Ligne -1 
# etoile =  1

# for i in range(1, Ligne*2):
#     for j in range(0, espace):
#         print("  ", end="")
#     for j in range(1, etoile*2):
#         print("* ", end="")
#     if  i < Ligne :
#         espace -= 1
#         etoile += 1
#     else :
#         espace += 1
#         etoile -= 1
#     print("")

#########################################################

# Lettre A : 

#   * * *   
# *       *
# *       *
# * * * * *
# *       *
# *       *
# *       *

# for i in range(1, Ligne+1):
#     for j in range(1, 6):
#         if (j == 1 or j==5) and (i != 1):
#             print("* ", end="")
#         elif (i ==1 or i ==(Ligne+1)//2) and (j>1 and j<5):
#             print("* ", end="")
#         else :
#             print("  ", end="")
#     print()


#########################################################

# 1  1  1  1  1  1  1  1
# 2  2  2  2  2  2  2  2
# 3  3  3  3  3  3  3  3
# 4  4  4  4  4  4  4  4

# for i in range (1, Ligne+1):
#     for j in range(1, Colonne+1):
#         print(i, end=" ")
#     print(i)

#########################################################

# * * * * * *
# *         *
# *         *
# * * * * * *
# for i in range (1, Ligne+1):
#     for j in range (1, Colonne+1):
#         if i == 1 or i == Ligne or j == 1 or j == Colonne:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

###########################################

# * * * * * * * * * 
# * *           * * 
# *   *       *   * 
# *     *   *     * 
# *       *       * 
# *     *   *     * 
# *   *       *   * 
# * *           * * 
# * * * * * * * * *

# for i in range(1, Ligne+1):
#     for j in range(1, Colonne+1):
#         if i == 1 or i == Ligne or j ==1 or j == Colonne or i == j or j== Ligne - i +1 :
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


###########################################################

#             + + + + + + + 
#           + + + + + + + 
#         + + + + + + + 
#       + + + + + + + 
#     + + + + + + + 
#   + + + + + + + 
# + + + + + + + 

# for i in range(1 , Ligne+1):
#     for j in range(1, Ligne - i+1):
#         print("  ", end="")
#     for j in range(1, Ligne+1):
#         print("+ ", end="")
#     print()

for i in range(1, 10 +1):
    print(i, " * ", Ligne, " = ", i*Ligne)