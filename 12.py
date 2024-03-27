# This Python code calculates the total cost of photocopies based on the number of copies made. Here's
# a breakdown of how it works:
N=int(input("Entre le nombre de photocopies: "))

if N < 10 :
    F = N * 0.3
elif N < 30 :
    F = 10 * 0.3 + (N-10) * 0.25
else :
    F = 10 *0.3 + 20*0.25 + (N-30)*0.2

print("Le montant de facture à payer est : ", format(F, ".2f"), "Dh")

