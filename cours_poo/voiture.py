print("\n")

class Voiture:
    # attributs (variables d'une classe)

    # constructeur
    def __init__(self, couleur = "blanc"):
        self.nb_roues = 4
        self.vitesse_max = 250
        self.couleur = couleur
        
    def __str__(self):
        return f"Une voiture {self.couleur} pouvant rouler à {self.vitesse_max}km/h"
    
    def klaxonner(self):
        print("Tut tut")
        
    # méthodes (fonctions de la classe)

ma_voiture = Voiture("rouge")
print(ma_voiture)
ma_voiture.klaxonner()

ta_voiture = Voiture("bleue")
print(ta_voiture)
ta_voiture.klaxonner()

une_voiture = Voiture()
print(une_voiture)
une_voiture.klaxonner()