# 7.8 LAB: Mad Lib - loops

# Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.

# Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in the example below. The program repeats until the input string is quit and disregards the integer input that follows.

# Ex: If the input is:

# apples 5
# shoes 2
# quit 0
# the output is:

# Eating 5 apples a day keeps the doctor away.
# Eating 2 shoes a day keeps the doctor away.

''' Type your code here. '''
mad_lib = []

keep_going = True
while keep_going:
    mad_words = input()
    if mad_words == "quit 0":
        keep_going = False
# mad_words = input()
#     if mad_words == "quit":
#         break
    else:
        mad_lib.append(mad_words)

for input_pieces in range(len(mad_lib)):
    #print(mad_lib[input_pieces])
    word, number = mad_lib[input_pieces].split(" ") # first round, mad_lib[0] is 
    print(f"Eating {number} {word} a day keeps the doctor away.")
