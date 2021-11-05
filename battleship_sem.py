# Intro

welcome_msg = "Welcome to the Ultimate Battleship Experience\n(Press ENTER to start)"
print()
print(welcome_msg)
input()
print("Who dares to enter the battle? Immediately state your name!")
player1 = input()
print()
while player1 == "":
    print("I didn't get that. Please, state your name.")
    player1 = input()
else:
    print("Ok then, " + player1 +", let's begin.")
print()

# Rules (need to be refined)
rules = """ 
I will hide 10 ships. Together they occupy a total of 20 fields.
The ships can be distributed horizontally or vertically, but not diagonally.
None of the ships touches another (not even diagonally).
The ships contain 1 carrier (4 fields), 2 battleships (3 fields), 3 carriers (2 fields) and 4 destroyers (1 field).
I will let you know, once you have sunk a particular ship.
You will have 75 missiles in total. If you manage to sink all my ships, YOU WIN.
Else, I WIN.
"""

print("First things first. Are you familiar with the rules, " + player1 + "? (y/n)")
answer_rules = input().lower()
while answer_rules != "y" and answer_rules != "n":
    print()
    print("Come again? Please enter y for yes or n for no.")
    answer_rules = input().lower()
else:
    if answer_rules == "y":
        print()
        print("Looks like we are good to go.")    
        print()
    else:
        print(rules)
    
# Setting up playing field

