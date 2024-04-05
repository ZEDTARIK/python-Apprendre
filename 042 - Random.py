from random import randint

wins = 0
losses = 0

for i in range(1, 4):
    x = randint(1, 6)
    if x == 2 or x == 6:
        print("You're winning!")
        wins += 1
    else:
        print("You're losing!")
        losses += 1

print(f"You won {wins} times and lost {losses} times.")