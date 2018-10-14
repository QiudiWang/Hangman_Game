# -*- coding: utf-8 -*-

# Hangman Game
# -----------------------------------
# Helper code

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



# -------------------------------------
# Hangman Part 1: Three helper functions

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE
    i =0
    while i < len(secret_word):
        if secret_word[i] not in letters_guessed:
            return False
        else:
            i += 1
    return True
#print(is_word_guessed('apple', ['e', 'i', 'k', 'p', 'r', 's']))       
#print(is_word_guessed('egg',['g', 'e']))
#print(is_word_guessed('pig', ['p', 'i']))
#print(is_word_guessed('dog',['d', 'p', 'g']))



def get_guessed_word(secret_word, letters_guessed):

    # FILL IN YOUR CODE HERE
    answer_word = secret_word
    j = 0 
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            continue
        else:
            answer_word = answer_word[:i+j] + '_ ' + secret_word[i+1:]       
            j += 1   # calculate '_ '
    return answer_word
"""
    answer_word = secret_word
    i = 0
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            answer_word = answer_word[:i] + secret_word[i] + answer_word[i+1:]
        else:
            answer_word = answer_word[:i] + '_' + answer_word[i+1:]
        i += 1
    return answer_word
"""
'''
def get_guessed_word(secret_word, letters_guessed):
   
    count = 0
    blank = ['_ '] * len(secret_word)

    for i, c in enumerate(secret_word):
        if c in letters_guessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secret_word):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secret_word):
                return ''.join(str(e) for e in blank)
'''
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
#print(get_guessed_word('pig', ['p', 'i']))
#print(get_guessed_word('absolutely',['b', 'c', 'l']))
            

    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE
    letters_available = string.ascii_lowercase
    for i in range(len(letters_available)):
        if letters_available[i] not in letters_guessed:
            continue
        else:
            letters_available = letters_available[:i] + '_' + letters_available[i+1:]
    letters_available = letters_available.replace('_','')
    return letters_available
#print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))  
#print(get_available_letters(['b', 'g', 'h', 'l', 'o', 'w']))
#print(get_available_letters(['a', 's', 'x','b', 'c', 'a']))
    
"""
    str_letters =str
    i = 0
    #j = 0
#    a = string.ascii_lowercase
#    slist = list(a) WHY CALLED AN ERROR
    
    slist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
    if letters_guessed == []:
        str_letters = ''.join(slist)
    else:
        while i < len(letters_guessed):
            j =0
            while j <len(slist):
                if letters_guessed[i] == slist[j]:
                    slist_new = slist.pop(j)
                else:
                    slist_new = slist
                j += 1
            i += 1
            str_letters = ''.join(slist_new)
    return str_letters
"""

#print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))
# end of part 1  
    
 
       
# -------------------------------------
# Hangman Part 2: The Game

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
    # FILL IN YOUR CODE HERE
    
#    alphabet_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alphabet_letters = string.ascii_uppercase + string.ascii_lowercase
    guesses_remaining = 6
    letters_guessed = []
    guess = str
    total_score = 0
    unique_letters = 0
    warnings = 3
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('You have ' + str(warnings) + ' warnings left.')
    print('-------------')
    
    while guesses_remaining > 0 and guesses_remaining <= 6:
            
        print('You have ' + str(guesses_remaining) + ' guesses left')
        print('Available letters: ' + str(get_available_letters(letters_guessed)),end = '')
        guess = input('Please guess a letter:').lower()
        if guess in secret_word:
            
# The first time you guessed a letter correctly
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
                print('-------------')
                unique_letters += 1
                if is_word_guessed(secret_word, letters_guessed):
                    break

# You guessed the letter correctly but not the first time
            else:
                warnings -=1
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
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
                letters_guessed.append(guess)
                # Guess a letter that is a vowel, but incorrectly
                if guess in ['a', 'e', 'i', 'o', 'u']:
                    guesses_remaining -= 2
                # Guess a letter that is a consonant and incorrectly
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word:' + get_guessed_word(secret_word, letters_guessed))
                #print('Oops! That is not a valid letter. You have ') + warnings + (' warnings:')
                #print(get_guessed_word(secret_word, letters_guessed))
                print('-------------')

