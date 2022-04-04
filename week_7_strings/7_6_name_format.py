# Many documents use a specific format for a person's name. Write a program whose input is:

# firstName middleName lastName

# and whose output is:

# lastName, firstInitial.middleInitial.

# Ex: If the input is:

# Pat Silly Doe
# the output is:

# Doe, P.S.

''' Type your code here. '''
name = input()

list_of_name_pieces = name.split(" ")

if len(list_of_name_pieces) == 3:
    firstName, middleName, lastName = name.split(' ')
    print(f"{lastName}, {firstName[0]}.{middleName[0]}.")
else:
    firstName, lastName = name.split(' ')
    print(f"{lastName}, {firstName[0]}.")
