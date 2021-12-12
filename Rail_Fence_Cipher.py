option=int(input("Enter 1 to encrypt and 2 to decrypt: ")) 
def cipher(clearText, key):
    result = ""
    matrix = [["" for x in range(len(clearText))] for y in range(key)]
    increment = 1
    row = 0
    col = 0
    for c in clearText:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[ row ][ col ] = c
        row += increment
        col += 1
    for list in matrix:
        result += "".join(list)
    return result
def decipher(cipherText, key):
    result = ""
    matrix = [["" for x in range(len(cipherText))] for y in range(key)]
    idx = 0
    increment = 1
    for selectedRow in range(0, len(matrix)):
        row = 0
        for col in range(0, len(matrix[ row ])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += cipherText[idx]
                idx += 1
            row += increment
    matrix = transpose( matrix )
    for list in matrix:
        result += "".join(list)
    return result
def transpose( m ):
    result = [ [ 0 for y in range( len(m) ) ] for x in range( len(m[0]) ) ]
    for i in range( len(m) ):
        for j in range( len(m[0]) ):
            result[ j ][ i ] = m[ i ][ j ]
    return result

if(option==1):        
    clearText =input("Enter String: ")
    key = int(input("Enter Key: "))
    print ("\nOriginal Text: " + clearText)
    cipheredText = cipher(clearText, key)
    print ("Ciphered Text: {0}".format(cipheredText))
else:
    cipherText =input("Enter Cipher string: ")
    key = int(input("Enter Key: "))
    print ("\nOriginal Text: " + cipherText)
    decipherText = decipher(cipherText, key)
    print ("Deciphered Text: {0}".format(decipherText))