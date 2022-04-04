# 4.14 LAB: Smallest number
# Write a program whose inputs are three integers, and whose output is the smallest of the three values.

# Ex: If the input is:

# 7
# 15
# 3
# the output is:

# 3


''' Type your code here. '''
first_num = int(input())
second_num = int(input())
third_num = int(input())

nums = []
nums.append(first_num)
nums.append(second_num)
nums.append(third_num)

print(min(nums))