Ligne = int(input("Entrez le nombre de Ligne : "))
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# * * * * * * * * * * * 

# for i in range(0, Ligne):
#     for j in range(0, Ligne-i):
#         print("  ", end="")
#     for j in range(0, 2*i-1):
#         print("* ", end="")
#     print() 

#########################################################


#           * 
#         *   * 
#       *       * 
#     *           * 
#   *               * 
# * * * * * * * * * * * 

for i in range(1, Ligne+1):
    for j in range(1, Ligne-i+1):
        print("  ", end="")
    for j in range(1, 2*i-1+1):
        if j == 1 or j == 2*i-1 or i ==Ligne :
            print("* ", end="")
        else :
            print("  ", end="")
    print()    

