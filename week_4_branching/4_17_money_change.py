# 4.17 LAB: Exact change

# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

# Ex: If the input is:

# 0 
# (or less than 0), the output is:

# No change 
# Ex: If the input is:

# 45
# the output is:

# 1 Quarter
# 2 Dimes 

total_change=int(input())

num_dollars=total_change//100
num_quarters=(total_change-num_dollars*100)//25
num_dimes=(total_change-num_dollars*100-num_quarters*25)//10
num_nickels=(total_change-num_dollars*100-num_quarters*25-num_dimes*10)//5
num_pennys=(total_change-num_dollars*100-num_quarters*25-num_dimes*10-num_nickels*5)//1

#no change 
if total_change<=0:
   print('No change')
#dollars
if 0<num_dollars<=1:
   print(num_dollars,'Dollar')
if num_dollars>1:
   print(num_dollars,'Dollars')
#quarters  
if 0<num_quarters<=1:
   print(num_quarters,'Quarter')
if num_quarters>1:
   print(num_quarters,'Quarters')
#dimes   
if 0<num_dimes<=1:
   print(num_dimes,'Dime')
if num_dimes>1:
   print(num_dimes,'Dimes')
#nickels   
if 0<num_nickels<=1:
   print(num_nickels,'Nickel')
if num_nickels>1:
   print(num_nickels,'Nickels')
#pennies
if 0<num_pennys<=1:
   print(num_pennys,'Penny')
if num_pennys>1:
   print(num_pennys,'Pennies')