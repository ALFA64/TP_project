# Generate a random number between 1 and 100
# User need to guess if odd or even

import random
n = random.randint(1, 100)
print("Ghiceste numarul intre 1 si 100")
tip_numar = None

if n % 2 == 0:
    tip_numar = "par"
else:
    tip_numar = "impar"
        
while True:
    val = input("Numarul gandit este par sau impar? ")
    if val == tip_numar:
        print("Ai ghicit!")
        break
    else:
        print("Mai incearca!")

print(f"Numarul era {n}")
