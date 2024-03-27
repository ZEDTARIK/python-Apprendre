# This Python code calculates the volume of a sphere based on the input radius provided by the user.
# Here's a breakdown of what the code does:
import math

Rayon = float(input("Saisir le rayon du sphere : "))
Volume = ( 4 * math.pi * ( Rayon**3 ) ) /3

print("Le volume de rayon dy+u sphere est de : ", format(Volume, ".2f"))