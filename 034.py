L = int(input("Entrez la valeur de L : "))

for i in range(1,L+1) :
    for j in range(1, L+1) :
        if i == 1 or i == L or j== 1 or j == L or i == j or j == L-i+1 : 
            print("* ", end="")
        else :
            print("  ", end="")
    print()


# * * * * * * * * * * * * * * * * * * * *
# * *                                 * *
# *   *                             *   *
# *     *                         *     *
# *       *                     *       *
# *         *                 *         *
# *           *             *           *
# *             *         *             *
# *               *     *               *
# *                 * *                 *
# *                 * *                 *
# *               *     *               *
# *             *         *             *
# *           *             *           *
# *         *                 *         *
# *       *                     *       *
# *     *                         *     *
# *   *                             *   *
# * *                                 * *
# * * * * * * * * * * * * * * * * * * * *