L = int(input("entre la valuer de L : "))

for i in range(1, L+1):
    for j in range(1, L-i+1):
        print("  ", end="")
    for k in range(1, 2*i-1+1):
        if k ==1 or  k== 2*i-1 or i ==L :
            print("* ", end="")
        else: 
            print("  ", end="")
    print()