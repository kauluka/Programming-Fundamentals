#Write a program using integers user_num and x as input, and output user_num divided by x three times.

''' Type your code here. '''
user_num = int(input())
x = int(input())

answer_1 = int(user_num / x)
answer_2 = int(answer_1 / x)
answer_3 = int(answer_2 / x)

print(answer_1, answer_2, answer_3)