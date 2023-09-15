# if

int
float
str
bool # True / False

# opérateurs booléens

# and
# or 
# not

if (True):
    pass

if (False):
    pass
else:
    pass

if (False):
    pass
elif (False):
    pass
elif (False):
    pass
else:
    pass

# algo SNCF
age = int(input("Quel est votre age ?"))

# ==
# <=
# >=
# <
# >
# !=

if (age > 0) and (age < 18):
    print("Statut enfant")
elif (age >= 18) and (age < 70):
    print("Statut adulte")
elif (age >= 70):
    print("Statut sénior")
    
note = -1
absence = False
triche = True

# not

if (absence == True) or (triche == True):
    note = 0
else:
    note = int(input("Saisir la note de l'élève: "))
    
if (note >= 0) and (note <= 20):
    print(f"Note finale: {note}")
else:
    print("Erreur système")