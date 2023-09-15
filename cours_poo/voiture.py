print("\n")

class Voiture:
    # attributs (variables d'une classe)

    # constructeur
    def __init__(self, couleur = "blanc", vitesse_bridage = 250):
        self.nb_roues = 4
        self._vitesse_max = 250
        self._vitesse_actuelle = 0
        self.couleur = couleur
        self.demarree = False
        self.brider(vitesse_bridage)
        self.klaxonner()
        
    def __str__(self):
        return f"Une voiture {self.couleur} pouvant rouler à {self._vitesse_max}km/h"
    
    def get_vitesse_max(self):
        # contrôle
        return self._vitesse_max
    
    def set_vitesse_max(self, nouvelle_vit_max):
        self.brider(nouvelle_vit_max)
    
    def demarrer(self):
        # if self.demarree == False:
        if not self.demarree:
            print("Démarrage de la voiture...")
            self.demarree = True
    
    def klaxonner(self):
        print("Tut tut")
    
    def rouler(self, vitesse_cible):
        if not self.demarree:
            print("Vous ne pouvez rouler")
            return
        
        # Lorsque la voiture roule elle affiche une vitesse incrémentée de 1km/h à partir de la vitesse courante jusqu'à la vitesse cible !
        
        if (vitesse_cible > self._vitesse_max):
            vitesse_cible = self._vitesse_max
            
        # while (self._vitesse_actuelle < vitesse_cible):
        #     print(f"Accélaration à {self._vitesse_actuelle}")
        #     self._vitesse_actuelle += 1
        for i in range(self._vitesse_actuelle, vitesse_cible + 1, 1):
            self._vitesse_actuelle = i
            print(f"Accélération à {self._vitesse_actuelle}km/h")
            
    def brider(self, vitesse_bridage):
        if (vitesse_bridage < self._vitesse_max):
            self._vitesse_max = vitesse_bridage

ma_voiture = Voiture("rouge", 500)
# print(ma_voiture)

ta_voiture = Voiture("bleue", 220)
# print(ta_voiture)

une_voiture = Voiture()
# print(une_voiture)

# nouvelle legislation : 220 km/h max

# ma_voiture.brider(220)
# ta_voiture.brider(220)
# une_voiture.brider(320)

# print(ma_voiture)
# print(ta_voiture)
# print(une_voiture)

ma_voiture.demarrer()
ma_voiture.rouler(200)

ta_voiture.demarrer()
ta_voiture._vitesse_max = 10000
ta_voiture.set_vitesse_max(10000)