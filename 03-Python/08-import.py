#!/usr/bin/env python

import random
import time

def check_guess(number, guess):
    if guess == number:
        print "yes, you are right!"
        return True
    else:
        print "That's wrong. try again!"
        return False

def get_guess():
    number_input = raw_input('Guess the number? ')
    try:
        number = int(number_input)
        return number
    except ValueError:
        print("That's not an int!")
        return 0

number = random.randint(1, 100)
guess = get_guess()
while not check_guess(number, guess):
    time.sleep(5)
    guess = get_guess()
