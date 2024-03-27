# This Python code calculates the average of three input grades and then provides a corresponding
# evaluation based on the average. Here's a breakdown of what the code does:

print("Les notes entre 0 et 20 S'il vous plait : ")

N1= float(input("Entre la note 1: "))
N2= float(input("Entre la note 2: "))
N3= float(input("Entre la note 3: "))

M= (N1+N2+N3)/3
print("La moyenne de l'etudiant est : ", format(M, ".2f"))


if M >=17 : 
    print("trés Bien")
elif M >=15 and M < 17 : 
    print("Bien")
elif M >=13 and M < 15 :
    print("Assez Bien")
elif M >=10 and M < 13 : 
    print("Passable")
else : 
    print("Inssuffisant")