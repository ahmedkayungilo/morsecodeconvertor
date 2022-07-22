from converter import MorseCodeConverter

my_converter = MorseCodeConverter()  # Create a convertor

while my_converter._another:  # Continuous looping so long as a new sentence is to be converted
    my_converter.initial()
    sentence = my_converter.prompt()
    my_converter.convert(sentence)

    print(my_converter._sentence + "\n")  # Print out the coded message

    if input(my_converter._CONFIRMATION_MESSAGE) == 'n':  # Ask for a new message if available
        another = False