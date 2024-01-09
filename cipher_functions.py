import re 

def find_index(plaintext, x, letters):
    """
    Finds and returns the index of every letter in a given string.

    Arguments: 
    (string) plaintext: the text the user wants to encrypt/decrypt
    (int) x: index value
    (list) letters: the alphabet

    Returns:
    (tuple) index: the span of the letter
    """

    pattern = re.compile(plaintext[x])
    #print(pattern)
    result = pattern.search("".join(letters))
    #print(result)
    index = result.span()
    #print(index)
    return index

def write_to_file(altered_text):
    """
    Writes encrypted/decrypted text to a file. 

    Arguments:
    (string) altered_text: the encrypted or decrypted text

    Returns:
    nothing
    """
    with open("cipher_results.txt", "w") as file_connection:
        file_connection.write(altered_text)