# gives me a dictionary of english words
def load_words(filename = "words.txt"):
    """Loads words from a text file into a Python list."""
    with open(filename, "r") as file:
        # Create a list by reading each line, stripping whitespace
        word_list = [line.strip() for line in file]
    return word_list

# caesar cipher
def encrypt(text, shift):
    cipher = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        count = 0
        for letter in alphabet:
            if char == letter:
                newPos = count + shift
                
                if newPos > 25:
                    newPos = newPos - 26

                cipher += alphabet[newPos]
            else:
                count += 1
    text = cipher
    print(text)

def decrypt(text, shift):
    cipher = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        count = 0
        for letter in alphabet:
            if char == letter:
                newPos = count - shift
                
                if newPos < 0:
                    newPos = newPos + 26

                cipher += alphabet[newPos]
            else:
                count += 1
    text = cipher
    print(text)

# decrypt caesar cipher without knowing key
# def decipher(text):
#     for shift in range(26):
#         count = 0
#         for char in text:
#             if count = 3

#             count += 1


encrypt("haha, decipher this", 5)

decrypt("mfmfijhnumjwymnx", 5)