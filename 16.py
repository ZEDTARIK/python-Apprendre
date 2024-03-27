# This Python code calculates the total price including tax based on the price before tax (`PHT`) and
# the category (`C`) provided by the user.
PHT= float(input("Entre votre prx hort taxe: "))
C= input("Entre votre categorie (A , B ou C): ")

if C == 'A' :
    PTTC = (PHT+PHT)*0.07
elif C == 'B' :
    PTTC = (PHT+PHT)* 0.2
elif C == 'C' :
    PTTC = (PHT+PHT)* 0.25
else :
    print("Categorie n'existe pas")

print("Total TTC de produit est : ", format(PTTC, ".2f"))
