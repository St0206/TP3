A=0
B=0
C=0
for i in range (0,11):
    N = int(input("Entrez la valeur du nombre N"))
    while N <0 or N>20:
     N= int(input("Entrez une valeur entre 0 et 20"))
     if N < 10:
         A=A+1
     elif N>=10 and  N<15:
         B=B+1
     else:
         C=C+1

print(f"le nombre de valeur inférier a 10 est {A} \n le nombre de valeur entree  10 et 15 est {B}\n le nombre de valeur superieur a 15 est {C}")