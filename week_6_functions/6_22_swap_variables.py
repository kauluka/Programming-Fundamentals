# 6.22 LAB: Swapping variables

# Define a function named swap_values that takes four integers as parameters and swaps the first with the second, and the third with the fourth values. Then write a main program that reads four integers from input, calls function swap_values() to swap the values, and prints the swapped values on a single line separated with spaces.

# Ex: If the input is:

# 3
# 8
# 2
# 4
# function swap_values() returns and the main program outputs:

# 8 3 4 2
# The program must define and call the following function. 
# def swap_values(user_val1, user_val2, user_val3, user_val4)

# Define your function here.
def swap_values(num1, num2, num3, num4):
    # print(f"{num2} {num1} {num4} {num3}")
    num1, num2 = num2, num1
    num3, num4 = num4, num3
    return num1, num2, num3, num4
    

if __name__ == '__main__': 
    # Type your code here. Your code must call the function.
    # user_list = []
    # for iteration in range(4):
    #     user_input = int(input())
    #     user_list.append(user_input)
    user_int1 = int(input())
    user_int2 = int(input())  
    user_int3 = int(input())  
    user_int4 = int(input())  
    
    print(swap_values(num1=user_int1, num2=user_int2, num3=user_int3, num4=user_int4))