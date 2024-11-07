import random as rnd

nbr = rnd.randint(0, 100)
tentatives = 1
devine = int(input("Deviner le nombre "))
if devine < nbr:
    print("Un peu plus grand")
    tentatives += 1
else:
    print("Un peu plus petit")
    tentatives += 1
while devine != nbr:
    devine = int(input("Deviner le nombre "))
    if devine < nbr:
        print("Un peu plus grand")
        tentatives += 1
    else:
        print("Un peu plus petit")
        tentatives += 1

print("Vous avez gagné")
print(f"Le nombre de tentatives est de {tentatives} ")