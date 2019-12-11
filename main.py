import mage
import warrior
import healer
import rogue
from random import randint
class Main:
    def __init__(self):
        self.player_class = ""
        self.blair_class = ""
    def run():
        print("Welcome to Tyler's Role Playing Adventure!")
        print("The goal of this game is to provide myself with constant practise in Python and to continue to innovate this game as my skill grows.")
        print("I will also be attempting to re-write this game in Java and JavaScript to further strengthen my skills in those languages as well.")
        print("The game will begin shortly, have fun!")
        pick_a_class()
        start_adventure()
    def pick_a_class(self):
        print("Choose your class from the following options: ")
        print("1. Mage")
        print("2. Warrior")
        print("3. Healer")
        print("4. Rogue")
        player_class_choice = input("Enter the number that corresponds to class you wish to choose")
        blair_class_choice = randint(1,4)
        #while player_class_choice == "1" or player_class_choice == "2" or player_class_choice == "3" or player_class_choice == "4":
        if player_class_choice == "1":
            print("You have chosen to be a Mage!")
            mage.Mage.build_mage()
            self.player_class = print("Mage")
        if player_class_choice == "2":
            print("You have chosen to be a Warrior!")
            warrior.Warrior.build_warrior()
            player_class = "Warrior"
        if player_class_choice == "3":
            print("You have chosen to be a Healer!")
            healer.Healer.build_healer()
            player_class = "Healer"
        if player_class_choice == "4":
            print("You have chosen to be a Rogue!")
            rogue.Rogue.build_rogue()
            player_class = "Rogue"
        if blair_class_choice == 1:
            mage.Mage.build_mage()
            blair_class = "Mage"
        if blair_class_choice == 2:
            warrior.Warrior.build_warrior()
            blair_class = "Warrior"
        if blair_class_choice == 3:
            healer.Healer.build_healer()
            blair_class = "Healer"
        if blair_class_choice == 4:
            rogue.Rogue.build_rogue()
            blair_class = "Rogue"
    def start_adventure(self):
        print("Hello Adventurer! Your tale beings in the small town of Tylersville where you have lived your entire life")
        print("You have studied the ways of your class and are ready to embark on your first adventure")
        print("Your lifelong friend Blair will be joining you on your adventure")
        print("Your class is: ")
        self.player_class
###########################
run()