playing_field_empty = """
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

playing_field_rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
playing_field_columns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
playing_fields = []
for letter in playing_field_rows:
    for i in range(10):
        playing_fields.append(letter + playing_field_columns[i])

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

# game itself

def battleship_game():
    print("Press ENTER so that I can set up our playing field.")
    input()
    print("Let the battle begin!")
    print(playing_field_empty)
    available_fields = []
    for letter in playing_field_rows:
        for i in range(10):
            available_fields.append(letter + playing_field_columns[i])
    occupied_fields = []

    carrier = []
    battleship_1 = []
    battleship_2 = []
    cruiser_1 = []
    cruiser_2 = []
    cruiser_3 = []
    destroyer_1 = []
    destroyer_2 = []
    destroyer_3 = []
    destroyer_4 = []
    
    # function that takes parameter of how many spaces a ship occupies

    def place_ship(num):
        ship = []
        for i in range(num):
            ship.append("")
        if num < 1 or num > 4:
            print("Error. A ship needs to occupy at least one and a maximum of 4 playing fields. Set num equal to an integer between 1 and 4.")
        ship[0] = select_random_field(available_fields)
        if num > 1:     
            index_counter = playing_fields.index(ship[0])
            dist = select_random_distribution()
            if dist == "horizontal":
                if str(num-2) in ship[0] or str(num-3) in ship[0] or str(num-4) in ship[0]:
                    dir = "right"
                elif str(num+3) in ship[0] or str(num+4) in ship[0] or str(num+5) in ship[0]:
                    dir = "left"
                else:
                    dir = select_random_left_right()
                for i in range(num-1):
                    if dir == "right":
                        index_counter += 1
                        ship[i+1] = playing_fields[index_counter]
                    else:
                        index_counter -=1
                        ship[i+1] = playing_fields[index_counter]
            else:
                if index_counter < (num-1)*10:
                    dir = "down"
                elif index_counter > (len(playing_fields)-1) - (num-1)*10:
                    dir = "up"
                else:
                    dir = select_random_up_down()
                for i in range(num-1):
                    if dir == "down":
                        index_counter += 10
                        ship[i+1] = playing_fields[index_counter]
                    else:
                        index_counter -=10
                        ship[i+1] = playing_fields[index_counter]
        return ship

    def remove_from_available_fields(ship):
        fields_to_be_removed = []
        for i in range(len(ship)):
            if ship[i] == "A0":
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])+1)
                fields_to_be_removed.append(playing_fields.index(ship[i])+10)
                fields_to_be_removed.append(playing_fields.index(ship[i])+11)
            elif ship[i] == "J9":
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])-1)
                fields_to_be_removed.append(playing_fields.index(ship[i])-10)
                fields_to_be_removed.append(playing_fields.index(ship[i])-11)
            elif "A" in ship[i]:
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])-1)
                fields_to_be_removed.append(playing_fields.index(ship[i])+1)
                fields_to_be_removed.append(playing_fields.index(ship[i])+9)
                fields_to_be_removed.append(playing_fields.index(ship[i])+10)
                fields_to_be_removed.append(playing_fields.index(ship[i])+11)
            elif "J" in ship[i]:
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])-1)
                fields_to_be_removed.append(playing_fields.index(ship[i])-9)
                fields_to_be_removed.append(playing_fields.index(ship[i])-10)
                fields_to_be_removed.append(playing_fields.index(ship[i])-11)
                fields_to_be_removed.append(playing_fields.index(ship[i])+1)
            elif "0" in ship[i]:
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])-9)
                fields_to_be_removed.append(playing_fields.index(ship[i])-10)
                fields_to_be_removed.append(playing_fields.index(ship[i])+1)
                fields_to_be_removed.append(playing_fields.index(ship[i])+10)
                fields_to_be_removed.append(playing_fields.index(ship[i])+11)
            elif "9" in ship[i]:
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])-1)
                fields_to_be_removed.append(playing_fields.index(ship[i])-10)
                fields_to_be_removed.append(playing_fields.index(ship[i])-11)
                fields_to_be_removed.append(playing_fields.index(ship[i])+9)
                fields_to_be_removed.append(playing_fields.index(ship[i])+10)
            else:
                fields_to_be_removed.append(playing_fields.index(ship[i]))
                fields_to_be_removed.append(playing_fields.index(ship[i])-1)
                fields_to_be_removed.append(playing_fields.index(ship[i])-9)
                fields_to_be_removed.append(playing_fields.index(ship[i])-10)
                fields_to_be_removed.append(playing_fields.index(ship[i])-11)
                fields_to_be_removed.append(playing_fields.index(ship[i])+1)
                fields_to_be_removed.append(playing_fields.index(ship[i])+9)
                fields_to_be_removed.append(playing_fields.index(ship[i])+10)
                fields_to_be_removed.append(playing_fields.index(ship[i])+11)
        list_without_duplicates = []
        for field in fields_to_be_removed:
            if field not in list_without_duplicates:
                list_without_duplicates.append(field)
        list_without_duplicates.sort(reverse = True)
        real_content_list = []
        for index in list_without_duplicates:
            real_content_list.append(playing_fields[index])
        real_content_list_filtered = []
        for element in real_content_list:
            if element in available_fields:
                real_content_list_filtered.append(element)
        index_in_available_fields_list = []
        for elem in real_content_list_filtered:
            index_in_available_fields_list.append(available_fields.index(elem))
        for item in index_in_available_fields_list:
            available_fields.pop(item)

    # define function to test if ship occupies already occupied fields

    def test_if_occupied(ship):
        occupied = False
        for field in ship:
            if field not in available_fields:
                occupied = True
        return occupied

    # populate playing field randomly

    carrier = place_ship(4)
    occupied_fields += carrier
    remove_from_available_fields(carrier)
    battleship_1 = place_ship(3)
    while test_if_occupied(battleship_1) == True:
        battleship_1 = place_ship(3)
    occupied_fields += battleship_1
    remove_from_available_fields(battleship_1)
    battleship_2 = place_ship(3)
    while test_if_occupied(battleship_2) == True:
        battleship_2 = place_ship(3)
    occupied_fields += battleship_2
    remove_from_available_fields(battleship_2)
    cruiser_1 = place_ship(2)
    while test_if_occupied(cruiser_1) == True:
        cruiser_1 = place_ship(2)
    occupied_fields += cruiser_1
    remove_from_available_fields(cruiser_1)
    cruiser_2 = place_ship(2)
    while test_if_occupied(cruiser_2) == True:
        cruiser_2 = place_ship(2)
    occupied_fields += cruiser_2
    remove_from_available_fields(cruiser_2)
    cruiser_3 = place_ship(2)
    while test_if_occupied(cruiser_3) == True:
        cruiser_3 = place_ship(2)
    occupied_fields += cruiser_3
    remove_from_available_fields(cruiser_3)
    destroyer_1 = place_ship(1)
    occupied_fields += destroyer_1
    remove_from_available_fields(destroyer_1)
    destroyer_2 = place_ship(1)
    occupied_fields += destroyer_2
    remove_from_available_fields(destroyer_2)
    destroyer_3 = place_ship(1)
    occupied_fields += destroyer_3
    remove_from_available_fields(destroyer_3)
    destroyer_4 = place_ship(1)
    occupied_fields += destroyer_4
    remove_from_available_fields(destroyer_4)

    all_ships = [[carrier], [battleship_1, battleship_2], [cruiser_1, cruiser_2, cruiser_3], [destroyer_1, destroyer_2, destroyer_3, destroyer_4]]
    battleships = battleship_1 + battleship_2
    cruisers = cruiser_1 + cruiser_2 + cruiser_3
    destroyers = destroyer_1 + destroyer_2 + destroyer_3 + destroyer_4

# function to display solved playing field

    def display_solution():
        playing_field_solution = playing_field_empty
        for field in playing_fields:
            playing_field_progress = """"""
            if field in occupied_fields:
                playing_field_progress = playing_field_solution.replace(" " + field + " ", "OOOO")
            else:
                playing_field_progress = playing_field_solution.replace(" " + field + " ", "~~~~")
            playing_field_solution = playing_field_progress
        return playing_field_progress

    print("I have hidden my ships well.\nIf at any point during the game you would like to review the rules, enter '?'.\nOtherwise give me your first target.")
    hit_list = []
    miss_list = []
    total_missiles = 0
    total_hits = 0

    # create function to reprint the playing field with hits and misses marked after each shot
    
    playing_field_updated = playing_field_empty 
    def playing_field_update(aim, hit_or_miss):
        playing_field_progress = """"""
        if hit_or_miss == "MISS":
            playing_field_progress = playing_field_updated.replace(" " + aim + " ", "~~~~")
        elif hit_or_miss == "HIT":
            playing_field_progress = playing_field_updated.replace(" " + aim + " ", "OOOO")
        else:
            playing_field_progress = playing_field_updated
        return playing_field_progress
    
    # create function to detect if a ship has been sunk (start with carrier)

    def ship_sunk(aim):
        if aim in occupied_fields:
            if aim in destroyers:
                print("*** SHIP SUNK ***")
                print("You have sunk one of my destroyers.")
                if all(field in hit_list for field in destroyers):
                    print("All destroyers down.")
            elif aim in carrier:
                if all(field in hit_list for field in carrier):
                    print("*** SHIP SUNK ***")
                    print("You have sunk my carrier.")
            elif aim in battleship_1:
                if all(field in hit_list for field in battleship_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my battleships.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            elif aim in battleship_2:
                if all(field in hit_list for field in battleship_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my battleships.")
                    if all(field in hit_list for field in battleships):
                        print("All battleships down.")
            elif aim in cruiser_1:
                if all(field in hit_list for field in cruiser_1):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif aim in cruiser_2:
                if all(field in hit_list for field in cruiser_2):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")
            elif aim in cruiser_3:
                if all(field in hit_list for field in cruiser_3):
                    print("*** SHIP SUNK ***")
                    print("You have sunk one of my cruisers.")
                    if all(field in hit_list for field in cruisers):
                        print("All cruisers down.")            
    for i in range(75):
        target = input().upper()
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
        playing_field_updated = playing_field_update(target, outcome)
        print()
        if outcome == "HIT":
            print("*** " + outcome + " ***")
            ship_sunk(target)
        else:
            print("*** " + outcome + " ***")
            print(message)
        print(playing_field_updated)

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
        print()
        print("*****   YOU WIN   *****\n\nCongratulations! It took " + str(total_missiles) + " missiles to take all my ships down. \nWell done, " + player1 + "!")
    else:
        print()
        print("*****   YOU LOSE   *****\n\nSorry, " + player1 + ". You didn't manage to destroy all my ships with the number of missiles at your disposal.")
        print("Here is the solution:")
        print(display_solution())
        print("You managed to hit " + str(total_hits) + " targets. Here is the complete list: " + str(hit_list))

battleship_game()

def play_again():
    print()
    print("Wanna play another round? (y/n)")
    answer = input().lower()
    while answer == "y":
        print("Ok, " + player1 + ". Here we go.")
        battleship_game()
        print()
        print("Wanna play another round? (y/n)")
        answer = input().lower()
    else:
        print("It was nice playing with you, " + player1 + "! CU next time.")  
        
play_again()