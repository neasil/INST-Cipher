# User Requirements:
# 1. Create Ceaser Cipher for ASCII characters 
# 2. User should be able to provide one or more strings
# 3. Program should return either an encrypted or decrypted text
# 4. The user should be able to modify the size of the shift

# Outline:
# 1. Prompt user to input plaintext, size of the shift, which way to shift, and whether they want to encrypt or decrypt
# 2. Create a list to represent the alphabet 
# 3. Use for loop to iterate through plaintext and identify indexes of each letter in plaintext
# 4. Using the extracted indexes, shift size, and shift direction, calculate the corresponding indexes in the alphabet for each encrypted/decrypted letter
# 5. Locate the new letters using these calculated indexes
# 6. Append each new letter to an empty array to represent the encrypted/decrypted text
# 7. Print out result to user
# 8. Write result to file. 

# Import statements:
import numpy as np
import sys
from cipher_functions import find_index, write_to_file

# Create alphabet for future reference:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Opening the program:
print("Welcome! This program acts as a Ceaser Cipher. Every piece of text that you encrypt or decrypt will be automatically written to a file called 'cipher_results.txt'. That is, unless you choose to input text from a file.")
print("You have several options for how you'd like to enter your inputs. \n\nYou may enter 1. command line arguments 2. a file with plaintext 3. manual inputs.")

# Prompting the user if they would like to continue:
play = input("In that case, would you like to begin? You may continuously use the program, unless you choose to enter a .txt file. Enter 'yes' to continue or 'no' to quit whenever prompted to.\t").replace(" ", "").lower()

