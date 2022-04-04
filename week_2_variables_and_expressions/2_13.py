# Driving is expensive. Write a program with a car's miles/gallon and gas dollars/gallon (both floats) as input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
# 2.13 LAB: Driving costs

''' Type your code here. '''
miles_p_gallon = float(input())
cost_p_gallon = float(input())

twenty_miles = 20 / miles_p_gallon * cost_p_gallon
seventy5_miles = 75 / miles_p_gallon * cost_p_gallon
five100_miles = 500 / miles_p_gallon * cost_p_gallon


print(f'{twenty_miles:.2f} {seventy5_miles:.2f} {five100_miles:.2f}')