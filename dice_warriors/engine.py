from rich import print
import random
from dice import Dice
from character import Warrior, Mage, Thief

def main():
    warrior = Warrior("James", 20, 8, 3, Dice(6))
    mage = Mage("Dina", 20, 8, 3, Dice(6))
    thief = Thief("Lara", 20, 8, 3, Dice(6))

    cars = [warrior, mage, thief]
    stats = {}
    print(cars[0])

    car1 = random.choice(cars)
    cars.remove(car1)
    car2 = random.choice(cars)
    cars.remove(car2)

    print(car1)
    print(car2)

    for i in range(100):
        while (car1.is_alive() and car2.is_alive()):
            car1.attack(car2)
        if car2.is_alive():
            car2.attack(car1)



if __name__ == "__main__":
    main()