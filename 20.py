# This Python code snippet prompts the user to enter a character (alphabetical letter, number, or
# special character) and then determines the type of the entered character.
C=input("Entre votre alphabetique , nombre  ou caractere special : ")

if ("a" <= C and "z" >= C) or ("A" <= C and "Z" >= C) :
    print(C, " est alphabet")
elif ("0" <= C and "9" >= C) :
    print(C, " est un nombre")
else :
    print(C, " est un caractere")