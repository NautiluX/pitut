# 01-hello.py
```
#!/usr/bin/env python

print("Hello, world!")
```
# 02-vars.py
```
#!/usr/bin/env python

who = "Pi"

print("Hello, %s!" % who)
```
# 03-input.py
```
#!/usr/bin/env python

who = raw_input('What are you? ')

print("Hello, %s!" % who)
```
# 04-loop.py
```
#!/usr/bin/env python

who = raw_input('What are you? ')

for i in range(10):
    print("Hello, %s!" % who)
```
# 05-functions.py
```
#!/usr/bin/env python

def get_name():
    return raw_input('What are you? ')

def greet(name, times):
    for i in range(times):
        print("Hello, %s!" % name)

who = get_name()
greet(who, 10)
```

## Uebung

* einlesen wie oft geloopt wird.
* hint: int(string) wandelt text in Zahl um

# 06-functions-types.py
```
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
```
# 07-if-bool.py
```
#!/usr/bin/env python

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

number = 42
guess = get_guess()
while not check_guess(number, guess):
    guess = get_guess()
```
# 08-import.py
```
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
```
