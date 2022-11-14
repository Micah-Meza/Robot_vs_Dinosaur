# (10 points): As a developer, I want a Weapon to have 
# a name and attack_power.

# (5 points): As a developer, I want to choose from a List of 
# 3 possible weapons before a robot makes an attack.


class Weapon:

    def __init__(self, name, attack_power):  
        self.name = name
        self.attack_power = attack_power


    def weapon_choice(self):
        weapon_choice = ["Light Saber", "Atom Bomb", "Machine Gun"]
