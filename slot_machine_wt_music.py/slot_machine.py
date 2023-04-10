# required libraries
# required libraries for generate slot machine random values
import random
# importing the datetime to get the current date and time
import datetime
from datetime import time
#voice(speaker)
import pyttsx3 
# libraries for background music
import pygame
from pygame.locals import *
from pygame import mixer
# libraries for typewriter
import sys
import os
import time

# initializing the global constant-value variables
max_lines = 3
max_bet = 100
min_bet = 1
# Specify the number of columns and rows
rows = 3
cols = 3


# Specify how many slot object (symbols) per column
symbol_count = {"🫀 ": 3, "🧠": 3, "🫁 ": 3, "👁️ ": 3}
# Specify the values of the symbols to multiply on the bet
symbol_value = {"🫀 ": 5, "🧠": 4, "🫁 ": 3, "👁️ ": 2}


# background music
def play_bgm():
    mixer.init()
    mixer.music.load('powdown-110017.ogg')
    mixer.music.play()
    mixer.music.set_volume(0.3)# volume up or down
    mixer.music.play(loops=-1)#the music will repeat indefinitely.

# define machine voice(speaker)
def speak(audio):
    #print("Sir, " + audio)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170) #slow voice speed
    engine.say(audio)
    engine.runAndWait()

# define a functions to get the current date and time
def get_date():# Current date
    return datetime.datetime.now().strftime("%d/%m/%y")

def get_time():# Current time
    return datetime.datetime.now().strftime("%H:%M")    

# opening wishes
def wishes():
    # get date
    print("Date: ", get_date())
    strDate = get_date()
    speak(f"The date is {strDate}.")
    
    # & Time
    print("Time: ", get_time())
    strTime = get_time()
    speak(f"The time is {strTime}.")

# typewriter function
text = ("\nWelcome to Sophia Learning - Python Programming Touchstone 4")
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char != "\n":
            time.sleep(0.1)

        else:
            time.sleep(1)

os.system("clear")  # for windows use cls instead of clear



# verifying winning or losing and print out the results after each spin.
def verify_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines): # loop through each line 
        symbol = columns[0][line] # check the symbol inside the first column of the current row
        for column in columns:
            symbol_to_check = column[line] # check the symbol looping through each column
            if symbol != symbol_to_check: # if symbols are not the same
               break
        else: # if get to the end without broke out the player won
            winnings += values[symbol] * bet # this bet is for the bet in each line
            winning_line.append(line + 1)
    
    return winnings, winning_line


# function to generate the symbols inside the slot machine
def slot_machine_spin(rows, cols, symbols):
    all_symbols = [] # create a list to randomly select the values
    # add the symbols into the all_symbol list
    for symbol, symbol_count in symbols.items(): # use .items() to get both the key and the associated value from the dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)
   
  # select random values for each column
    columns = [] # define column list
    for _ in range(cols): # generate the values (symbols) inside the columns
        column = [] # represent the values for every column
        current_symbols = all_symbols[:] # copy of all_symbols list 
        for _ in range(rows): # loop through the number of values to generated
            value = random.choice(current_symbols) # select a random values from the current_symbols list
            current_symbols.remove(value) # find and delete the value from the current_symbols list in order to not pick it again
            column.append(value) # add the value to the column list
        
        columns.append(column) # add the column to the columns list.
    
    return columns


# print out the slot
def draw_slot_machine(columns):
    for row in range(len(columns[0])): # loop through the rows and print the first value
        for i, column in enumerate(columns): # loop through the columns and get the index 
            if i != len(columns) - 1:
               print(column[row], end=" | ") # print the value of first row
            else:
               print(column[row], end="") # print the value of the single row and end the line
        print()# print an empty new line
  

# function for deposit and balance
def deposit():  # This function is responsible for collecting user's input that get the deposit from the user.
    while True: # loop for continually ask the user to enter a deposit amount until they give a valid amount and then break out.
          typewriter(f"\nHow much $ do you want to deposit? ")
          speak(f"{client_name} How much money do you want to deposit?")
          amount = input("\n$ - deposit? $")
          speak(f"You have deposited {amount} to your account")

          if amount.isdigit():  # to make sure that the amount is a number.
             amount = int(amount)# convert string in to a numeric value (integer).
             if amount > 0: # check if number is grater than 0 in order to break or get them to try again. 
                break # if input greater than 0, break the wallet and end the loop.
             else: # if number is not greater than 0
                typewriter(f"$$$ Amount > 0")
                speak(f"{client_name} Money amount must be greater than $0.")
          else: # if the amount entered is not a digit (number) 
             typewriter("Please enter a valid character (number).")
             speak(f"{client_name} The amount must be a number.")

    return amount


# lines
def number_of_line():
    while True: # loop for continually ask the user to enter the number of lines they want to bet on until they give a valid number of line and then break out.
          typewriter(f"\nEnter the number of lines you want to bet on. ")
          speak(f"{client_name} Please enter the number of lines you want to bet on (1 to" + str(max_lines) + ") ")
          line = input("Enter 1, 2 or 3 ")
          if line.isdigit(): # to make sure that the line input is a number.
             line = int(line) # to convert the string in to a numeric value (integer).
             if 1 <= line <= max_lines: # to check if the line value is between min(1) and max(3) lines.
                break # if it meets the condition then end the loop.
             
             else: # condition for enter a valid number of lines 1-3.
                typewriter(f"\nPlease enter a number between 1 and "
                + str(max_lines) + ".")
                speak(f"{client_name} Wrong number of lines. Please enter a number between 1 and " + str(max_lines) + ".")
                
          else: # condition for enter a valid digit (number) between 1-3.
             typewriter("Wrong option, please enter a number between 1 and " +
                       str(max_lines) + ".")
             speak("Wrong option, please enter a number between 1 and " + str(max_lines) + ".")
             typewriter("Please enter a number.")

    return lines


