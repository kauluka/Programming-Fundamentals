# 3.14 LAB: Input and formatted output: Right-facing arrow

# Given input characters for an arrowhead and arrow body, print a right-facing arrow.

# Ex: If the input is:

# *
# #
# Then the output is:

#       #
# ******##
# ******###
# ******##
#       #

base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char
''' Type your code here. '''

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

