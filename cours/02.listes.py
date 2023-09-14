eleves = ["Camille", "Thomas", "Luc", "Elsa", "Franck"]

print(eleves)

notes = [10.5, 18.0, 16.0, 20.0, 8.0]

print(notes)

dates = []

print(dates)

print(type(dates))

print(type(notes) == list)
print(type(notes) == int)

# Manipuler des listes

# longueur = len(notes)
# print(longueur)

print(len(eleves))

# LES INDICES DES LISTES COMMENCENT à 0

print(eleves[0])
print(eleves[len(eleves) - 1])
# equivalent
print(eleves[-1])

# Ajouter un élément (et plus si affinité)

eleves.append("Laetitia")
notes.append(14.5)

print(eleves)
print(notes)

# Slicing

jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]

print(jours[0:2])
print(jours[4:5])
print(jours[3:])
print(jours[:3])
print(jours[:])

weekend = jours[-3:]
print(weekend)

# Listes n-dimensions
jours_fr_en = [
    ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim'],
    ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
]

print(jours_fr_en[-2][-3])