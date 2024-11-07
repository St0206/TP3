nbr=int(input("Entrez le nombre "))
query=int(input("Tapez 1 pour la boucle for et 2 pour la boucle while: "))
fact=1
t=1
if query==1:
        for i in range (nbr,1,-1):
                fact=fact*i
                print(fact)
        factorielle=fact
        print(f"le factorielle de {nbr} est {factorielle}")
elif query==2:
        while t!=nbr:
                t=t+1
                fact=fact*t
                print(fact)
        factorielle=fact
        print(f"le factorielle de {nbr} est {factorielle}")
else:
        print("Vous auriez du entrez un chiffre entre 1 et 2")  