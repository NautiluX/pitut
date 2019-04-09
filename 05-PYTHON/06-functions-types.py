#!/usr/bin/env python

def get_name():
    return raw_input('What are you? ')

def get_amount():
    amount_input = raw_input('How often should I say hello? ')
    try:
        amount = int(amount_input)
        return amount
    except ValueError:
        print("That's not an int!")
        return 0

def greet(name, times):
    for i in range(times):
        print("Hello, %s!" % name)

who = get_name()
amount = get_amount()
greet(who, amount)