# funtion to collect the money amount the player want to bet and in how many rows or lines they want to bet on.
def get_bet():
    while True: # loop for continually ask the user to enter the money amount they want to bet on until they give a valid amount and then break out.
          typewriter(f"\nHow much would  you  like  to  bet  per  line?  ")
          speak(f"{client_name} How much would  you  like  to  bet  on  each  line?")
          amount = input("\n$")
          if amount.isdigit():# to make sure that the amount entered is a number.
             amount = int(amount)# to convert the string in to a numeric value (integer).
             if min_bet <= amount <= max_bet: # to check if the amount entered is between the min($1) and max($100) amount to bet.
                break # if it meets the condition of bet amount then end the loop.
             else: # otherwise, if the input is not metting the condition for a valid bet amount.
                typewriter(f"\nAmount | ${min_bet} - ${max_bet}.")
                speak(f"{client_name} The amount must be between ${min_bet} - ${max_bet}.")
                
          else: # if the amount entered is not a number.
              typewriter(f"\nWrong option, enter an amount($).")
              speak(f"{client_name}Please, enter an amount of money do you want to bet.")

    return amount # return to the input


# bet info (balance & winning) to execute 1 game
# this allow to get the bet amount($) according to the player money balance.
def game(balance): 
    line = number_of_line()
    while True: # loop for continually ask the user to enter the number of lines they want to bet on until they give a valid number of line and then break out.    
          bet = get_bet()
          total_bet = bet * line # bet per line
        
          if total_bet > balance : # if bet is greater than current balance
             typewriter(f"\nbalance: ${balance}.")
             speak(f"{client_name}, your current balance is ${balance}.")
             typewriter(f"\nBalance: ${balance}\n")
             speak(f"Sorry {client_name}, you don't have enough money to bet.Your current balance: ${balance}")
             speak(f" Thank you for playing!")
             break
          else: # if bet is less than current balance
             break

    typewriter(f"{lines} : ${total_bet}")
    speak(f"{client_name} You are betting ${bet} on {lines} lines.")
    typewriter(f"${total_bet}\n")
    speak(f"\nTotal bet is equal to ${total_bet}\n")
    # random spinning for slots
    print("\n")# print a new empty line
    slot_machine = slot_machine_spin(rows, cols, symbol_count)
    draw_slot_machine(slot_machine)
    winnings, winning_lines = verify_winnings(slot_machine, line, bet, symbol_value)
    typewriter(f"\nYou won ${winnings}.")
    speak(f"{client_name} You won ${winnings}")
    print(f"\nYou won on line:", *winning_lines)
    return winnings - total_bet # return how much player won or lose from the spin


# Game Opening 
def program_opening():
    print("\n-------------------------------🎰-------------------------------")
    typewriter(text)
    speak("Welcome to Sophia Learning - Python Programming Touchstone 4")
    typewriter(f"This virtual machine is a slot machine for gambling games.")
    speak(f"This virtual machine is a slot machine for gambling games.")
    typewriter(f"\nI hope you enjoy it.")
    speak(f"I hope you enjoy it.")
    typewriter("\nEven though I am not allowed to bet, if I could, I would bet on you!")
    speak("Even though I am not allowed to bet, if I could, I would bet on you!")
    typewriter("\nGood luck!\n")
    speak("Good luck!")
    print("-------------------------------🎰-------------------------------")


# -------------------------------🎰-------------------------------
# the program begins
play_bgm()
program_opening()
wishes()

# get client name
speak("What is you name?")
client_name = input("name: ")
typewriter(f"Welcome to the bookmaker!")
speak(f"Hello {client_name}, Welcome to the bookmaker!")

# main program
def main():
    balance = deposit()  # to enter the amount of money for the gambling game
    while True:  # running the game
          typewriter(f"\nYour current balance is ${balance}\n" )  # constantly print out the player current balance
    # it allow to deposit again when balance is 0 or end the game
    if balance == 0:
       typewriter(f"Insuficient, balance ${balance}.")
       speak(f"Sorry {client_name}, you don't have enough money to bet.")
       typewriter("Another deposit? ")
       speak("\nDo you want to deposit again?")
       speak("Yes or No")
       answer = input("\ny / n ?  ")
       if answer.lower() == "y":
          balance += deposit()
       elif answer == "n":  # to end the game
            break
       typewriter(f"Press enter to play or e to exit")
       speak(f"Press enter to play or e to exit")
       answer = input("? ")
       if answer == "e":
          break
       balance += spin(balance)
    typewriter(f"\nYou left with ${balance}")
    speak(f"\nYou left with ${balance}")
    speak(f"{client_name} Thank you for playing!, Hope you come back to play again, see you soon!")
    speak("Goodbye!")
    typewriter("\n-------------------------------🎰-------------------------------\n")


main()
