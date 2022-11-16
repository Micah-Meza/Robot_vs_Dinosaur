# (10 points): As a developer, I want a Robot to have 
# a name, health, and active_weapon.

# (10 points): As a developer, I want a Robot to have the 
# ability to attack a Dinosaur on a Battlefield. This attack 
# method should lower the Dinosaur’s health by the attack_power 
# of the Robot’s active_weapon.

from weapon import Weapon
import random

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 800
        self.active_weapon = Weapon("Light Saber",random.randint(50,90) )


    def robot_attack(self, dinosaur):
        dinosaur_life = dinosaur.health - self.active_weapon.attack_power
        dinosaur.health = dinosaur_life
        if dinosaur_life < 0:
            dinosaur.health = 0
            dinosaur_life = dinosaur.health
        print(f"{self.name} attacks {dinosaur.name} with a {self.active_weapon.name} causing {self.active_weapon.attack_power} damage!")
        print(f"{dinosaur.name} health is now {dinosaur_life}!")
        print()
        
        
        





