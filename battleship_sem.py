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
