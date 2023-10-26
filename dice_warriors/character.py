from __future__ import annotations
from dice import Dice, RiggedDice
from panel import panneau_jeu
import threading
from rich import print
import time
import pygame

# Initialisation de Pygame
pygame.mixer.init()

# Chargez le son
soundFight = pygame.mixer.Sound('1-01.-Opening.wav')
soundArmure = pygame.mixer.Sound('SF-coup_armure_3.wav')

largeur, hauteur = 800, 600

print("\n")


class Character:
    _label = "Character"

    def __init__(self, name, max_health, attack, defense, dice):
        self._name = name
        self._max_health = max_health
        self._health = self._max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice : Dice = dice

    def __str__(self):
        return f"{type(self)._label} {self._name} is starting the fight with {self._health}/{self._max_health}hp ({self._attack_value}atk / {self._defense_value}def)"

    def is_alive(self):
        return self._health > 0
        # return bool(self._health)

    def show_healthbar(self):
        missing_hp = self._max_health - self._health
        print(
            f"[{'❤️' * self._health}{' ' * missing_hp}] {self._health}/{self._max_health}hp"
        )

    def decrease_health(self, amount):
        if self._health - amount < 0:
            amount = self._health
        self._health = self._health - amount
        self.show_healthbar()

    def compute_damages(self, roll):
        return self._attack_value + roll
    
    def get_name(self):
        return self._name

    def attack(self, target):
        if self.is_alive():
            roll = self._dice.roll()
            damages = self.compute_damages(roll)
            print(
                f"⚔️  {type(self)._label}  {self._name} [red]attack[/red] {target.get_name()} with {damages} damages ! (attack: {self._attack_value} + roll: {roll})"
            )
            #time.sleep(2)
            target.defense(damages)

    def compute_defense(self, damages, roll):
        return damages - self._defense_value - roll
    
    def defense(self, damages):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll)
        print(
            f"🛡️  {type(self)._label} {self._name} defend against {damages} damages and take {wounds} wounds ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})"
        )
        soundArmure.play()

        time.sleep(2)
        self.decrease_health(wounds)


class Warrior(Character):
    _label = "Warrior"
    
    def compute_damages(self, roll):
        print(f"🪓 Axe in face ! (bonus: +3)")
        return super().compute_damages(roll) + 3


class Mage(Character):
    _label = "Mage"

    def compute_defense(self, damages, roll):
        print(f"🔮 Magic armor ! (bonus: -3)")
        return super().compute_defense(damages, roll) - 3


class Thief(Character):
    _label = "Thief"
    

if __name__ == "__main__":
    panneau_thread = threading.Thread(target=panneau_jeu)

    panneau_thread.start()

    soundFight.play()
    char_1 = Warrior("James", 20, 8, 3, Dice(6))
    char_2 = Mage("Dina", 20, 8, 3, Dice(6))

    print(char_1)
    print(char_2)

    while char_1.is_alive() and char_2.is_alive():
        char_1.attack(char_2)
        char_2.attack(char_1)
    soundFight.stop()

    panneau_thread.join()

