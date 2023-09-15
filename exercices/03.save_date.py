date = ['0', '1', '/', '0', '1', '/', '1', '9', '7', '0']

jour = "".join(date[:2])
mois = "".join(date[3:5])
annee = "".join(date[-4:])

print(jour, mois, annee, sep="/")

date = "01/01/1970"

jour = int(date[:2])
mois = int(date[3:5])
annee = int(date[-4:])

annee = annee

print(jour, mois, annee, sep="/")