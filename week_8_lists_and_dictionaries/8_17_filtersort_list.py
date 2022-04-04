# 8.17 LAB: Filter and sort a list

# Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

# Ex: If the input is:

# 10 -7 4 39 -6 12 2
# the output is:

# 2 4 10 12 39
# For coding simplicity, follow every output value by a space. Do not end with newline.

''' Type your code here. '''
num_list = input()


nums = list(num_list.split())

nums = ([int(x) for x in nums])

# nums = ([x for x in nums if x >= 0])

nums = sorted(nums)


nums = ([x for x in nums if x >= 0])


# num_list = [i for i in num_list if i >= 0]

print(*nums, sep=' ', end=' ')

