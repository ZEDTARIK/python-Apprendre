c=input("Saisir ec que vous voulez : ")

if ("a" <= c and c <= "z") or ("A"<= c and c <= "Z") :
    print(c, " c'est une Alphabet")
elif ("0" <= c and c <= "9") :
    print(c, " c'est un Nombre")
else :
    print(c, " c'est un caracteres")
