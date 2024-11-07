taille=int(input("Quelle est la taille de votre vecteur:  "))
v1=[]
v2=[]
s=0
x=0
print("Saisie du premier vecteur")
for i in range (taille):
    val=float(input(f" v1[{i+1}] : "))
    v1.append(val)
print("Saisie du second vecteur")
for i in range (taille):
    var=float(input(f" v2[{i+1}] : "))
    v2.append(var)
print(v1,v2)


for i in range(taille):
    x=v1[i]*v2[i]
    s=s+x
print(f"Le produit scalaire de v1 et v2 est {s}")
