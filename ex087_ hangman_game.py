import random

FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = 'formiga babuino bicicleta abacate beterraba geladeira eletrodomestico bebado chocolate giroscopio'.split()


def main():
    global FORCAIMG

    print('F O R C A')
    wrongLetters = ''
    rightLetters = ''
    secretWord = ramdon_word_generator().upper()
    playing = True

    while playing:
        print_game(wrongLetters, rightLetters, secretWord)

        guess = guess_receive(wrongLetters + rightLetters)

        if guess in secretWord:
            rightLetters += guess

            if check_won(secretWord, rightLetters):
                print(f'Exato! A palavra secreta é "{secretWord}"! Você ganhou.')
                playing = False
        else:
            wrongLetters += guess
            if len(wrongLetters) == len(FORCAIMG) - 1:
                print_game(wrongLetters, rightLetters, secretWord)

                print(f'Você excedeu seu limite palpites!'
                      f'\nDepois de {str(len(wrongLetters))} erros e {str(len(rightLetters))} acertos, '
                      f'a palavra era {secretWord}.'
                      f'\nVOCÊ PERDEU!')

                playing = False

        if not playing:
            if play_again() == 'S':
                wrongLetters = ''
                rightLetters = ''
                playing = True
                secretWord = ramdon_word_generator().upper()
            else:
                break



def ramdon_word_generator():
    '''
    Generates a random word from the list "words".
    '''
    global words
    return random.choice(words)


def print_with_spaces(word):
    '''
    Receive a string, word or list and print it with spaces between the letters or strings.
    '''
    for l in word:
        print(l, end = ' ')

    print()


def print_game(wrongLetters, rightLetters, secretWord):
    '''
    Made from the global variable that contains the game images in ASCII art,
    and the letters correctly guessed and the wrong letters and the secret word
    '''
    global FORCAIMG
    print(FORCAIMG[len(wrongLetters)] + '\n')

    print('Wrong Letters: ', end = ' ')
    print_with_spaces(wrongLetters)

    empty = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in rightLetters:
            empty = empty[:i] + secretWord[i] + empty[i + 1:]

    print_with_spaces(empty)


def guess_receive(guessMade):
    '''
    Guess validation: Must be a single letter not used yet.
    '''
    while True:
        guess = input('Adivinhe uma letra: \n').upper()

        if len(guess) != 1:
            print('É permitido apenas uma letra.')
        elif guess in guessMade:
            print('Essa letra já foi usada, escolha novamente.')
        elif not 'A' <= guess <= 'Z':
            print('Apenas letras são escolhas válidas.')
        else:
            return guess


def play_again():
    '''
    Ask if the user wants to play again.
    :return: boolean = user answear
    '''
    return input('Deseja continuar jogando? [S/N]: ').upper().strip()


def check_won(secretWord, rightLetters):
    '''
    checks whether the player has hit all the letters of the secret word.
    '''
    won = True
    for letter in secretWord:
        if letter not in rightLetters:
            won = False
            break

    return won


main()





