# This is the dictionary that contains the normal letters and numbers with their Morse code equivalent
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

# This is the introductory prompt at the beginning of converter execution
INTRO_MESSAGE = "\n\nThis is an online Morse Code Convertor for the English language. Once prompted a sent" \
                "ence is expected from you which will be converted into morse code. The separation of " \
                "words will be five spaces while that of letters within a word will be three spaces.\n\n"

# This is the prompt message and confirmation sentence
PROMPT_MESSAGE = "Please enter your sentence: "
CONFIRMATION_MESSAGE = "Would you like to convert another message? (y/n): "

another = True  # This is the controller for continuous conversion

print(INTRO_MESSAGE)

while another:
    sentence = input(PROMPT_MESSAGE)
    sentence = sentence.upper()  # Convert the sentence into upper case to match morse code dictionary keys

    word_list = sentence.split(" ")

    coded_sentence = ""  # Initial empty string for the coded message

    for word in word_list:
        for letter in word:
            letter = MORSE_CODE_DICT[letter]  # Convert each letter into Morse code
            coded_sentence += letter
            coded_sentence += " "  # Add a single space between the letters in a word

        coded_sentence += "   "  # Add three space in between words

    print(coded_sentence + "\n")  # Print out the coded message

    if input(CONFIRMATION_MESSAGE) == 'n':
        another = False
