# Functions to randomly populate playing field

import random
distribution = ["horizontal", "vertical"]
up_down = ["up", "down"]
left_right = ["left", "right"]
def select_random_field(selection):
    return random.choice(selection)
def select_random_distribution():
    return random.choice(distribution)
def select_random_up_down():
    return random.choice(up_down)
def select_random_left_right():
    return random.choice(left_right)
def select_random_left_amazing method():
    return random.choice(left_right)

# Playing field class

class Playfield:

    # Create an instance of a playing field
    def __init__(self):
        self.empty = """
         ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
        |    |    |    |    |    |    |    |    |    |    |
        | A0 | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | B0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | E9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | F0 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | H0 | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | I0 | I1 | I2 | I3 | I4 | I5 | I6 | I7 | I8 | I9 |
        |____|____|____|____|____|____|____|____|____|____|
        |    |    |    |    |    |    |    |    |    |    |
        | J0 | J1 | J2 | J3 | J4 | J5 | J6 | J7 | J8 | J9 |
        |____|____|____|____|____|____|____|____|____|____|
        """

        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.columns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.fields = [self.rows[i] + column for i in range(10) for column in self.columns]
    
    # Populate the playing fiels: returns a list of occupied fields as well as a list containing all the placed ships
    def populate(self, ship_list):
        available_fields = self.fields.copy()
        occupied_fields = []
        for ship in ship_list:
            while ship.is_occupied(available_fields):
                ship.place(self.fields)
            occupied_fields += ship.fields
            ship.remove(available_fields)
        return occupied_fields, ship_list
    
    # Update the appearance (output to the terminal) of the playing field after each player move
    def update(self, hit_list, miss_list):
        update = self.empty
        for field in hit_list:
            update = update.replace(" " + field + " ", "OOOO")
        for field in miss_list:
            update = update.replace(" " + field + " ", "~~~~")
        return update

    # Update the appearance of the playing field to show where the ships are located
    def solution(self, occupied_fields):
        solution = self.empty
        for field in self.fields:
            if field in occupied_fields:
                solution = solution.replace(" " + field + " ", "OOOO")
            else:
                solution = solution.replace(" " + field + " ", "~~~~")
        return solution


# Ship class
class Ship:
    
    # Create an instance of a ship in the form of a list containing the pre-defined number of fields
    def __init__(self, size):
        self.size = size
        self.fields = []
        for i in range(size):
            self.fields.append("")
    
    # Place the ship on the playing field randomly
    def place(self, playing_fields):
        self.playing_fields = playing_fields
        self.fields[0] = select_random_field(playing_fields)
        if self.size > 1:     
            index_counter = playing_fields.index(self.fields[0])
            dist = select_random_distribution()
            if dist == "horizontal":
                if str(self.size-2) in self.fields[0] or str(self.size-3) in self.fields[0] or str(self.size-4) in self.fields[0]:
                    dir = "right"
                elif str(11-self.size) in self.fields[0] or str(12-self.size) in self.fields[0] or str(13-self.size) in self.fields[0]:
                    dir = "left"
                else:
                    dir = select_random_left_right()
                for i in range(self.size-1):
                    if dir == "right":
                        index_counter += 1
                        self.fields[i+1] = playing_fields[index_counter]
                    else:
                        index_counter -=1
                        self.fields[i+1] = playing_fields[index_counter]
            else:
                if index_counter < (self.size-1)*10:
                    dir = "down"
                elif index_counter > (len(playing_fields)-1) - (self.size-1)*10:
                    dir = "up"
                else:
                    dir = select_random_up_down()
                for i in range(self.size-1):
                    if dir == "down":
                        index_counter += 10
                        self.fields[i+1] = playing_fields[index_counter]
                    else:
                        index_counter -=10
                        self.fields[i+1] = playing_fields[index_counter]
        return self.fields
    
    # Remove the fields occupied by the ship and surrounded no longer choosable fields from the list of available fields
    def remove(self, from_fields):
        fields_to_be_removed = []
        available_fields = Playfield().fields
        for i in range(self.size):
            idx = available_fields.index(self.fields[i])
            if self.fields[i] == "A0":
                fields_to_be_removed += [available_fields[idx], available_fields[idx+1], available_fields[idx+10], available_fields[idx+11]]
            elif self.fields[i] == "J9":
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-10], available_fields[idx-11]]
            elif "A" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx+1], available_fields[idx+9], available_fields[idx+10], available_fields[idx+11]]
            elif "J" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-9], available_fields[idx-10], available_fields[idx-11], available_fields[idx+1]]
            elif "0" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-9], available_fields[idx-10], available_fields[idx+1], available_fields[idx+10], available_fields[idx+11]]
            elif "9" in self.fields[i]:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-10], available_fields[idx-11], available_fields[idx+9], available_fields[idx+10]]
            else:
                fields_to_be_removed += [available_fields[idx], available_fields[idx-1], available_fields[idx-9], available_fields[idx-10], available_fields[idx-11], available_fields[idx+1], available_fields[idx+9], available_fields[idx+10], available_fields[idx+11]]
        for field in fields_to_be_removed:
            if field in from_fields:
                from_fields.pop(from_fields.index(field))
        return from_fields

    # Check if the fields selected for the ship are already occupied
    def is_occupied(self, available_fields):
        return any(field not in available_fields for field in self.fields)

