# 7.9 LAB: Palindrome

# A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

# Ex: If the input is:

# bob
# the output is:

# bob is a palindrome
# Ex: If the input is:

# bobby
# the output is:

# bobby is not a palindrome
# Hint: Start by removing spaces. Then check if a string is equivalent to its reverse.

''' Type your code here. '''
# pali = input()
# pali_no_space = pali.replace(" ", "")

def isPalindrome(s):
    return s == s[::-1]
 
# Driver code
pali = input()
pali_no_space = pali.replace(" ", "")
ans = isPalindrome(pali_no_space)
 
if ans:
    print(f"{pali} is a palindrome")
else:
    print(f"{pali} is not a palindrome")

#for i in range(len(pali_no_space)):
   # if pali_no_space[-1] == pali_no_space[0] and pali_no_space[-2] == pali_no_space[1]:
    #    print(f"{pali} is a palindrome")
  #  else:
  #    print(f"{pali} is not a palindrome")