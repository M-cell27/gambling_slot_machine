# required libraries
import random
import datetime
from datetime import time
import pyttsx3 #voice(speaker)
# libraries for background music
import pygame
from pygame.locals import *
from pygame import mixer
# libraries for dinamic writing
import sys
import os
import time


max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "🫀 ": 2,
    "🧠": 4,
    "🫁 ": 6,
    "👁️ ": 8
}

symbol_value = {
    "🫀 ": 5,
    "🧠": 4,
    "🫁 ": 3,
    "👁️ ": 2
}

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

# define date & time functions
# date
def get_date():
    return datetime.datetime.now().strftime("%d/%m/%y")
# time
def get_time():
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

os.system("clear") # for linux use clear instead of cls


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


# verifying winning or losing
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
               break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# def machine_spin
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
               print(column[row], end=" | ")
            else:
               print(column[row], end="")

        print()


def deposit():
    while True:
        speak(f"{client_name} How much money do you want to deposit?")
        amount = input("\n$$$ - deposit? $")
        speak(f"You have deposited {amount} to your account")
        
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
               break
            else:
               speak(f"{client_name}Money amount must be greater than $0.")
               print("$$$ Amount > 0")
        else:
            speak(f"{client_name} The amount must be a number.")
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        speak(f"{client_name} Please enter the number of lines you want to bet on (1-" + str(max_lines) + ")? ")
        lines = input(
            "Number of lines to bet on (1-" + str(max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                speak(f"{client_name} Wrong number of lines. Please enter a number between 1 and " + str(max_lines) + ".")
                typewriter("Enter a valid number of lines.")
        else:
            speak("Wrong option, please enter a number between 1 and " + str(max_lines) + ".")
            typewriter("Please enter a number.")

    return lines


def get_bet():
    while True:
        speak(f"{client_name} How much would  you  like  to  bet  on  each  line?")
        amount = input("\nbet per each line? $")
        if amount.isdigit():
           amount = int(amount)
           if min_bet <= amount <= max_bet:
              break
           else:
              speak(f"{client_name} The amount must be between ${min_bet} - ${max_bet}.")
              typewriter(f"\nAmount / ${min_bet} - ${max_bet}.")
        else:
              speak(f"{client_name}Please enter an amount.")
              typewriter("\n$$$ (number)\n")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
          bet = get_bet()
          total_bet = bet * lines

          if total_bet > balance:
             speak(f"{client_name}, your current balance is ${balance}.")
             typewriter(f"\nBalance: ${balance}\n")
             speak(f"Sorry {client_name}, you don't have enough money to bet.Your current balance: ${balance}")
             speak(f" Thank you for playing!")
             break
          else:
             break

    speak(f"{client_name} You are betting ${bet} on {lines} lines.")
    typewriter(f"{lines} : ${total_bet}")
    speak(f"\nTotal bet is equal to ${total_bet}\n")
    # ramdom spinning for slots
    print("\n")
    slots = get_slot_machine_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    typewriter(f"\nYou won ${winnings}.")
    speak(f"{client_name} You won ${winnings}")
    typewriter(f"You won on lines:", *winning_lines)
    return winnings - total_bet

# -------------------------------🎰-------------------------------
#program_opening
play_bgm()
program_opening()
wishes()

# get client name
speak("What is you name?")
client_name = input("Enter your name: ")
typewriter("\nWelcome to the bookmaker!")
speak(f"Hello {client_name}, Welcome to the bookmaker!")

# main program
def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance is ${balance}\n")
        typewriter(f"Press enter to play or e to exit")
        speak(f"Press enter to play or e to exit")
        answer = input("Press enter to play (e to exit).")
        if answer == "e":
            break
        balance += spin(balance)
    typewriter(f"\nYou left with ${balance}")
    speak(f"\nYou left with ${balance}")
    speak(f"{client_name} Thank you for playing!, Hope you come back to play again, see you soon!")
    speak("Goodbye!")
    typewriterprint("\n-------------------------------🎰-------------------------------\n")


main()