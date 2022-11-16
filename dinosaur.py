# (10 points): As a developer, I want a Dinosaur to 
# have a name, health, and attack power.

# (10 points): As a developer, I want a Dinosaur to have 
# the ability to attack a Robot on a Battlefield. This 
# attack method should lower a Robot’s health by the value 
# of the Dinosaur’s attack_power.

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 800
        self.attack_power = attack_power

    def dinosaur_attack(self, robot):
        robot_life = robot.health - self.attack_power
        robot.health = robot_life
        if robot_life < 0:
            robot.health = 0
            robot_life = robot.health
        print(f"{self.name} attacks {robot.name} causing {self.attack_power} damage!")
        print(f"{robot.name} health is now {robot_life}!")
        print()
        
