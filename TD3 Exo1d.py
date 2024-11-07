s=0
x=0
nbr=int(input("Entrer le nombre "))
while s+x<=nbr:
    s=s+x
    x+=1
x-=1
print(f"Le nombre recherché est {x}")
