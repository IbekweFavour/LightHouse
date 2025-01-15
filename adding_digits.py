def add_digits(number_list):

	running_total = 0
	
	for number in number_list:
		running_total += number
	return running_total
				 

list_of_numbers = [4,34,3,54,2,23]
Total = add_digits(list_of_numbers)

to_string = str(Total)
print(to_string[0], end = " + ")
print(to_string[1], end = " + ")
print(to_string[2])
