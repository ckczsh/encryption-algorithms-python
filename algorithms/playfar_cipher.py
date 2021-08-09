#Playfar cipher
#Author: Julio Aviña

#global vars
user_string = ''
key_us = ''
enconded_matrix = []
encoded_string = ''
decoded_string = ''

def set_matrix():
    global enconded_matrix
    global key_us
    #build list alphabet with key
    list_alphabet = list()
    for letter_key in key_us:
        if letter_key not in list_alphabet:
            if letter_key == 'j':
                list_alphabet.append('i')
            else:
                list_alphabet.append(letter_key)
    print(list_alphabet)
    #Complete the list alphabet
    flag = 0
    for char_alphabet in range(97 , 123): #ASCII a-z
        if chr(char_alphabet) not in list_alphabet:
            if char_alphabet == 105 and chr(106) not in list_alphabet:
                list_alphabet.append("i")
                flag = 1
            elif flag == 0 and char_alphabet == 105 or char_alphabet == 106:
                pass    
            else:
                list_alphabet.append(chr(char_alphabet))
    print(list_alphabet)
    index_matrix = 0
    #init matrix
    auxiliar_matrix = [[0 for i in range(5)] for j in range(5)] 
    print(auxiliar_matrix)
    for i in range(0, 5):
        for j in range(0, 5):
            auxiliar_matrix[i][j] = list_alphabet[index_matrix]
            index_matrix += 1
    enconded_matrix = auxiliar_matrix
    print(enconded_matrix)
    
#get the coords
def get_location_of_char_in_matrix(char_string): 
    list_of_char = list()
    if char_string == 'j':
        char_string = 'i'
    for index_column ,column in enumerate(enconded_matrix):
        for index_row, row in enumerate(column):
            if char_string == row:
                list_of_char.append(index_column)
                list_of_char.append(index_row)
                return list_of_char
    

#set user string
def set_user_string(entered_user_string):
    global user_string
    user_string = entered_user_string.lower().replace(" ", "")

#set user key
def set_user_key(user_key):
    global key_us
    key_us = user_key.lower().replace(" ", "")

#encode string   
def encode_string():
    global user_string
    global encoded_string
    set_user_string(input('Enter the string to cipher: '))
    set_user_key(input('Enter the key: '))
    set_matrix()
    #if it has repeating characters then
    for index in range(0, len(user_string) + 1, 2):
        if index < len(user_string) - 1:
            if user_string[index] == user_string[index + 1]:
                user_string = user_string[:index + 1] + 'x' + user_string[index + 1:]
    #if it is not even, we will complete it    
    if len(user_string) % 2 != 0:
        user_string = user_string[:] + 'x'
    counter = 0
    #by pairs
    while counter < len(user_string):
        letter_1_location = list()
        letter_2_location = list()
        letter_1_location = get_location_of_char_in_matrix(user_string[counter])
        letter_2_location = get_location_of_char_in_matrix(user_string[counter + 1])
        # if the letters are in the same column, then get 1 to the down
        if letter_1_location[1] == letter_2_location[1]:
            encoded_string += str(enconded_matrix[(letter_1_location[0] + 1) % 5 ][letter_1_location[1]]) + str(enconded_matrix[(letter_2_location[0] + 1) %5 ][letter_2_location[1]]) + ' '
        # if the letters are in the same row, then get 1 to the right
        elif letter_1_location[0] == letter_2_location[0]:
            encoded_string += str(enconded_matrix[letter_1_location[0]][(letter_1_location[1] + 1) % 5]) + str(enconded_matrix[letter_2_location[0]][(letter_2_location[1] + 1) % 5]) + ' '
        #otherwise get the opposite diagonal
        else:
            encoded_string += str(enconded_matrix[letter_1_location[0]][letter_2_location[1]])  + str(enconded_matrix[letter_2_location[0]][letter_1_location[1]]) + ' '  
        counter = counter + 2
    return encoded_string
    
def decode_string(): 
    global user_string
    global decoded_string
    set_user_string(input('Enter the string to decipher: '))
    set_user_key(input('Enter the key: '))
    set_matrix()
    counter = 0
    while counter < len(user_string):
        letter_1_location = list(get_location_of_char_in_matrix(user_string[counter]))
        letter_2_location = list(get_location_of_char_in_matrix(user_string[counter + 1]))
        if letter_1_location[1] == letter_2_location[1]:
            decoded_string += str(enconded_matrix[(letter_1_location[0] - 1) % 5 ][letter_1_location[1]]) + str(enconded_matrix[(letter_2_location[0] - 1) %5 ][letter_2_location[1]]) + ' '
        elif letter_1_location[0] == letter_2_location[0]:
            decoded_string += str(enconded_matrix[letter_1_location[0]][(letter_1_location[1] - 1) % 5]) + str(enconded_matrix[letter_2_location[0]][(letter_2_location[1] - 1) % 5]) + ' '  
        else:
            decoded_string += str(enconded_matrix[letter_1_location[0]][letter_2_location[1]])  + str(enconded_matrix[letter_2_location[0]][letter_1_location[1]]) + ' '     
        counter = counter + 2
    decoded_string = decoded_string.rstrip()
    if decoded_string[len(decoded_string) - 1] == 'x':
        decoded_string = decoded_string[:len(decoded_string) - 1]
    return decoded_string
        
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