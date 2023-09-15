print("\n")

class Voiture:
    # attributs (variables d'une classe)

    # constructeur
    def __init__(self, couleur = "blanc", vitesse_bridage = 250):
        self.nb_roues = 4
        self.vitesse_max = 250
        self.vitesse_courante = 0
        self.couleur = couleur
        self.brider(vitesse_bridage)
        self.klaxonner()
        
    def __str__(self):
        return f"Une voiture {self.couleur} pouvant rouler à {self.vitesse_max}km/h"
    
    def klaxonner(self):
        print("Tut tut")
    
    def rouler(self, vitesse_cible):
        # Une voiture ne peut rouler que si elle est démarrée
            # Une voiture peut démarrer et s'arrêter
            # Une voiture ne peut s'arrêter que si elle est à 0 km/h
        
        # Lorsque la voiture roule elle affiche une vitesse incrémentée de 1km/h à partir de la vitesse courante jusqu'à la vitesse cible !
        
        if (vitesse_cible <= self.vitesse_max):
            self.vitesse_courante = vitesse_cible
        else:
            self.vitesse_courante = self.vitesse_max
            
    def brider(self, vitesse_bridage):
        if (vitesse_bridage < self.vitesse_max):
            self.vitesse_max = vitesse_bridage

ma_voiture = Voiture("rouge", 500)
print(ma_voiture)
# ma_voiture.klaxonner()

ta_voiture = Voiture("bleue", 220)
print(ta_voiture)
# ta_voiture.klaxonner()

une_voiture = Voiture()
print(une_voiture)

# nouvelle legislation : 220 km/h max

ma_voiture.brider(220)
ta_voiture.brider(220)
une_voiture.brider(320)

print(ma_voiture)
print(ta_voiture)
print(une_voiture)