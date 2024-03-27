# This Python code calculates the Euclidean distance between two points in a 2D plane.
import math

Xa=float(input("Enter the Xa : "))
Xb=float(input("Enter the Xb : "))
Ya=float(input("Enter the Ya : "))
Yb=float(input("Enter the Yb : "))

AB= (Xb-Xa)**2 + (Yb-Ya)**2
AB=math.sqrt(AB)

print("La distance between Xa and Ya is ", format(AB, ".2f"))
