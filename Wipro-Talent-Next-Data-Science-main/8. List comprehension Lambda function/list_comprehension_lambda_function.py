# Write a LC program to create an output dictionary 
# which contains only the odd numbers that are 
# present in the input list = [1,2,3,4,5,6,7] 
# as keys and their cubes as values

input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print("Output of Question 1:")
print(output_dict)

# Output:
# {1: 1, 3: 27, 5: 125, 7: 343}


# ---------------------------------------------
# Make a dictionary of the 26 English alphabets 
# mapping each with the corresponding integer

import string
alphabet_dict = {char: idx + 1 for idx, char in enumerate(string.ascii_lowercase)}
print("\nOutput of Question 2:")
print(alphabet_dict)

# Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, ..., 'z': 26}


# ---------------------------------------------
# Cube every number in the given list 
# list_1 = [1,2,3,4,5,6,7,8,9] using lambda and map()

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed_list = list(map(lambda x: x**3, list_1))
print("\nOutput of Question 3:")
print(cubed_list)

# Output:
# [1, 8, 27, 64, 125, 216, 343, 512, 729]
