# (10 points): As a developer, I want a Robot to have 
# a name, health, and active_weapon.

# (10 points): As a developer, I want a Robot to have the 
# ability to attack a Dinosaur on a Battlefield. This attack 
# method should lower the Dinosaur’s health by the attack_power 
# of the Robot’s active_weapon.

from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 800
        self.active_weapon = Weapon()


    def attack(self, dinosaur):
        pass
        





