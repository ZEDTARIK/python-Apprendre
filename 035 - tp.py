gues = ""
secret_key = "123"
gues_limit = 3
gues_count = 0
out_of_gues = False

while gues != secret_key :
    if gues_count < gues_limit and not out_of_gues : 
        gues = input("Enter the value :")
        gues_count += 1
    else :
        out_of_gues = True
        break

if out_of_gues :
    print("you're lose out of guesses")
else :
    print("you're winning")