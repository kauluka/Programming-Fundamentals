# 7.7 LAB: Count characters

# Write a program whose input is a string which contains a character and a phrase, 
# and whose output indicates the number of times the 
# character appears in the phrase. 
# The output should include the input character and use the plural form, n's,
# if the number of times the characters appears is not exactly 1.

''' Type your code here. '''

user_input = input()

letter = user_input[0]
phrase = user_input[1:]

n_times = phrase.count(letter)

if n_times == 1:
    print(f"{n_times} {letter}")
else:
    print(f"{n_times} {letter}'s")