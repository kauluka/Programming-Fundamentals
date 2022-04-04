# 2.17 LAB: Convert to dollars

# Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount as dollars and cents.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'Amount: ${dollars:.2f}')

''' Type your code here. '''
quarters = int(input())
dimes = int(input())
nickels = int(input())
pennies = int(input())

quarter_val = 0.25
dime_val = 0.10
nickel_val = 0.05
penny_val = 0.01

amount = quarters*quarter_val + dimes*dime_val + nickels*nickel_val + pennies*penny_val

print(f"Amount: ${amount:.2f}")