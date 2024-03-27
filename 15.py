# This Python code snippet is a simple program that determines whether a person should pay taxes based
# on their age and gender.
Age = int(input("Entre vote Age : "))
Sexe =input("Entre votre Sexe (M/F) : ")

Regle1= Sexe == 'M' and Age >20
Regle2= Sexe == 'F' and (Age >= 18 and Age < 36)

if Regle1 or Regle2 :
    print("Vous devez payer les impôts")
else : 
    print("Ne pas payes les impôts")