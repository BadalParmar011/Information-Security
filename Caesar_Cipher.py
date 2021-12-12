def Encryption(plaintext, key_val):
    ciphertext = ''
    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()
        if new_special == " ":
            ciphertext += ' '
        elif special.isalpha():
            ciphertext += chr((ord(new_special) + key_val - 97) % 26 + 97)
    return ciphertext
def Decryption(ciphertext, key_val):
    plaintext = ''
    for i in range(len(ciphertext)):
        special = ciphertext[i]
        new_special = special.lower()
        if new_special == " ":
            plaintext += ' '
        elif special.isalpha():
            plaintext += chr((ord(new_special) - key_val - 97) % 26 + 97)
    return plaintext
while True:
    print(
        'Assignment 2 Cryptography: Select the Choice for further analysis: ..\n [*] Press 1 for Encryption \n [*] Press 0 for Decryption \n [*] Press 01 to exit.. ')
    print('Encryption/Decryption with shift value of your choice ! ')
    choice = input('Insert Here : ')
    if choice.isdigit():
        if choice == '1':
            sen = input('Insert the PlainText : ')
            key = int(input('Insert Shift Value(Only integer values)/KEY : '))
            
            print(f'Your CipherText => {Encryption(sen, key)}')
            
            print('Special symbols (!,# etc and numbers) are deleted..')
            con = input('Press any integer to continue, NO to Exiting!!')
            if con == 'NO':
                print('Exiting..')
                break
            else:
                pass
        elif choice == '0':
            csen = input('Insert the CipherText : ')
            key = int(input('Insert Shift Value(Only integer values)/KEY : '))
            
            print(f'Your PlainText => {Decryption(csen, key)}')
        
            print('Special symbols (!,# etc and numbers) are deleted!')
            con = input('Press any integer to continue, NO to Exiting!! ')
            if con == 'NO':
                print('Exiting..')
                break
            else:
                pass
        elif choice == '01':
            print('Code Execution Completed!')
            break
        else:
            print('Exception error .. \n'
                  'Please insert 0 or 1 ')
