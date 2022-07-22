class MorseCodeConverter:
    
    # This is a constructor function
    def __init__(self):
        self._MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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
        self._INTRO_MESSAGE = "\n\nThis is an online Morse Code Convertor for the English language. Once prompted a sent" \
                              "ence is expected from you which will be converted into morse code. The separation of " \
                              "words will be five spaces while that of letters within a word will be three spaces.\n\n"

        # This is the prompt message and confirmation sentence
        self._PROMPT_MESSAGE = "Please enter your sentence: "
        self._CONFIRMATION_MESSAGE = "Would you like to convert another message? (y/n): "

        self._another = True  # This is the controller for continuous conversion

        self._sentence = ""

    def initial(self):
        print(self._INTRO_MESSAGE)

    def prompt(self):
        # Returns the sentence that the user enters in upper case inorder to match the morse code dictionary keys 
        return input(self._PROMPT_MESSAGE).upper()
    
    def convert(self, sentence):
        # This method converts the user's sentence into Morse code
        word_list = sentence.split(" ")

        for word in word_list:
            for letter in word:
                letter = self._MORSE_CODE_DICT[letter]  # Convert each letter into Morse code
                self._sentence += letter
                self._sentence += " "  # Add a single space between the letters in a word

            self._sentence += "   "  # Add three space in between words
