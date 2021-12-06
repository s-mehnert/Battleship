# create functions to randomly populate playing field

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

# Playing field class

class Playfield:
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

    # bug: doesn't update available fields properly when calling ship.remove()
    
    def populate(self, ship_list):
        available_fields = self.fields.copy()
        occupied_fields = []
        for ship in ship_list:
            while ship.is_occupied(available_fields):
                ship.place(self.fields)
            occupied_fields += ship.fields
            print(occupied_fields)
            ship.remove(available_fields)
            print(available_fields)
            print(len(available_fields))
        return occupied_fields, ship_list
    
    def update(self, hit_list, miss_list):
        update = self.empty
        for field in hit_list:
            update = update.replace(" " + field + " ", "OOOO")
        for field in miss_list:
            update = update.replace(" " + field + " ", "~~~~")
        return update

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
    
    # create an instance of a ship in the form of a list containing the pre-defined number of fields
    def __init__(self, size):
        self.size = size
        self.fields = []
        for i in range(size):
            self.fields.append("")
    
    # place the ship on the playing field randomly
    def place(self, playing_fields):
        self.playing_fields = playing_fields
        self.fields[0] = select_random_field(playing_fields)
        if self.size > 1:     
            index_counter = playing_fields.index(self.fields[0])
            dist = select_random_distribution()
            if dist == "horizontal":
                if str(self.size-2) in self.fields[0] or str(self.size-3) in self.fields[0] or str(self.size-4) in self.fields[0]:
                    dir = "right"
                elif str(self.size+3) in self.fields[0] or str(self.size+4) in self.fields[0] or str(self.size+5) in self.fields[0]:
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
    
    # remove the ship from the list of available fields

    # bug: doesn't remove all the fields it should

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
        print(from_fields)
        print(len(from_fields))
        return from_fields

    # check if the fields selected for the ship are already occupied
    def is_occupied(self, available_fields):
        for field in self.fields:
            return field not in available_fields

    # check if the ship has been sunk
    def is_sunk(self, hit_list):
        return all(field in hit_list for field in self.fields)

# Setting up playing field and other global parameters

playing_field = Playfield()
playing_fields = playing_field.fields

carrier = Ship(4)
battleship_1 = Ship(3)
battleship_2 = Ship(3)
cruiser_1 = Ship(2)
cruiser_2 = Ship(2)
cruiser_3 = Ship(2)
destroyer_1 = Ship(1)
destroyer_2 = Ship(1)
destroyer_3 = Ship(1)
destroyer_4 = Ship(1)

empty_fleet = [carrier, battleship_1, battleship_2, cruiser_1, cruiser_2, cruiser_3, destroyer_1, destroyer_2, destroyer_3, destroyer_4]

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
You will have 75 missiles in total. If you manage to sink all my ships, YOU WIN.
Else, I WIN.
"""

answer_rules = input(f"\nFirst things first. Are you familiar with the rules, {player1}? (y/n)\n> ").lower()
while answer_rules != "y" and answer_rules != "n":
    answer_rules = input("\nCome again? Please enter y for yes or n for no.\n> ").lower()
else:
    if answer_rules == "y":
        print("\nLooks like we are good to go.\n")    
    else:
        print(rules)
        
# Game

def battleship_game():
    input("\nPress ENTER so that I can set up our playing field.")
    print("\nLet the battle begin!\n")
    print(playing_field.empty)

    occupied_fields, fleet = playing_field.populate(empty_fleet)
    
    print(playing_field.solution(occupied_fields))

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
    
    print("\nI have hidden my ships well.\nIf at any point during the game you would like to review the rules, enter '?'.\nOtherwise give me your first target.")

    for i in range(75):
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
        print(f"Fleet contains {len(fleet)} ships.")
        print("Carrier:",carrier)
        print("Battleship 1:", battleship_1)
        print("Battleship 2:", battleship_2)
        print(battleships)
        print("Cruiser 1:", cruiser_1)
        print("Cruiser 2:", cruiser_2)
        print("Cruiser 3:", cruiser_3)
        print(cruisers)
        print(destroyers)

        if total_hits == 0:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles didn't hit my ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            elif total_missiles == 74:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missile left.")
                print("So far your missiles didn't hit my ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles didn't hit my ships.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
                if total_missiles == 75:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits == 1:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            elif total_missiles == 74:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missile left.")
                print("So far your missiles hit my ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships once.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
                if total_missiles == 75:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits == 2:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            elif total_missiles == 74:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missile left.")
                print("So far your missiles hit my ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships twice.")
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
                if total_missiles == 75:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits == 19:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.")
                print()
            elif total_missiles == 74:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missile left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.")
                print()
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hit needed to win this battle.")
                print()
                if total_missiles == 75:
                    continue
                else:
                    print("Give me your next target.")
        elif total_hits < 20:
            if total_missiles == 1:
                print("You have launched " + str(total_missiles) + " missile, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            elif total_missiles == 74:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missile left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
            else:
                print("You have launched " + str(total_missiles) + " missiles, " + str(75-total_missiles) + " missiles left.")
                print("So far your missiles hit my ships " + str(total_hits) + " times: " + str(hit_list))
                print(str(len(occupied_fields)-total_hits) + " more hits needed to win this battle.")
                print()
                if total_missiles == 75:
                    continue
                else:
                    print("Give me your next target.")
        else:
            break

    if total_hits == 20:
        print("\n*****   YOU WIN   *****\n\nCongratulations! It took " + str(total_missiles) + " missiles to take all my ships down. \nWell done, " + player1 + "!")
    else:
        print("\n*****   YOU LOSE   *****\n\nSorry, " + player1 + ". You didn't manage to destroy all my ships with the number of missiles at your disposal.")
        print("Here is the solution:")
        print(playing_field.solution(occupied_fields))
        print("You managed to hit " + str(total_hits) + " targets. Here is the complete list: " + str(hit_list))

# define a loop for playing the game again

# bug: doesn't randomly populate after the first round 

def play_again():
    answer = input("\nWanna play another round? (y/n)\n\t> ").lower()
    while answer == "y":
        print(f"Ok, {player1}. Here we go.")
        battleship_game()
        answer = input("\nWanna play another round? (y/n)\n\t> ").lower()
    else:
        print(f"It was nice playing with you, {player1}! CU next time.")  

battleship_game()        
play_again()