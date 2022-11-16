from dinosaur import Dinosaur
from robot import Robot
import random

class Battlefield:

    def __init__(self):
        self.robot_1 = Robot("Bender")
        self.dinosaur_1 = Dinosaur("Rex", random.randrange(30,100))


    def run_game(self):
        pass


    def display_welcome(self):
        print("Welcome to Robots Vs Dinosaurs. Where only one can win and the other destroyed! ")

    
    def battle_phase(self):
        battle = True
        while battle != False:
            
            if self.robot_1.health == 0:
                self.display_winner()
                battle = False
                break
            elif self.robot_1.health != 0:
                self.robot_1.robot_attack(self.dinosaur_1)
                battle = True
            
            if self.dinosaur_1.health == 0:
                self.display_winner()
                battle = False
                break
            elif self.dinosaur_1.health != 0:
                self.dinosaur_1.dinosaur_attack(self.robot_1)
                battle == True

    def display_winner(self):
        
        if self.robot_1.health == 0:
            print(f"{self.dinosaur_1.name} wins the war! ")
        elif self.dinosaur_1.health == 0:
            print(f"{self.robot_1.name} wins the war! ")







