nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
s=0
for i in range (0,nombreEtudiants):
  while True:
     note=float(input(f"Note Etudiant {i+1} : "))
     if 0<= note<=20:
        break
     else:
         print("Note non conventionelle")
  notes.append(note)
  s=note+1
moyenne=s/nombreEtudiants
moyenne=float(moyenne)
print(f"Moyenne de la classe: {moyenne}")
print("Numéro de l'Etudiant | note | ecart de la moyenne")
for i, note in enumerate(notes):
    ecart= note -moyenne
    print(f"{i} | {note} | {ecart} ")


