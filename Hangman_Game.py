# -*- coding: utf-8 -*-

# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print('Loading word list from file...')
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print('', len(wordlist), 'words loaded.')
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all   letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    compare_result = 1
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            continue
        else:
            compare_result = 0
    return bool(compare_result)


def get_guessed_word(secret_word, letters_guessed):

    answer_word = secret_word
    j = 0 
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            continue
        else:
            answer_word = (answer_word[: i+j] + '_ ' 
                           + secret_word[i+1: ])
            j += 1
    return answer_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_available = string.ascii_lowercase
    for i in range(len(letters_available)):
        if letters_available[i] not in letters_guessed:
            continue
        else:
            letters_available = (letters_available[: i] 
                                + '_' + letters_available[i+1: ])
    letters_available = letters_available.replace('_', '')
    return letters_available

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears    in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    alphabet_letters = (string.ascii_uppercase 
                        + string.ascii_lowercase)
    guesses_remaining = 6
    letters_guessed = []
    guess = str
    total_score = 0
    unique_letters = 0
    warnings = 3

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word),
           'letters long')
    print('You have ' + str(warnings) + ' warnings left.')
    print('-------------')

    while guesses_remaining > 0 and guesses_remaining <= 6:
            
        print('You have ' + str(guesses_remaining) + ' guesses left')
        print('Available letters: ' 
               + str(get_available_letters(letters_guessed)), end = 
               '')
        guess = input('Please guess a letter: ').lower()
        if guess in secret_word:

# The first time you guessed a letter correctly
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good guess: ' 
                       + get_guessed_word(secret_word,  
                                         letters_guessed))
                print('-------------')
                unique_letters += 1
                if is_word_guessed(secret_word, letters_guessed):
                    break

# You guessed the letter correctly but not the first time
            else:
                warnings -= 1
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You now have " + str(warnings) + ' warnings left:')
                    print((get_guessed_word(secret_word, 
                                            letters_guessed)))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' +  
                          get_guessed_word(secret_word, 
                                           letters_guessed))
                    guesses_remaining -= 1

# You entered a number or symbol that is not from the alphabet                   
        elif guess not in alphabet_letters:
            warnings -= 1
            if warnings >= 0:
                print(('Oops! That is not a valid letter. You now have ' + str(warnings) + ' warnings left:'))
                print(get_guessed_word(secret_word, letters_guessed))
                print('-------------')
            else:
                print('Oops! That is not a valid letter. You have no warnings left')
                print('so you lose one guess: ' 
                      + get_guessed_word(secret_word, 
                                         letters_guessed))
                guesses_remaining -= 1

# The first time you entered a letter incorrectly 
        else:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                if guess in ['a', 'e', 'i', 'o', 'u']:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word: ' 
                      + get_guessed_word(secret_word, 
                                         letters_guessed))
                print('-------------')

# You guessed the letter incorrectly and not for the fist time
            else:
                warnings -= 1
                if warnings >= 0:
                    print("Oops! You've already guesses that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, 
                                           letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' 
                          + get_guessed_word(secret_word, 
                                             letters_guessed))
                    guesses_remaining -= 1

    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * unique_letters
        print('Congratulations, you won!')
        print('Your total score for this game is: ', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was else.')

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    letters_revealed = []
    compare_result = 1
    for i in range(len(my_word)):
        if (my_word[i] == '_') or (my_word[i] in letters_revealed):
            continue
        else:
            letters_revealed.append(my_word[i])
    if (len(my_word) == len(other_word) and my_word.count('_') < 
        len(other_word)):
        for i in range(len(other_word)):
            if my_word[i] == other_word[i]:
                continue
            elif my_word[i] == '_':
                if other_word[i] in letters_revealed:
                    compare_result = 0
                else:
                    continue
            else:
                compare_result = 0
    else:
        compare_result = 0
    return bool(compare_result)


def not_word_guesswrong(possible_word,letters_guessed_wrong):
    '''
    possible_word: string, a word which may match my_word 
    letters_guessed_wrong: list (of letters), which contains some wrong letters that have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of possible_word are not in letters_guessed_wrong;
      False otherwise
    '''
    compare_result = 1
    for i in range(len(possible_word)):
        if possible_word[i] not in letters_guessed_wrong:
            continue
        else:
            compare_result = 0
    return bool(compare_result)


def show_possible_matches(my_word,letters_guessed_wrong):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matchwords = []
    match_result = []
    for i in range(len(wordlist)):
        if not(match_with_gaps(my_word, wordlist[i])):
            continue
        elif not_word_guesswrong(wordlist[i],letters_guessed_wrong):
            possible_matchwords.append(wordlist[i])
        else:
            continue
    if possible_matchwords:
        match_result = possible_matchwords
    else:
        match_result = ["No matches found"]
    return match_result

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    alphabet_letters = (string.ascii_uppercase + 
                        string.ascii_lowercase)
    guesses_remaining = 6
    letters_guessed = []
    letters_guessed_wrong = []
    guess = str
    total_score = 0
    unique_letters = 0
    warnings = 3
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word),
          'letters long')
    print('You have ' + str(warnings) + ' warnings left.')
    print('-------------')
    
    while guesses_remaining > 0 and guesses_remaining <= 6:
            
        print('You have ' + str(guesses_remaining) + ' guesses left')
        print('Available letters: ' 
              + str(get_available_letters(letters_guessed)),end = '')
        guess = input('Please guess a letter: ').lower()

# Provide some hints after the following conditions are met
# condition1: an asterisk(*) should be input
# condition2: at least two proper letters have been guessed
        cond_1 = bool(guess == '*')
        cond_2 = bool(len(secret_word) 
                      - get_guessed_word(secret_word, 
                                         letters_guessed).count('_ ') 
                      > 1)
        if cond_1 and cond_2:
            print('Possible word matches are: ')
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed_wrong))
            print('-------------')
            continue
        if guess in secret_word:

# The first time you guessed a letter correctly
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good guess: ' + get_guessed_word(secret_word, 
                                                   letters_guessed))
                print('-------------')
                unique_letters += 1
                if is_word_guessed(secret_word, letters_guessed):
                    break

# You guessed the letter correctly but not the first time
            else:
                warnings -= 1
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' 
                          + get_guessed_word(secret_word, 
                                             letters_guessed))
                    guesses_remaining -= 1

# You entered a number or symbol that is not from the alphabet                   
        elif guess not in alphabet_letters:
            warnings -= 1
            if warnings >= 0:
                print('Oops! That is not a valid letter. You now have ' + str(warnings) + ' warnings left:')
                print(get_guessed_word(secret_word, letters_guessed))
                print('-------------')
            else:
                print("Oops! That is not a valid letter. You have no warnings left")
                print('so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
                
        else:
# The first time you entered a letter incorrectly 
            if guess not in letters_guessed:
                letters_guessed_wrong.append(guess)
                letters_guessed.append(guess)
                if guess in ['a', 'e', 'i', 'o', 'u']:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word: ' + 
                      get_guessed_word(secret_word, letters_guessed))
                print('-------------')

# You guessed the letter incorrectly and not for the fist time
            else:
                warnings -= 1
                if warnings >= 0:
                    print("Oops! You've already guesses that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, 
                                           letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' + 
                          get_guessed_word(secret_word, 
                                           letters_guessed))
                    guesses_remaining -= 1

    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * unique_letters
        print('Congratulations, you won!')
        print('Your total score for this game is: ', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was else.')
    
#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)