# You guessed the letter incorrectly and not for the fist time
            else:
                warnings -= 1
                #guesses_remaining -= 1
                #print("Oops! You've already guesses that letter." + get_guessed_word(secret_word, letters_guessed))
                if warnings >= 0:
                    print("Oops! You've already guesses that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -=1

    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * unique_letters
        print('Congratulations, you won!')
        print('Your total score for this game is: ', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was else.')
        
# -----------------------------------
# end of part 2
    

     
# -------------------------------------
# Hangman Part 3: The Game with Hints

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE
    my_word = my_word.replace(' ','')
    if len(my_word) == len(other_word) and my_word.count('_') < len(other_word):
        for i in range(len(other_word)):
            if my_word[i] == other_word[i] or my_word[i] == '_':
                continue
            else:
                return False
        return True
    else:
        return False
#print(match_with_gaps('t _ _ _', 'tact'))       
#print(match_with_gaps('a_ _ le','banana'))
#print(match_with_gaps('a_ _ le','apple'))
#print(match_with_gaps('a_ ple','apple'))        
        

    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE
# method 1:use 'def match_with_gaps(my_word, other_word)'
    possible_matchwords = []
    for i in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[i]) == False:
            continue
        else:
            possible_matchwords.append(wordlist[i])
    if possible_matchwords:
        return possible_matchwords
    else:
        return "No matches found"

# method 2:without 'def match_with_gaps(my_word, other_word)'
"""
    my_word = my_word.replace(' ','')
    possible_matchwords = []
    for i in range(len(wordlist)):
        if len(my_word) != len(wordlist[i]) or my_word.count('_') == len(wordlist[i]):
            continue
        else:
            possible_word = wordlist[i]
            for j in range(len(possible_word)):
                if my_word[j] == possible_word[j] or my_word[j] == '_':
                   continue
                else:
                    break
            if j == len(possible_word) - 1:
                possible_matchwords.append(possible_word)
    if possible_matchwords:
        return possible_matchwords
    else:
        return "No matches found"
"""   

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

    # FILL IN YOUR CODE
    alphabet_letters = string.ascii_uppercase + string.ascii_lowercase
    guesses_remaining = 6
    letters_guessed = []
    guess = str
    total_score = 0
    unique_letters = 0
    warnings = 3
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('You have ' + str(warnings) + ' warnings left.')
    print('-------------')
    
    while guesses_remaining > 0 and guesses_remaining <= 6:
            
        print('You have ' + str(guesses_remaining) + ' guesses left')
        print('Available letters: ' + str(get_available_letters(letters_guessed)),end = '')
        guess = input('Please guess a letter:').lower()

# Give some conditions required to provide hints       
        if guess == '*' and len(secret_word) - get_guessed_word(secret_word, letters_guessed).count('_ ') > 1:
            print('Possible word matches are:')
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            print('-------------')
            continue
        
        if guess in secret_word: 
            
# The first time you guessed a letter correctly
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
                print('-------------')
                unique_letters += 1
                if is_word_guessed(secret_word, letters_guessed):
                    break
# You guessed the letter correctly but not the first time
            else:
                warnings -=1
                if warnings >= 0:
                    print("Oops! You've already guessed that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
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
                letters_guessed.append(guess)
                if guess in ['a', 'e', 'i', 'o', 'u']:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word:' + get_guessed_word(secret_word, letters_guessed))
                #print('Oops! That is not a valid letter. You have ') + warnings + (' warnings:')
                #print(get_guessed_word(secret_word, letters_guessed))
                print('-------------')

# You guessed the letter incorrectly and not for the fist time
            else:
                warnings -= 1
                #guesses_remaining -= 1
                #print("Oops! You've already guesses that letter." + get_guessed_word(secret_word, letters_guessed))
                if warnings >= 0:
                    print("Oops! You've already guesses that letter. You now have " + str(warnings) + ' warnings left:')
                    print(get_guessed_word(secret_word, letters_guessed))
                    print('-------------')
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left")
                    print('so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -=1

    if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * unique_letters
        print('Congratulations, you won!')
        print('Your total score for this game is: ', total_score)
    else:
        print('Sorry, you ran out of guesses. The word was else.')   

# -----------------------------------
# end of part 3

# Main code 

# To test part 2
# uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)


    
# To test part 3 re-comment out the above lines and 
# uncomment the following two lines. 
    
#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)

            


