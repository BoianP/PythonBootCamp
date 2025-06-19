
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#first solution
#from random import sample, choice
# password_length = nr_numbers + nr_symbols + nr_letters
#
# #generataes a random sequence of letters, symbols, numbers as types. Then for each type it will choose
# # a corresponding random value
# password_type = sample(["l", "s", "n"], counts = [nr_letters, nr_symbols, nr_numbers], k = password_length)
# password_list = []
# for item in password_type :
#     if item == "l" :
#         password_list.append(choice(LETTERS))
#     elif item == "s" :
#         password_list.append(choice(SYMBOLS))
#     elif item == "n" :
#         password_list.append(choice(NUMBERS))
# password = "".join(password_list)
# print(password)
# print(sample("password", len("password")))
#*********************************************************************************
#a second solution
#generate a list of random letter, numbers, and symbols and then shuffle it
from random import shuffle, choices
password_l = []
password_l.extend(choices(LETTERS, k = nr_letters))
password_l.extend(choices(SYMBOLS, k = nr_symbols))
password_l.extend(choices(NUMBERS, k = nr_numbers))

shuffle(password_l)
password = "".join(password_l)
print(password)