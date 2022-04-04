# 6.20 LAB: Step counter

# A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float as a parameter, representing the number of feet walked, and returns an integer that represents the number of steps walked. Then, write a main program that reads the number of feet walked as an input, calls function feet_to_steps() with the input as an argument, and outputs the number of steps.

# Use floating-point arithmetic to perform the conversion.

# Ex: If the input is:

# 150.5
# the output is:

# 60
# The program must define and call the following function: 
# def feet_to_steps(user_feet)

import math
# Define your function here 
def feet_to_steps(user_feet):
    return user_feet // 2.5

if __name__ == '__main__':
    # Type your code here.
    user_feet = float(input())
    
    print(math.trunc(feet_to_steps(user_feet)))