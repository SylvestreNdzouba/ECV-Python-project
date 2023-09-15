from dice import Dice, RiggedDice
print("\n")


class Character:

    _label = "Character"

    def __init__(self, name, max_health, attack, defense, dice):
        self._name = name
        self._max_health = max_health
        self._health = self._max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice

    def __str__(self):
        return f"{type(self)._label} {self._name} is starting the fight with {self._health}/{self._max_health}hp ({self._attack_value}atk / {self._defense_value}def)"

    def is_alive(self):
        return (self._health > 0)
        # return bool(self._health)

    def show_healthbar(self):
        missing_hp = self._max_health - self._health
        print(
            f"[{'●' * self._health}{' ' * missing_hp}] {self._health}/{self._max_health}hp")

    def decrease_health(self, amount):
        if (self._health - amount < 0):
            amount = self._health
        self._health = self._health - amount
        self.show_healthbar()

    def attack(self, target):
        if (self.is_alive()):
            damages = self._attack_value + self._dice.roll()
            print(
                f"⚔️ {type(self)._label}  {self._name} attack with {damages} damages !")
            target.defense(damages)

    def defense(self, damages):
        wounds = damages - self._defense_value - self._dice.roll()
        print(
            f"🛡️ {type(self)._label} {self._name} defend against {damages} damages and take {wounds} wounds !")
        self.decrease_health(wounds)


class Warrior(Character):
    _label = "Warrior"


class Mage(Character):
    _label = "Mage"


class Thief(Character):
    _label = "Thief"


if __name__ == "__main__":
    char_1 = Warrior("James", 20, 8, 3, Dice(6))
    char_2 = Thief("Dina", 20, 8, 3, Dice(6))

    print(char_1)
    print(char_2)

    while (char_1.is_alive() and char_2.is_alive()):
        char_1.attack(char_2)
        char_2.attack(char_1)
