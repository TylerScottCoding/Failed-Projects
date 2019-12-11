from random import randint
class Game:
    def start_adventure():
        print("Welcome to Tyler's Role Playing Adventure!")
        print("The goal of this game is to provide myself with constant practise in Python and to continue to innovate this game as my skill grows.")
        print("I will also be attempting to re-write this game in Java and JavaScript to further strengthen my skills in those languages as well.")
        print("The game will begin shortly, have fun!")
    def pick_a_class():
        def build_mage():
            max_hp = 200
            player_hp = 200
            player_dmg = 40
            max_mana = 300
            player_mana = 300
            xp = 0
            player_level = 1
            spell_dmg = player_dmg * player_level
            spell_mana = max_mana*.5
        def build_warrior():
            max_hp = 250
            player_hp = 250
            player_dmg = 20
            max_mana = 100
            player_mana = 100
            xp = 0
            player_level = 1
            spell_dmg = player_dmg * 2
            spell_mana = max_mana*.3
        def build_healer():
            max_hp = 100
            player_hp = 100
            player_dmg = 20
            max_mana = 200
            player_mana = 200
            xp = 0
            player_level = 1
            spell_heal = max_hp
            spell_mana = max_mana*.25
        def build_rogue():
            max_hp = 200
            player_hp = 200
            player_dmg = 35
            max_mana = 100
            player_mana = 100
            xp = 0
            player_level = 1
            spell_dmg = player_dmg * 2
            spell_mana = max_mana*.5
        def build_blair_class():
            blair_max_hp = 350
            blair_hp = 350
            blair_dmg = 25
            blair_max_mana = 150
            blair_player_mana = 150
            blair_xp = 0
            blair_level = 2
            blair_spell_dmg = player_dmg * 2
            blair_spell_mana = max_mana*.3
        print("Choose your class from the following options: ")
        print("1. Mage")
        print("2. Warrior")
        print("3. Healer")
        print("4. Rogue")
        player_class_choice = input("Enter the number that corresponds to class you wish to choose")
        blair_class = "Warrior"
        #while player_class_choice == "1" or player_class_choice == "2" or player_class_choice == "3" or player_class_choice == "4":
        if player_class_choice == "1":
            print("You have chosen to be a Mage!")
            build_mage()
        if player_class_choice == "2":
            print("You have chosen to be a Warrior!")
            build_warrior()
        if player_class_choice == "3":
            print("You have chosen to be a Healer!")
            build_healer()
        if player_class_choice == "4":
            print("You have chosen to be a Rogue!")
            build_rogue()
        print("Hello Adventurer! Your tale beings in the small town of Tylersville where you have lived your entire life.")
        print("You have studied the ways of your class and are ready to embark on your first adventure.")
        print("Your lifelong friend Blair will be joining you on your adventure.")
        print(f"Blair's class is: {blair_class}")
        
def main():
    s = Game
    s.start_adventure()
    s.pick_a_class()
main()