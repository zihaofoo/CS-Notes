# Commentating techniques
# This is a single line comment, usually written beside a line of code to tell others what it is.
"""
This is a multi line comment (1)
This is a multi line comment (2)
"""

cube = 25
epsilon = 0.001
guess = 0.0
increment = 1E-03
num_guesses= 0
while abs(guess**3 -cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses+= 1
print('num_guesses=', num_guesses)
if abs(guess**3 -cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
    