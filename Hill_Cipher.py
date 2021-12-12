import string

main = string.ascii_lowercase

while True:
    print(
            '\n Assignment 7 Cryptography: Select the Choice for further analysis: ..\n [*] Press 1 for Encryption \n [*] Press 2 for Decryption \n [*] Press 01 to exit.. \n\n')
    print(' Encryption/Decryption using Hill Cipher! ')
    option = input(' Insert Here : ')
    if option == '1':
        def generate_key(n, s):
            s = s.replace(" ", "")
            s = s.lower()

            key_matrix = ['' for i in range(n)]
            i = 0;
            j = 0
            for c in s:
                if c in main:
                    key_matrix[i] += c
                    j += 1
                    if (j > n - 1):
                        i += 1
                        j = 0
            print("The key matrix " + "(" + str(n) + 'x' + str(n) + ") is:")
            print(key_matrix)

            key_num_matrix = []
            for i in key_matrix:
                sub_array = []
                for j in range(n):
                    sub_array.append(ord(i[j]) - ord('a'))
                key_num_matrix.append(sub_array)

            for i in key_num_matrix:
                print(i)
            return (key_num_matrix)


        def message_matrix(s, n):
            s = s.replace(" ", "")
            s = s.lower()
            final_matrix = []
            if (len(s) % n != 0):
                # z is the bogus word
                while (len(s) % n != 0):
                    s = s + 'z'
            print("Converted plain_text for encryption: ", s)
            for k in range(len(s) // n):
                message_matrix = []
                for i in range(n):
                    sub = []
                    for j in range(1):
                        sub.append(ord(s[i + (n * k)]) - ord('a'))
                    message_matrix.append(sub)
                final_matrix.append(message_matrix)
            print("The column matrices of plain text in numbers are:  ")
            for i in final_matrix:
                print(i)
            return (final_matrix)


        # Function to get cofactor of
        # mat[p][q] in temp[][]
        # passing the key matrix as 'mat' to check for invertibility
        def getCofactor(mat, temp, p, q, n):
            i = 0
            j = 0

            # Looping for each element
            # of the matrix
            for row in range(n):
                for col in range(n):

                    # Copying into temporary matrix only those element
                    # which are not in given row and column
                    if (row != p and col != q):
                        temp[i][j] = mat[row][col]
                        j += 1

                        # Row is filled, so increase
                        # row index and reset col index
                        if (j == n - 1):
                            j = 0
                            i += 1


        # Recursive function for finding determinant of matrix.
        # n is current dimension of mat[][].
        def determinantOfMatrix(mat, n):
            D = 0  # Initialize result

            # Base case : if matrix
            # contains single element
            if (n == 1):
                return mat[0][0]

                # To store cofactors
            temp = [[0 for x in range(n)]
                    for y in range(n)]

            sign = 1  # To store sign multiplier

            # Iterate for each
            # element of first row
            for f in range(n):
                # Getting Cofactor of mat[0][f]
                getCofactor(mat, temp, 0, f, n)
                D += (sign * mat[0][f] *
                      determinantOfMatrix(temp, n - 1))

                # terms are to be added with alternate sign
                sign = -sign
            return D


        def isInvertible(mat, n):
            if (determinantOfMatrix(mat, n) != 0):
                return True
            else:
                return False


        def multiply_and_convert(key, message):
            # multiplying matrices
            # resultant must have:
            # rows = numbers of rows in message matrix
            # columns = number of columns in key matrix
            res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]

            for i in range(len(key)):
                for j in range(len(message[0])):
                    for k in range(len(message)):
                        # resulted number matrix
                        res_num[i][j] += key[i][k] * message[k][j]

            res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
            # getting the alphabets from the numbers
            # according to the logic of hill ciipher
            for i in range(len(key)):
                for j in range(len(message[0])):
                    # resultant alphabet matrix
                    res_alpha[i][j] += chr((res_num[i][j] % 26) + 97)

            return (res_alpha)


        # implementing all logic and calling function
        n = int(input("What will be the order of square matrix: "))
        s = input("Enter the key: ")
        key = generate_key(n, s)

        # check for invertability here
        if (isInvertible(key, len(key))):
            print("Yes it is invertable and can be decrypted")
        else:
            print("No it is not invertable and cannot be decrypted")

        plain_text = input("Enter the message: ")
        message = message_matrix(plain_text, n)
        final_message = ''
        for i in message:
            sub = multiply_and_convert(key, i)
            for j in sub:
                for k in j:
                    final_message += k
        print("plain message: ", plain_text)
        print("final encrypted message: ", final_message)
    elif option == '2':
        import string
        import numpy as np

        main = string.ascii_lowercase


        def generate_key(n, s):
            s = s.replace(" ", "")
            s = s.lower()

            key_matrix = ['' for i in range(n)]
            i = 0;
            j = 0
            for c in s:
                if c in main:
                    key_matrix[i] += c
                    j += 1
                    if (j > n - 1):
                        i += 1
                        j = 0
            print("The key matrix " + "(" + str(n) + 'x' + str(n) + ") is:")
            print(key_matrix)

            key_num_matrix = []
            for i in key_matrix:
                sub_array = []
                for j in range(n):
                    sub_array.append(ord(i[j]) - ord('a'))
                key_num_matrix.append(sub_array)

            for i in key_num_matrix:
                print(i)
            return (key_num_matrix)


        def modInverse(a, m):
            a = a % m;
            for x in range(1, m):
                if ((a * x) % m == 1):
                    return x
            return 1


        def method(a, m):
            if (a > 0):
                return (a % m)
            else:
                k = (abs(a) // m) + 1
            return method(a + k * m, m)


        def message_matrix(s, n):
            s = s.replace(" ", "")
            s = s.lower()
            final_matrix = []
            if (len(s) % n != 0):
                # may be negative also
                for i in range(abs(len(s) % n)):
                    # z is the bogus word
                    s = s + 'z'
            print("Converted cipher_text for decryption: ", s)
            for k in range(len(s) // n):
                message_matrix = []
                for i in range(n):
                    sub = []
                    for j in range(1):
                        sub.append(ord(s[i + (n * k)]) - ord('a'))
                    message_matrix.append(sub)
                final_matrix.append(message_matrix)
            print("The column matrices of plain text in numbers are:  ")
            for i in final_matrix:
                print(i)
            return (final_matrix)


        def multiply_and_convert(key, message):

            # multiplying matrices
            # resultant must have:
            # rows = numbers of rows in message matrix
            # columns = number of columns in key matrix
            res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]

            for i in range(len(key)):
                for j in range(len(message[0])):
                    for k in range(len(message)):
                        # resulted number matrix
                        res_num[i][j] += key[i][k] * message[k][j]

            res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
            # getting the alphabets from the numbers
            # according to the logic of hill ciipher
            for i in range(len(key)):
                for j in range(len(message[0])):
                    # resultant alphabet matrix
                    res_alpha[i][j] += chr((res_num[i][j] % 26) + 97)

            return (res_alpha)


        n = int(input("What will be the order of square matrix: "))
        s = input("Enter the key: ")
        key_matrix = generate_key(n, s)
        A = np.array(key_matrix)
        det = np.linalg.det(A)
        adjoint = det * np.linalg.inv(A)

        if (det != 0):
            convert_det = modInverse(int(det), 26)
            adjoint = adjoint.tolist()
            print("Adjoint Matrix before modulo26 operation: ")
            for i in adjoint:
                print(i)
            print(convert_det)

            # applying modulo 26 to all elements in adjoint matrix
            for i in range(len(adjoint)):
                for j in range(len(adjoint[i])):
                    adjoint[i][j] = round(adjoint[i][j])
                    adjoint[i][j] = method(adjoint[i][j], 26)
            print("Adjoint Matrix after modulo26 operation: ")
            for i in adjoint:
                print(i)

            # modulo is applied to inverse of determinant and
            # multiplied to all elements in the adjoint matrix
            # to form inverse matrix
            adjoint = np.array(adjoint)
            inverse = convert_det * adjoint

            inverse = inverse.tolist()
            for i in range(len(inverse)):
                for j in range(len(inverse[i])):
                    inverse[i][j] = inverse[i][j] % 26

            print("Inverse matrix after applying modulo26 operation: ")
            for i in inverse:
                print(i)

            cipher_text = input("Enter the cipher text: ")
            message = message_matrix(cipher_text, n)
            plain_text = ''
            for i in message:
                sub = multiply_and_convert(inverse, i)
                for j in sub:
                    for k in j:
                        plain_text += k

            print("plain message: ", plain_text)
        else:
            print("Matrix cannot be inverted")
    elif option == '01':
        print('EXITING!!!!')
        break
    else:
        print('Exception error .. \n'
              'Please insert 1, 2 or 01 ')