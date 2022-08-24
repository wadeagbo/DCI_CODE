def isWordGuessed(secretWord):
    guess = 0
    lettersGuessed = ''
    secretLetters = set(secretWord)
    while guess <= 8:
        letter = input('Enter a letter: ')
        lettersGuessed += letter
        print('Letters guessed so far:', lettersGuessed)
        if letter not in secretLetters:
            guess += 1
        else:
            secretLetters.remove(letter)
            if not secretLetters:
                return True
    return False

secretWord = 'hello'
lettersGuessed = []

isWordGuessed(secretWord,lettersGuessed)

