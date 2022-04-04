# 3.16 LAB: Simple statistics

# Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.

# Output each rounded integer using the following:
# print(f'{your_value:.0f}')

# Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.3f}')

# Ex: If the input is:

# 8.3
# 10.4
# 5.0
# 4.8
# the output is:

# 2072 7
# 2071.680 7.125

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

''' Type your code here. '''
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4 
print(f'{product:.0f} {average:.0f}')
print(f'{product:.3f} {average:.3f}')