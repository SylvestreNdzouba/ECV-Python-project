print("\n")

import random

class Dice:
    
    def __init__(self, faces):
        self._faces = faces
    
    def roll(self):
        return random.randint(1, self._faces)
    
    def __str__(self):
        return f"I'm a dice with {self._faces} faces"
    
# Coder une classe RiggedDice
    # Hérite de la classe Dice
    # polymorphe la méthode roll()
    # roll() prend désormais un paramètre "rigged" (booléen)
    # Si rigged : alors on obtient tjrs le résultat max
    # Sinon : lancé de dès normal
        # Sans utiliser la méthode roll()
        # en une ligne
    
a_dice = Dice(6)
print(a_dice)

for i in range(0, 10):
    print(a_dice.roll())
    
a_rigged_dice = RiggedDice(20)
a_rigged_dice.roll() # résultat aléatoire
a_rigged_dice.roll(True) # 20