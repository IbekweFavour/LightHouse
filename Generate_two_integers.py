import random

users_entry = int(input("Enter a first_number: "))
users_second_entry = int(input("Enter the second number: "))
sum_of_numbers = users_entry + users_entry 

first_number_genration = [num_first for num_first in range(1, 100)]
second_number_generation = [num_second for num_second in range(1, 100)]

if sum_of_numbers in first_number_genration:
	print("true")
elif sum_of_numbers not in first_number_genration:
	print("false")