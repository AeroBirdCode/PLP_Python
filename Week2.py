# This submission contains PART 1 and PART 2.
# PART 1 is the required assignment and PART 2 is the recommended challenge.

# PART 1: Assignment

# Create an empty list
my_list = []

# Append elements 10, 20, 30, 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of value 30
index_of_30 = my_list.index(30)

# Display results
print("Final list:", my_list)
print("Index of 30:", index_of_30)


# PART 2: CODING CHALLENGE IN WEEK2
# Task 1: Create a list of integers and compute their sum
numbers = []
# Get the number of inputs
count = int(input("How many numbers do you want to enter? "))  

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    # Add number to the list
    numbers.append(num)
    
# Compute the sum of all numbers and display the sum
total_sum = sum(numbers)  
print("Sum of all numbers:", total_sum)

#Print new line
print()


# Task 2: Create a tuple of favorite books and print each book name
favorite_books = ("RICH DAD POOR DAD", "ATOMIC HABITS", "ART OF WAR", "12 RULES", "ZERO TO ONE")  

print("My favorite books are:")
for book in favorite_books:
    print(book)  
print()

# Task 3: Store information about a person using a dictionary
# Initialize an empty dictionary
person_info = {}  
# Collect user input
person_info["name"] = input("Enter your name: ")
person_info["age"] = input("Enter your age: ")
person_info["color"] = input("Enter your favorite color: ")

# Print the dictionary and new line
print("Person Information:", person_info)  
print()


# Task 4: Create two sets and find common elements
# Initialize an empty sets
set1 = set()  
set2 = set()

# Get size of first set
size1 = int(input("How many numbers in the first set? "))  
for i in range(size1):
    num = int(input(f"Enter number {i+1} for set 1: "))
    # Add number to set 1
    set1.add(num)
    
# Get size of second set
size2 = int(input("How many numbers in the second set? "))  
for i in range(size2):
    num = int(input(f"Enter number {i+1} for set 2: "))
    # Add number to set 2
    set2.add(num)
    
# Find common elements and print them
common_elements = set1 & set2  
print("Common elements in both sets:", common_elements)
print()

# Task 5: Store a list of words and filter words with odd number of characters
# Define the list of words
words = ["PLP", "Evans", "Chakim", "apple", "banana", "grape", "orange", "kiwi"]
# Filter words with odd length
# I will use list compression 
odd_length_words = [word for word in words if len(word) % 2 != 0]  

print("Words with odd number of characters:", odd_length_words)
