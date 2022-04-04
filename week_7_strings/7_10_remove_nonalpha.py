# 7.10 LAB: Remove all non-alpha characters

# Write a program that removes all non-alpha characters from the given input.

# Ex: If the input is:

# -Hello, 1 world$!
# the output is:

# Helloworld

''' Type your code here. '''
given_input = input()

s1="".join(c for c in given_input if c.isalpha())
print (s1) 