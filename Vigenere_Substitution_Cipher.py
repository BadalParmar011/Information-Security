import string
main = string.ascii_lowercase

while True:
    print(
            '\n Assignment 5 Cryptography: Select the Choice for further analysis: ..\n [*] Press 1 for Encryption \n [*] Press 2 for Decryption \n [*] Press 01 to exit.. \n\n')
    print(' Encryption/Decryption using Vigenere Substitution Cipher! ')
    option = input(' Insert Here : ')
    if option == '1':
        def conversion(plain_text, key):
            index = 0
            cipher_text = ""

            # convert into lower case
            plain_text = plain_text.lower()
            key = key.lower()

            # For generating key, the given keyword is repeated
            # in a circular manner until it matches the length of
            # the plain text.
            for c in plain_text:
                if c in main:
                    # to get the number corresponding to the alphabet
                    off = ord(key[index]) - ord('a')

                    # implementing algo logic here
                    encrypt_num = (ord(c) - ord('a') + off) % 26
                    encrypt = chr(encrypt_num + ord('a'))

                    # adding into cipher text to get the encrypted message
                    cipher_text += encrypt

                    # for cyclic rotation in generating key from keyword
                    index = (index + 1) % len(key)
                # to not to change spaces or any other special
                # characters in their positions
                else:
                    cipher_text += c

            print("\n ORIGINAL PLAIN MESSAGE: ", plain_text)
            print(" CIPHER ENCRYPTED MESSAGE: ", cipher_text )

        plain_text = input(" Enter the message to be Encrypted: ")
        key = input(" Enter the key for encryption: ")

        # calling function
        conversion(plain_text, key)

    elif option == '2':
        def Decryption(cipher_text, key):
            index = 0
            plain_text = ""

            # convert into lower case
            cipher_text = cipher_text.lower()
            key = key.lower()

            for c in cipher_text:
                if c in main:
                    # to get the number corresponding to the alphabet
                    off = ord(key[index]) - ord('a')

                    positive_off = 26 - off
                    decrypt = chr((ord(c) - ord('a') + positive_off) % 26 + ord('a'))

                    # adding into plain text to get the decrypted messag
                    plain_text += decrypt

                    # for cyclic rotation in generating key from keyword
                    index = (index + 1) % len(key)
                else:
                    plain_text += c

            print("\n ORIGINAL ENCRYPTED MESSAGE: ", cipher_text)
            print(" PLAIN DECRYPTED MESSAGE: ", plain_text)


        cipher_text = input(" Enter the message to be decrypted: ")
        key = input(" Enter the key for decryption: ")

        # calling function
        Decryption(cipher_text, key)

    elif option == '01':
        print('EXITING!!!!')
        break
    else:
        print('Exception error .. \n'
              'Please insert 1, 2 or 01 ')