# Intro

welcome_msg = "\nWelcome to the Ultimate Battleship Experience\n"

print(welcome_msg)
input("Press ENTER to start")
player1 = input("\nWho dares to enter the battle? Immediately state your name!\n> ")
while player1 == "":
    player1 = input("\nI didn't get that. Please, state your name.\n> ")
else:
    print(f"\nOk then, {player1}, let's begin.\n")

rules = """ 
I will hide 10 ships. Together they occupy a total of 20 fields.
The ships can be distributed horizontally or vertically, but not diagonally.
None of the ships touches another (not even diagonally).
The ships contain 1 carrier (4 fields), 2 battleships (3 fields), 3 carriers (2 fields) and 4 destroyers (1 field).
I will let you know, once you have sunk a particular ship.
Depending on the difficulty level you will have 80, 70, 60 or 50 missiles in total. If you manage to sink all my ships, YOU WIN.
Else, I WIN.
"""

answer_rules = input(f"\nFirst things first. Are you familiar with the rules, {player1}? (y/n)\n> ").lower()
while answer_rules != "y" and answer_rules != "n":
    answer_rules = input("\nCome again? Please enter y for yes or n for no.\n> ").lower()
else:
    if answer_rules == "y":
        print("\nLooks like we are good to go.")    
    else:
        print(rules)
        
# Game

