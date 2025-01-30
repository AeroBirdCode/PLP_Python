# The following small program takes two numbers and an operator from user and perfroms necessary calculations.
# No conditional statements, we are using eval() and input() functions only. 

# Get user input
input1 = input("Enter number 1: ")
input2 = input("Enter number 2: ")
sign = input("Please indicate your sign: eg +, -, * or / : ")

# Perform the operation directly using eval
result = eval(f"{input1} {sign} {input2}")

# Display the result
print(f"{input1} {sign} {input2} = {result}")

