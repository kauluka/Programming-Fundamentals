# 8.16 LAB: Varied amount of input data

# Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

# Ex: If the input is:

# 15 20 0 5
# the output is:

# 10 20
# Note: For output, round the average to the nearest integer.

''' Type your code here. '''
import statistics

input = input()

nums = list(input.split())

nums = ([int(x) for x in nums])

average = int( sum(nums) / len(nums) ) 

print(f"{average} {max(nums)}")