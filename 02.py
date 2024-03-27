# This Python code calculates the perimeter and area of a rectangle based on user input for the width
# and length of the rectangle. Here's a breakdown of what each part of the code does:
largeur = float(input("Taper la largeur d'un rectangle : "))
longeur = float(input("Longeur d'un rectangle : "))
Perimetre = (largeur + longeur) / 2 
Surface = largeur * longeur
print("================================")

print("Le perimetre d'un rectangle est de : ", format(Perimetre, ".2f"))
print("La Surface d'un rectangle est de : ", format(Surface, ".2f"))