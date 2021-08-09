#Columnar transposition
#Author: Julio Aviña
import math

#global vars
user_string = ''
string_len = 0
number_of_columns = 0
flag_number_of_columns = False
wrapped_string = []
encoded_string = ''
decoded_string = ''
auxiliar_matrix = []

#set user string
def set_user_string(entered_user_string):
    global user_string
    user_string = entered_user_string

#compute string columns
def compute_string_columns():
    global string_len
    string_len = len(user_string)

#set number of columns
def set_number_of_colums(number_c):
    global number_of_columns
    number_of_columns = number_c
    
#encode string
def string_to_encode(string_to_encode, columns_string):
    global auxiliar_matrix
    global decoded_string
    auxiliar_matrix = [''] * columns_string
    for column in range(columns_string):
        counter = column
        while counter < len(string_to_encode):
            auxiliar_matrix[column] += string_to_encode[counter]
            counter += columns_string
    for letter in auxiliar_matrix:
        decoded_string += letter
    return decoded_string

#decode sring
def string_to_decode(string_to_encode, columns_string):
    global decoded_string
    global string_len
    num_colums_to_decode = math.ceil(string_len / columns_string)
    number_of_rows = columns_string
    empty_cells = (num_colums_to_decode * number_of_rows) - string_len
    auxiliar_matrix = [""] * num_colums_to_decode
    column = 0
    row = 0
    for letter in string_to_encode:
        auxiliar_matrix[column] += letter
        column += 1
        if (column == num_colums_to_decode) or (column == num_colums_to_decode - 1) and (row >= number_of_rows - empty_cells):
            column = 0
            row += 1
    for letter in auxiliar_matrix:
        decoded_string += letter
    return decoded_string


#encode string
def encode_string():
    global flag_number_of_columns, user_string
    set_user_string(input('Enter the string to cipher (The string must have a length greater than 3): '))
    compute_string_columns()
    while flag_number_of_columns == False:
        set_number_of_colums(int(input('Enter the number of colums between [2 and ' + str(int(string_len) - 1) + ']:')))
        if number_of_columns >= 2 and number_of_columns <= int(string_len) - 1:
            flag_number_of_columns = True
    return string_to_encode(user_string, number_of_columns)
    
    
#decode string
def decode_string():
    set_user_string(input('Enter the string to decipher (The string must have a length greater than 3): '))
    set_number_of_colums(int(input('Enter the number of colums: ')))
    compute_string_columns()
    return string_to_decode(user_string, number_of_columns)
    
def main():
    print('You want to do?\n\n')
    print('1. cipher string\n')
    print('2. decipher string\n')
    option = int(input('# '))
    if option == 1:
        print('The cipher string is: ' + encode_string())
    elif option == 2:
        print('The original string is: ' + decode_string())
    else:
        print('\nThe entered option is wrong')