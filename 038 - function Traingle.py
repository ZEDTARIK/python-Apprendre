def triangle(L):
    """Prints a triangle of L lines"""
    for i in range(1, L + 1):
        for j in range(1, L-i + 1):
            print("  ", end="")
        for j in range(1, 2*i-1 + 1):
            print("* ", end="")
        print()


triangle(9)
