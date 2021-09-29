# Intro

welcome_msg = "Welcome to the Ultimate Battleship Experience"
print(welcome_msg)
print("Who dares to enter the battle? Immediately state your name!")
player1 = input()
print("Ok then, " + player1 +", let's begin.")

# Rules
rules = "I will hide 10 battleships in total. More on that later."
print("First things first. Are you familiar with the rules? (y/n)")
answer_rules = input().lower()
if answer_rules == "y":
    print("Looks like we are good to go.")    
elif answer_rules == "n":
    print(rules)
else:
    print("Come again? Please enter y for yes or n for no.")

# Setting up playing field

playing_field = """
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

print("Press enter so that I can set up our playing field.")
input()
print("Let the battle begin!")
print(playing_field)

playing_field_rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
playing_field_columns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
playing_fields = []

for letter in playing_field_rows:
    for i in range(10):
        playing_fields.append(letter + playing_field_columns[i])

# define hidden ships
# 1 carrier: 4 spaces
# 2 battleships: 3 spaces
# 3 cruisers: 2 spaces
# 4 destroyers: 1 space

carrier = ["A1", "A2", "A3", "A4"]
battleship_1 = ["C5", "D5", "E5"]
battleship_2 = ["I5", "I6", "I7"]
cruiser_1 = ["G1", "H1"]
cruiser_2 = ["D8", "E8"]
cruiser_3 = ["G4", "G5"]
destroyer_1 = ["J0"]
destroyer_2 = ["B7"]
destroyer_3 = ["H9"]
destroyer_4 = ["D2"]
occupied_fields = carrier + battleship_1 + battleship_2 + cruiser_1 + cruiser_2 + cruiser_3 + destroyer_1 + destroyer_2 + destroyer_3 + destroyer_4
     
print("I have hidden my battleships well. If at any point during the game you would like to review the rules, enter '?', otherwise give me your next target.")

# game itself

target = input().upper()
if target == "?":
    print(rules)
elif target not in playing_fields:
    print("You are aiming outside the target area. Try again.")
elif target in occupied_fields:
    print("hit")
else:
    print("miss")



