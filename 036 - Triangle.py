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
p = 1
for i in range(1, Colonne*2-1+1) :
    for j in range(1, p+1):
        print("* ", end="")
    if i < Colonne : p+=1
    else : p-=1
    print()