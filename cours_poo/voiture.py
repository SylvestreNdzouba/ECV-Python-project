print("\n")

class Voiture:
    # attributs (variables d'une classe)

    # constructeur
    def __init__(self, couleur = "blanc", vitesse_bridage = 250):
        self.nb_roues = 4
        if (vitesse_bridage > 250):
            vitesse_bridage = 250
        self.vitesse_max = vitesse_bridage
        self.vitesse_courante = 0
        self.couleur = couleur
        self.klaxonner()
        
    def __str__(self):
        return f"Une voiture {self.couleur} pouvant rouler à {self.vitesse_max}km/h"
    
    def klaxonner(self):
        print("Tut tut")
    
    def rouler(self, vitesse_cible):
        if (vitesse_cible <= self.vitesse_max):
            self.vitesse_courante = vitesse_cible
        else:
            self.vitesse_courante = self.vitesse_max
            
    # méthode "brider" qui bride la vitesse max de la voiture
    # la vitesse de bridage ne peut jamais dépasser la vitesse max actuelle
        # utiliser cette méthode dans le constructeur

ma_voiture = Voiture("rouge", 500)
print(ma_voiture)
# ma_voiture.klaxonner()

ta_voiture = Voiture("bleue", 220)
print(ta_voiture)
# ta_voiture.klaxonner()

une_voiture = Voiture()
print(une_voiture)
# une_voiture.klaxonner()

########