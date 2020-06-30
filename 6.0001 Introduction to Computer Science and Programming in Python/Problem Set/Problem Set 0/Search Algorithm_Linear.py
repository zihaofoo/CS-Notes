"""
Created on Thu May 21 20:12:32 2020

@author: Zi Hao Foo
"""

guess = 0.0
num_guesses = 0
print_freq = 100000
cube_in = float(input("Enter number to be rooted: "))
power_in = float(input("Enter exponent: "))

epsilon = 0.00001 * cube_in

if cube_in >= 0:
    increment = 0.0001 * cube_in
else:
    increment = -0.0001 * cube_in

while abs(cube_in - guess**power_in) >= epsilon and guess**power_in < cube_in:
    guess = guess + increment
    num_guesses = num_guesses + 1
    
    if (num_guesses % print_freq) == 0:
        print(num_guesses, guess)
        
print("The solution to", cube_in, "^", 1/power_in, "is", guess)
         