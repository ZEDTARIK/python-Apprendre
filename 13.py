# This Python code snippet prompts the user to enter an age for voting eligibility. Depending on the
# age entered, it will output a corresponding category. Here are the categories based on the age
# ranges:
Age= int(input("Enter vote Age: "))

if Age >= 6 and Age <=7 :
    print("Pussin")
elif Age >= 8 and Age <=9 :
    print("Pupille")
elif Age >= 10 and Age <=11 :
    print("Minime")
elif Age >= 12 and Age <=16 :
    print("Cadet")
else :
    print("La catégorie n'existe pas")
    

