# This Python code prompts the user to enter a value for `L`, and then it generates a pattern of stars
# and spaces based on the value of `L`. The pattern consists of a square with diagonal lines of stars
# from the top left to the bottom right and from the top right to the bottom left, as well as stars on
# the borders of the square.
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