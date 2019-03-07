# Hangman Game
This is a python game called hangman. Players in this game can play against the computer. 

Here is the game architecture:
1. The computer must select a word at random from the list of available words that was provided in words.txt. 
2. Users start with 6 guesses and 3 warnings.
3. At the start of the game, let the user know how many letters the computer's word contains and how many guesses s/he starts 
   with.
4. The computer keeps track of all the letters the user has not guessed so far and before each turn shows the user the 
   “remaining letters”.

Here are the game rules:
1. The user starts with 3 warnings.
2. If the user inputs anything besides an alphabet (symbols, numbers), tell the user that they can only input an alphabet.
   a. If the user has one or more warning left, the user should lose one warning. Tell the user the number of remaining 
      warnings.
   b. If the user has no remaining warnings, they should lose one guess.
3. If the user inputs a letter that has already been guessed, print a message telling the user the letter has already been 
   guessed before.
   a. If the user has one or more warning left, the user should lose one warning. Tell the user the number of remaining 
      warnings.
   b. If the user has no warnings, they should lose one guess.
4. If the user inputs a letter that hasn’t been guessed before and the letter is in the secret word, the user loses no guesses.
5. Consonants: If the user inputs a consonant that hasn’t been guessed and theconsonant is not in the secret word, the user 
   loses one guess if it’s a consonant.
6. Vowels: If the vowel hasn’t been guessed and the vowel is not in the secret word, the user loses two guesses. Vowels are 
   'a', 'e', 'i', 'o', and 'u'. 'y' does not count as a vowel.

Game shoould end when the user constructs the full word or runs out of guesses. 
If the player runs out of guesses before completing the word, tell them they lost and reveal the word to the user when the game ends. 
If the user wins, print a congratulatory message and tell the user their score.
Total score = guesses_remaining* number unique letters in secret_word

*This game also has hints! Users can ask the computer for a hint, and computer would list all the words in the word list that match what you have currently guessed.