if play == "yes":
    while play == "yes":

        # Letting the user select which input method they would like to use
        input_method = input("Which method would you like to use? To use command line arguments enter 'command', to use a file enter 'file', to use user input enter 'input'.\t").lower()

        # Checking the input method
        if input_method != "command" and input_method != "file" and input_method != "input":
            input_method = input("Please enter either 'command', 'file', or 'input'.\t").lower()
            if input_method != "command" and input_method != "file" and input_method != "input":
                print("You have failed to enter a valid input method. The program will now close")
                exit()

        # If the user chooses to enter inputs at the command line:
        if input_method == "command":
            
            # Checking inputs:
            # Plaintext: 
            try:
                text = sys.argv[1].replace(",", "").lower()
            except IndexError:
                text = input("Please enter a plaintext.\t").lower()
                # Checking for inputs that contain numbers 
                if text.isnumeric() == True:
                    text = input("I cannot encrypt/decrypt a plaintext that contains numbers. Please reenter your plaintext so it only has characters.\t").lower()
                    if text.isnumeric() == True:
                        print("You've failed to enter a valid plaintext. The program will now close.")
                        exit()
        
            # Checking for inputs that contain numbers 
            if text.isnumeric() == True:
                text = input("I cannot encrypt/decrypt a plaintext that contains numbers. Please reenter your plaintext so it only has characters.\t").lower()
                if text.isnumeric() == True:
                    print("You've failed to enter a valid plaintext. The program will now close.")
                    exit()

            # Shift direction: 
            try: 
                shift = sys.argv[2].replace(",", "").lower()
            except IndexError:
                shift = input("Please enter a shift direction.\t").lower()
                # Checking for inputs that aren't 'left' or 'right'
                if shift != "left" and shift != "right":
                    shift = input("You must enter either 'left' or 'right' to indicate your shift direction. Please try again.\t").lower()
                    if shift != "left" and shift != "right":
                        print("You have failed to enter a valid shift direction. The program will now close.")
                        exit()

            # Checking for inputs that aren't 'left' or 'right'
            if shift != "left" and shift != "right":
                shift = input("You must enter either 'left' or 'right' to indicate your shift direction. Please try again.\t").lower()
                if shift != "left" and shift != "right":
                    print("You have failed to enter a valid shift direction. The program will now close.")
                    exit()

            # Shift size: 
            try: 
                shift_size = sys.argv[3].replace(",", "")
            except IndexError:
                shift_size = input("Please enter a shift size.\t")
                # Checking for inputs that aren't numbers 
                if shift_size.isnumeric() == False: # isnumeric(): https://www.w3schools.com/python/ref_string_isnumeric.asp
                    shift_size = input("You must enter an integer to indicate your shift size. Please try again.\t")
                    if shift_size.isnumeric() == False:
                        print("You have failed to enter a valid shift size. The program will now close.")
                        exit()

            # Checking for inputs that aren't numbers 
            if shift_size.isnumeric() == False: 
                shift_size = input("You must enter an integer to indicate your shift size. Please try again.\t")
                if shift_size.isnumeric() == False:
                    print("You have failed to enter a valid shift size. The program will now close.")
                    exit()
    
            # Encryption/decryption
            try: 
                encrypt_decrypt = sys.argv[4].replace(",", "").lower()
            except IndexError:
                encrypt_decrypt = input("Please enter whether or not you'd like to encrypt or decrypt your plaintext.\t").lower()
                # Checking for inputs that aren't 'encrypt' or 'decrypt'
                if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                    encrypt_decrypt = input("You must enter either 'encrypt' or 'decrypt' to indicate whether you'd like to encrypt or decrypt your text. Please try again.\t").lower()
                    if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                        print("You failed to properly indicate whether you wanted to encrypt or decrypt your plaintext. The program will now close.")
                        exit()

            # Checking for inputs that aren't 'encrypt' or 'decrypt'
            if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                encrypt_decrypt = input("You must enter either 'encrypt' or 'decrypt' to indicate whether you'd like to encrypt or decrypt your text. Please try again.\t").lower()
                if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                    print("You failed to properly indicate whether you wanted to encrypt or decrypt your plaintext. The program will now close.")
                    exit()

        # If the user chooses to enter inputs from a file:
        elif input_method == "file":
            
            # Prompting user to enter a file path
            file_path = input("Please enter a file path to a simple .txt file: \t")

            # Checking the file 
            try: 
                with open(file_path, "r") as file_connect:
                    parsed_text = file_connect.readlines()
            except FileNotFoundError:
                print("This file does not exist.")
                exit()
            except TypeError:
                print("You've entered a file with invalid contents. You must enter a .txt that can be encrypted or decrypted.")
                exit()
            except IOError:
                print("Sorry, I can't open this file.")
                exit()
            
            # Plaintext: text file contents converted to list of words
            text = ""
            for i in range(len(parsed_text)):
                line = parsed_text[i].replace("\\n\\", "").replace(" ", "").replace(".", "").replace(",", "").replace("'", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("(", "").replace(")", "").replace("-", "").lower().split() 
                text = np.append(text, line)

            # User inputs
            inputs = input("Now, in this order, please enter the direction of your shift, the size of your shift as an integer, and if you'd like to encrypt or decrypt the string, please enter either 'encrypt' or 'decrypt' respectively. Each input should be separated with a space. ").replace(".", "").replace(",", "").lower().split()

            # Checking inputs:
            # Shift direction:
            try:
                shift = inputs[0]
            except IndexError:
                shift = input("Please enter a shift direction.\t").lower()
                # Checking for inputs that aren't 'left' or 'right'
                if shift != "left" and shift != "right":
                    shift = input("You must enter either 'left' or 'right' to indicate your shift direction. Please try again.\t").lower()
                    if shift != "left" and shift != "right":
                        print("You have failed to enter a valid shift direction. The program will now close.")
                        exit()

            # Checking for inputs that aren't 'left' or 'right'
            if shift != "left" and shift != "right":
                shift = input("You must enter either 'left' or 'right' to indicate your shift direction. Please try again.\t").lower()
                if shift != "left" and shift != "right":
                    print("You have failed to enter a valid shift direction. The program will now close.")
                    exit()

            # Shift size:
            try:
                shift_size = inputs[1]
            except IndexError:
                shift_size = input("Please enter a shift size.\t")
                # Checking for inputs that aren't numbers 
                if shift_size.isnumeric() == False: 
                    shift_size = input("You must enter an integer to indicate your shift size. Please try again.\t")
                    if shift_size.isnumeric() == False:
                        print("You have failed to enter a valid shift size. The program will now close.")
                        exit()

            # Checking for inputs that aren't numbers 
            if shift_size.isnumeric() == False: 
                shift_size = input("You must enter an integer to indicate your shift size. Please try again.\t")
                if shift_size.isnumeric() == False:
                    print("You have failed to enter a valid shift size. The program will now close.")
                    exit()
    
            # Encryption/decryption: 
            try: 
                encrypt_decrypt = inputs[2]
            except IndexError:
                encrypt_decrypt = input("Please enter whether or not you'd like to encrypt or decrypt your plaintext.\t")
                # Checking for inputs that aren't 'encrypt' or 'decrypt'
                if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                    encrypt_decrypt = input("You must enter either 'encrypt' or 'decrypt' to indicate whether you'd like to encrypt or decrypt your text. Please try again.\t").lower()
                    if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                        print("You failed to properly indicate whether you wanted to encrypt or decrypt your plaintext. The program will now close.")
                        exit()

            # Checking for inputs that aren't 'encrypt' or 'decrypt'
            if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                encrypt_decrypt = input("You must enter either 'encrypt' or 'decrypt' to indicate whether you'd like to encrypt or decrypt your text. Please try again.\t").lower()
                if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                    print("You failed to properly indicate whether you wanted to encrypt or decrypt your plaintext. The program will now close.")
                    exit()
    
            # Storing encrypted/decrypted words in a list
            gather_words = ""

            for i in range(len(text)): # iterates through all the words of the entire list 
                # What happens for every single word
                if encrypt_decrypt == "encrypt":
                    # What happens when the user chooses to encrypt their inputted plaintext
                    if shift == "left":
                        # What happens when the user chooses to shift left 
                        encrypted_word = ""
                        for idx in range(len(text[i])):
                            # Iterating through every letter in the plaintext to find its index
                            index = find_index(text[i], idx, alphabet)
                            new_index = index[0] - int(shift_size)
                            if new_index < 0: # Accounting for possible 'out of bounds' shift sizes
                                index[0] + (len(alphabet) - int(shift_size))
                            new_letter = alphabet[new_index]
                            encrypted_word = "".join(np.append(encrypted_word, new_letter))
                        # Appending resulting text 
                        gather_words = np.append(gather_words, encrypted_word)
                    elif shift == "right":
                        # What happens when the user chooses to shift right 
                        encrypted_word = ""
                        for idx in range(len(text[i])):
                            # Iterating through every letter in the plaintext to find its index
                            index = find_index(text[i], idx, alphabet)
                            new_index = index[0] + int(shift_size)
                            if new_index > 24: # Accounting for possible 'out of bounds' shift sizes
                                new_index = index[0] - (len(alphabet) - int(shift_size))
                            encrypted_word = "".join(np.append(encrypted_word, new_letter))
                        # Appending resulting text
                        gather_words = np.append(gather_words, encrypted_word)
                elif encrypt_decrypt == "decrypt": 
                    # What happens when the user chooses to decrypt their inputted plaintext
                    if shift == "left":
                        # What happens when the user chooses to shift left 
                        decrypted_word = ""
                        for idx in range(len(text[i])):
                            # Iterating through every letter in the plaintext to find its index
                            index = find_index(text[i], idx, alphabet)
                            new_index = index[0] + int(shift_size)
                            if new_index > 24: # Accounting for possible 'out of bounds' shift sizes
                                new_index = index[0] - (len(alphabet) - int(shift_size))
                            new_letter = alphabet[new_index]
                            decrypted_word = "".join(np.append(decrypted_word, new_letter))
                        # Appending resulting text 
                        gather_words = np.append(gather_words, decrypted_word)
                    elif shift == "right":
                        # What happens when the user chooses to shift right 
                        decrypted_word = ""
                        for idx in range(len(text[i])):
                            # Iterating through every letter in the plaintext to find its index
                            index = find_index(text[i], idx, alphabet)
                            new_index = index[0] - int(shift_size)
                            if new_index < 0: # Accounting for possible 'out of bounds' shift sizes
                                new_index = index[0] + (len(alphabet) - int(shift_size))
                            new_letter = alphabet[new_index]
                            decrypted_word = "".join(np.append(decrypted_word, new_letter))
                        # Appending resulting text 
                        gather_words = np.append(gather_words, decrypted_word)
    
            # Outputting the final text to the user 
            final_text = " ".join(gather_words)
            print(final_text)

            # Appending text to the given .txt file: https://www.scaler.com/topics/append-to-file-python/
            file = open(file_path, "a")
            file.write(final_text)
            file.close()

            # Closing the program
            print("The program will now close.")
            exit()
        
        # If the user chooses the enter their own inputs:
        elif input_method == "input":

            # Prompting user to enter inputs:
            inputs = input("In this order, please enter a string, the direction of your shift, the size of your shift as an integer, and if you'd like to encrypt or decrypt the string, please enter either 'encrypt' or 'decrypt' respectively. Each input should be separated with a space. ").replace(",", "").lower().split()

            # Checking inputs: 
            # Plaintext: 
            try: 
                text = inputs[0]
            except IndexError:
                text = input("Please enter a plaintext.\t").lower()
                # Checking for inputs that contain numbers 
                if text.isnumeric() == True:
                    text = input("I cannot encrypt/decrypt a plaintext that contains numbers. Please reenter your plaintext so it only has characters.\t").lower()
                    if text.isnumeric() == True:
                        print("You've failed to enter a valid plaintext. The program will now close.")
                        exit()

            # Checking for inputs that contain numbers 
            if text.isnumeric() == True:
                text = input("I cannot encrypt/decrypt a plaintext that contains numbers. Please reenter your plaintext so it only has characters.\t").lower()
                if text.isnumeric() == True:
                    print("You've failed to enter a valid plaintext. The program will now close.")
                    exit()

            # Shift direction:
            try:
                shift = inputs[1]
            except IndexError:
                shift = input("Please enter a shift direction.\t").lower()
                # Checking for inputs that aren't 'left' or 'right'
                if shift != "left" and shift != "right":
                    shift = input("You must enter either 'left' or 'right' to indicate your shift direction. Please try again.\t").lower()
                    if shift != "left" and shift != "right":
                        print("You have failed to enter a valid shift direction. The program will now close.")
                        exit()
  
            # Checking for inputs that aren't 'left' or 'right'
            if shift != "left" and shift != "right":
                shift = input("You must enter either 'left' or 'right' to indicate your shift direction. Please try again.\t").lower()
                if shift != "left" and shift != "right":
                    print("You have failed to enter a valid shift direction. The program will now close.")
                    exit()
    
            # Shift size:
            try:
                shift_size = inputs[2]
            except IndexError:
                shift_size = input("Please enter a shift size.\t")
                # Checking for inputs that aren't numbers 
                if shift_size.isnumeric() == False:
                    shift_size = input("You must enter an integer to indicate your shift size. Please try again.\t")
                    if shift_size.isnumeric() == False:
                        print("You have failed to enter a valid shift size. The program will now close.")
                        exit()

            # Checking for inputs that aren't numbers 
            if shift_size.isnumeric() == False:
                shift_size = input("You must enter an integer to indicate your shift size. Please try again.\t")
                if shift_size.isnumeric() == False:
                    print("You have failed to enter a valid shift size. The program will now close.")
                    exit()
    
            # Encryption/decryption:
            try:
                encrypt_decrypt = inputs[3]
            except IndexError: 
                encrypt_decrypt = input("Please enter whether or not you'd like to encrypt or decrypt your plaintext.\t").lower()
                # Checking for inputs that aren't 'encrypt' or 'decrypt'
                if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                    encrypt_decrypt = input("You must enter either 'encrypt' or 'decrypt' to indicate whether you'd like to encrypt or decrypt your text. Please try again.\t").lower()
                    if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                        print("You failed to properly indicate whether you wanted to encrypt or decrypt your plaintext. The program will now close.")
                        exit()

            # Checking for inputs that aren't 'encrypt' or 'decrypt'
            if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                encrypt_decrypt = input("You must enter either 'encrypt' or 'decrypt' to indicate whether you'd like to encrypt or decrypt your text. Please try again.\t").lower()
                if encrypt_decrypt != "encrypt" and encrypt_decrypt != "decrypt":
                    print("You failed to properly indicate whether you wanted to encrypt or decrypt your plaintext. The program will now close.")
                    exit()

        # Encrypting and decrypting: 
        if encrypt_decrypt == "encrypt":
            # What happens when the user chooses to encrypt their inputted plaintext
            if shift == "left":
                # What happens when the user chooses to shift left 
                encrypted_text = ""
                for i in range(len(text)):
                    # Iterating through every letter in the plaintext to find its index
                    index = find_index(text, i, alphabet)
                    new_index = index[0] - int(shift_size)
                    if new_index < 0: # Accounting for possible 'out of bounds' shift sizes
                        new_index = index[0] + (len(alphabet) - int(shift_size))
                    new_letter = alphabet[new_index]
                    encrypted_text = "".join(np.append(encrypted_text, new_letter))
                    # Writing the resulting text to a file
                    write_to_file(encrypted_text)
                print(text + " has been encrypted to " + encrypted_text)  
            elif shift == "right":
                # What happens when the user chooses to shift right 
                encrypted_text = ""
                for i in range(len(text)):
                    # Iterating through every letter in the plaintext to find its index
                    index = find_index(text, i, alphabet)
                    new_index = index[0] + int(shift_size)
                    if new_index > 24: # Accounting for possible 'out of bounds' shift sizes
                        new_index = index[0] - (len(alphabet) - int(shift_size))
                    new_letter = alphabet[new_index]
                    encrypted_text = "".join(np.append(encrypted_text, new_letter))
                    # Writing the resulting text to a file
                    write_to_file(encrypted_text)
                print(text + " has been encrypted to " + encrypted_text)   
        elif encrypt_decrypt == "decrypt": 
            # What happens when the user chooses to decrypt their inputted plaintext
            if shift == "left":
                # What happens when the user chooses to shift left 
                decrypted_text = ""
                for i in range(len(text)):
                    # Iterating through every letter in the plaintext to find its index
                    index = find_index(text, i, alphabet)
                    new_index = index[0] + int(shift_size)
                    if new_index > 24: # Accounting for possible 'out of bounds' shift sizes
                        new_index = index[0] - (len(alphabet) - int(shift_size))
                    new_letter = alphabet[new_index]
                    decrypted_text = "".join(np.append(decrypted_text, new_letter))
                    # Writing the resulting text to a file
                    write_to_file(decrypted_text)
                print(text + " has been decrypted to " + decrypted_text) 
            elif shift == "right":
                # What happens when the user chooses to shift right 
                decrypted_text = ""
                for i in range(len(text)):
                    # Iterating through every letter in the plaintext to find its index
                    index = find_index(text, i, alphabet)
                    new_index = index[0] - int(shift_size)
                    if new_index < 0: # Accounting for possible 'out of bounds' shift sizes
                        new_index = index[0] + (len(alphabet) - int(shift_size))
                    new_letter = alphabet[new_index]
                    decrypted_text = "".join(np.append(decrypted_text, new_letter))
                    # Writing the resulting text to a file
                    write_to_file(decrypted_text)
                print(text + " has been decrypted to " + decrypted_text) 
    
        play = input("Would you like to continue? Please enter 'yes' or 'no'.\t").lower()

elif play == "no":
    print("You have chosen to quit.")
    exit()
else: 
    print("It seems you've entered an invalid input. The program will close automatically.")
    exit()

