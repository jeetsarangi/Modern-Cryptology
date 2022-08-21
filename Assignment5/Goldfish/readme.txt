
Files included:
1)Plaintext_Generator.py(Used to generate dummy plaintext for attack)
2)Ciphertext_Generator.py(Used to generate ciphertexts for all plaintexts by connecting to the server)
3)Find_Keys.py(Used to generate the key using the plaintexts and corresponding ciphertexts)
4)Decrypt.py(Used to generate the final password using the key)

Libraries used:
*pyfinite
*numpy
*pandas
*pickle
*os

How to run ?
1)Unzip the folder.
2)Run makefile using command "make attack".
3)The final password to crack will get generated in the terminal.
