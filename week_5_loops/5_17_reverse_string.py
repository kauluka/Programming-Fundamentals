# 5.17 LAB: Print string in reverse

# Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# done
# then the output is:

# ereht olleH
# yeH

def print_list(l):
    for num in l:
        print(num[::-1])
        # print()
l = []
while True:
    s = input() 
    if (s == "Done") or (s =="done") or (s == "d"):
        break
    l.append(s)

print_list(l)