def isWordGuessed(secretWord,lettersGuessed):
  guess  = 0
  secretLetters = list(secretWord)
  while guess <= 8:
    secretWordLen = len(secretLetters)
    letter = input('Enter a letter: ')
    lettersGuessed.append(letter)

    print('Letters guessed so far: ',lettersGuessed)

    if letter not in secretLetters:
        guess += 1

    while letter in secretLetters:
        secretLetters.remove(letter)

    if secretLetters == []:
       return True

  return False

secretWord = 'hello'
lettersGuessed = []

isWordGuessed(secretWord,lettersGuessed)

