from algorithms import atbash, bellaso, cesar, columnar_transposition, playfar_cipher

option = 0
print('\nClassic encryption algorithms\n')
while option == 0:
    print('1. The ATBASH cipher\n')
    print('2. The Caesar cipher\n')
    print('3. Bellaso cipher\n')
    print('4. The Playfair cipher\n')
    print('5. Simple column transpose cipher\n')
    print('6. Exit\n')
    option = int(input('Choose an option: '))
    if option == 1:
        atbash.main()
    elif option == 2:
        cesar.main()
    elif option == 3:
        bellaso.main()
    elif option == 4:
        playfar_cipher.main()
    elif option == 5:
        columnar_transposition.main()
    elif option == 6:
        exit()
    else:
        print('Choose a correct option')
        option = 0