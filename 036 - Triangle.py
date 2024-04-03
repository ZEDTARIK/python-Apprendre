Ligne = int(input("Entrez le nombre de Ligne : "))
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# * * * * * * * * * * * 

for i in range(0, Ligne):
    for j in range(0, Ligne-i):
        print("  ", end="")
    for j in range(0, 2*i-1):
        print("* ", end="")
    print() 


    