"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Václav Jaroš
email: vaclav.jaros93@gmail.com
discord: vaclavjaros1993
"""
import random
import time
import csv


# BULLS AND COWS
LINE_SEPARATOR = 47 * "-"
CSV_FILENAME = "bulls_cows_statistics.csv"
TIME_ROUND = 2

# PROGRAM FUNCTIONS 
def greet_user():
    """ SIMPLE FUNCTION FOR GREET AND GAME INTRODUCTION"""
    print("Hi there!")
    print(LINE_SEPARATOR)
    print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    print(LINE_SEPARATOR)
    
def generate_pc_number():
    """THIS FUNCTION GENERATE RANDOM, UNIQUE 4 DIGIT THAT CANT START WITH 0"""
    digits = set(range(10))
    first = random.randint(1,9)
    last_three = random.sample(sorted(digits - {first}), 3)
    pc_number = [first] + last_three
    return pc_number

def get_user_input():
     """PROMPTS USER TO ENTER A 4-DIGIT NUMBER."""
     return input("ENTER A NUMBER:\n")

def valid_input(user_number):
    """VALIDATES IF INPUT IS A UNIQUE 4-DIGIT NUMBER THAT DOESNT START WITH 0."""
    if len(user_number) != 4:
        print("INPUT MUST BE 4-DIGIT NUMBER.")
        return False
    if not user_number.isdigit():
        print("INPUT MUST ONLY CONTAIN DIGITS.")
        return False
    if user_number[0] == "0":
        print("INPUT CANNOT START WITH 0.")
        return False
    if len(set(user_number)) != 4:
        print("DIGITS MUST BE UNIQUE.")
        return False
    return True

def evaluate_guess(user_number, pc_number):
    """COMPARE USER NUMBER TO THE PC NUMBER AND COUNT BULLS, COWS."""
    bulls = 0
    cows = 0

    for i, num in enumerate(user_number):
        if int(num) == pc_number[i]:  
            bulls += 1
        elif int(num) in pc_number:   
            cows += 1

    return bulls, cows

def format_result(bulls, cows):
    """FUNCTION FOR FORMATING PLURAL OR SINGULAR TERMS, LIKE '1 BULL, 2 COWS'"""
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"

def save_statistics(attempts, elapsed_time):
    """ THIS FUNCTION TAKES ATTEMPTS AND GAMETIME AND SAVE IT TO CSV.FILE"""
    with open(CSV_FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([attempts, round(elapsed_time, TIME_ROUND)])

# PROGRAM MAIN LOGIC
def main():
    greet_user()
    pc_number = generate_pc_number()
    # print(pc_number) # DEBUG PRINT
    attempts = 0 
    start_time = time.time()

    while True:
        user_number = get_user_input()
        
        if valid_input(user_number):
            attempts += 1
            bulls, cows = evaluate_guess(user_number, pc_number)
            print(format_result(bulls, cows))
            
            if bulls == 4:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts!")
                print("Game time:", round(elapsed_time), "seconds")

                # SAVE STATISTICS TO CSV FILE
                save_statistics(attempts, elapsed_time)
                print("Statistics saved.")
                break
                
        else:
            print("Invalid input. Enter a unique 4-digit number that doesn't start with 0.")
        print(LINE_SEPARATOR)

main()

