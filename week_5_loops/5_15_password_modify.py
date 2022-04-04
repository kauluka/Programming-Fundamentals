# 5.15 LAB: Password modifier

# Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

# i becomes 1
# a becomes @
# m becomes M
# B becomes 8
# s becomes $
# Ex: If the input is:

# mypassword
# the output is:

# Myp@$$word!

word = input()
password = ''

for letter in range(len(word)):
   newl = ""
   if word[letter] == "i":
      newl = "1"

   elif word[letter] == "a":
      newl = "@"

   elif word[letter] == "m":
      newl = "M"  

   elif word[letter] == "B":
      newl = "8"
   
   elif word[letter] == "s":
      newl = "$"
   else:
      newl = word[letter]
   password = password + newl 
print(password+"!")