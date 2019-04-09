#!/usr/bin/env python

def get_name():
    return raw_input('What are you? ')

def greet(name, times):
    for i in range(times):
        print("Hello, %s!" % name)

who = get_name()
greet(who, 10)
