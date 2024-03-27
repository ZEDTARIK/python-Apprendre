# This Python code is checking if a given year is a leap year or not.
annee = int(input("Saisir une année: "))

if (((annee % 4 == 0) and (annee % 100  != 0)) or (annee % 400 == 0)) :
    print(annee, "est une année bissextile")
else : 
    print(annee, "n'est pas une année bissextile")