def battleship_game(play_count=0, won_count=0, lost_count=0):
    
    # Set up playing field and create empty fleet of ships

    playing_field = Playfield()
    playing_fields = playing_field.fields

    car = Ship(4)
    bat_1 = Ship(3)
    bat_2 = Ship(3)
    cru_1 = Ship(2)
    cru_2 = Ship(2)
    cru_3 = Ship(2)
    des_1 = Ship(1)
    des_2 = Ship(1)
    des_3 = Ship(1)
    des_4 = Ship(1)

    empty_fleet = [car, bat_1, bat_2, cru_1, cru_2, cru_3, des_1, des_2, des_3, des_4]

    # Populate playing field and determine position of ships

    occupied_fields, fleet = playing_field.populate(empty_fleet)

    carrier = fleet[0].fields
    battleship_1 = fleet[1].fields
    battleship_2 = fleet[2].fields
    battleships = battleship_1 + battleship_2
    cruiser_1 = fleet[3].fields
    cruiser_2 = fleet[4].fields
    cruiser_3 = fleet[5].fields
    cruisers = cruiser_1 + cruiser_2 + cruiser_3
    destroyers = fleet[6].fields + fleet[7].fields + fleet[8].fields + fleet[9].fields

    hit_list = []
    miss_list = []
    total_missiles = 0
    total_hits = 0
    num_missiles = 0
    
    # Main body of the game

    difficulty_levels = ["1", "2", "3", "4"]
    selection = input("\nLet's see. How difficult shall I make it for you?\nEasy (1), Medium (2), Hard (3) or Extreme (4)?\n> ")
    while selection not in difficulty_levels:
        selection = input("\nWho's supposed to decipher that??? Please, type 1 for Easy, 2 for Medium, 3 for Hard or 4 for Extreme.\n> ")
    else:
        difficulty = int(selection)
    if difficulty == 1:
        print(f"\nWise decision, {player1}. Take it slow in the beginning.")
        num_missiles = 80
    if difficulty == 2:
        print(f"\nMedium, ey, {player1}? Let's see if your skills are a match for me.")
        num_missiles = 70
    if difficulty == 3:
        print(f"\nI wanna see you try, {player1}!")
        num_missiles = 60
    if difficulty == 4:
        print(f"\nHahaha! You stand no chance, {player1}!")
        num_missiles = 50

    input("\nPress ENTER so that I can set up our playing field.")
    print("\nLet the battle begin!\n")
    print(playing_field.empty)
    print("\nI have hidden my ships well.\nIf at any point during the game you would like to review the rules, enter '?'.\nOtherwise give me your first target.")

    # Get player input, check it against game conditionals and give appropriate feedback to player
    
    for i in range(num_missiles):
        target = input("> ").upper()
        outcome = ""
        message = ""
        if target == "?":
            outcome = "RULES"
            message = rules
            total_missiles -= 1
        elif target in hit_list or target in miss_list:
            outcome = "I CAN'T BELIEVE IT"
            message = "You're wasting ammunition. You already hit this target."
        elif target not in playing_fields:
            outcome = "PATHETIC"
            message = "You are way outside the target area. Try again."
        elif target in occupied_fields:
            outcome = "HIT"
            hit_list.append(target)
            total_hits += 1
        else:
            outcome = "MISS"
            miss_list.append(target)
        total_missiles +=1
        print(f"\n*** {outcome} ***")
        if outcome == "HIT":
            if target in destroyers:
                print("\n*** SHIP SUNK ***")
                print("You have sunk one of my destroyers.")
                if all(field in hit_list for field in destroyers):
                    print("All destroyers down.")
            elif target in cruiser_1:
                if all(field in hit_list for field in cruiser_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif target in cruiser_2:
                if all(field in hit_list for field in cruiser_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif target in cruiser_3:
                if all(field in hit_list for field in cruiser_3):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif target in battleship_1:
                if all(field in hit_list for field in battleship_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my battleships.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            elif target in battleship_2:
                if all(field in hit_list for field in battleship_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my battleships.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            else:
                if all(field in hit_list for field in carrier):
                    print("*** SHIP SUNK ***")
                    print("You have sunk my carrier.")
        else:
            print(message)        
        print(playing_field.update(hit_list, miss_list))

        if total_hits == 0:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles didn't hit my ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles didn't hit my ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles didn't hit my ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits == 1:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit my ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits == 2:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit my ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits == 19:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.\n")
                print("Give me your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.\n")
                print("Give me your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits < 20:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            elif total_missiles == num_missiles-1:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missile left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                print("Give me your next target.")
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(num_missiles-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.\n")
                if total_missiles == num_missiles:
                    continue
                else:
                    print("Give me your next target.")
        else:
            break

    if total_hits == 20:
        won_count += 1
        print("\n*****   YOU WIN   *****\n\nCongratulations! It took " + str(total_missiles) + " missiles to take all my ships down. \nWell done, " + player1 + "!")
    else:
        lost_count +=1
        print("\n*****   YOU LOSE   *****\n\nSorry, " + player1 + ". You didn't manage to destroy all my ships with the number of missiles at your disposal.")
        print("Here is the solution:")
        print(playing_field.solution(occupied_fields))
        print("You managed to hit " + str(total_hits) + " targets. Here is the complete list: " + str(hit_list))
    play_count += 1
    print(f"\nGames played: {play_count}\nGames won: {won_count}\nGames lost: {lost_count}")
    
    # Define a loop for playing the game again
    
    answer = input("\nWanna play another round? (y/n)\n> ").lower()
    if answer == "y":
        print(f"Ok, {player1}. Here we go.")
        battleship_game(play_count, won_count, lost_count)
    else:
        print(f"It was nice playing with you, {player1}! CU next time.")  

battleship_game()        
