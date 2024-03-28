# This Python code is calculating the number of years it will take for Agatha's savings (`aga`) to
# surpass Mark's savings (`mar`).
ans = 0
mar = 1000000
aga = 500000

while True:
    mar = mar + 50000
    aga = aga + (aga*8/100)
    ans = ans + 1
    if aga > mar:
        break

print("les nomber d'anne(s) est", ans)