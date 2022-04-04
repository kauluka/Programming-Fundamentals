# 4.19 LAB: Golf scores

# Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:

# "Eagle": number of strokes is two less than par
# "Birdie": number of strokes is one less than par
# "Par": number of strokes equals par
# "Bogey": number of strokes is one more than par
# Given two integers that represent par and the number of strokes used, write a program that prints the appropriate score name. Print "Error" if par is not 3, 4, or 5.

# Ex: If the input is:

# 4
# 3
# the output is:

# Birdie

''' Type your code here. '''
par = int(input())
score = int(input())

output = "Error"

if (par == 3) or (par == 4) or (par == 5):
    if (par - score) == 2:
        output = "Eagle"
    elif (par - score) == 1:
        output = "Birdie"
    elif (par - score) == 0:
        output = "Par"
    elif (par - score) == -1:
        output = "Bogey"
else:
        output = "Error"
print(output)
    

