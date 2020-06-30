# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char1 in secret_word:
        if char1 not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = []                           # List of characters
    for char1 in secret_word:
        if char1 in letters_guessed:
            guessed_word.append(char1)          # Append guessed character
        else:
            guessed_word.append("_ ")           # Append blank 
        
    guessed_word = "".join(guessed_word)        # join list of char into a string
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    missing_letters = []
    for char1 in string.ascii_lowercase:
        if char1 not in letters_guessed:
            missing_letters.append(char1)
    missing_letters = "".join(missing_letters)
    return missing_letters
                

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
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_length = len(secret_word)
    letters_guessed = []
    guess_left = 6
    warning_left = 3
    letter_vowel = ("aeiou")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", word_length, "long.")
    
    game_completion_status = is_word_guessed(secret_word, letters_guessed)
    
    while game_completion_status == False and guess_left > 0:
        missing_letters = get_available_letters(letters_guessed)
        print("------------------------------")
        print("You have", guess_left,"guesses left.")
        print("Available letters:", missing_letters)
        current_guess = input("Please guess a letter: ")
    
        if str.isalpha(current_guess) == True:
            current_guess = str.lower(current_guess)
        
            if current_guess not in letters_guessed:
                letters_guessed.append(current_guess)                        # Append list of guessed letters
        
                if current_guess in secret_word:
                    displayed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", displayed_word)
                else:
                    displayed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Oops! That letter is not in my word:", displayed_word)
                    
                    if current_guess in letter_vowel:
                        guess_left = guess_left - 2
                    else:
                        guess_left = guess_left - 1
                        
            else:
                if warning_left > 0:
                    warning_left = warning_left - 1
                    print("Oops! You've already guessed that letter. you now have", warning_left, "warnings:", displayed_word)
                else:
                    guess_left = guess_left - 1
                    print("Oops! You've already guessed that letter. you have no warnings left so you lose one guess: ", displayed_word)
                
        else: 
            if warning_left > 0:
                warning_left = warning_left - 1
            else:
                guess_left = guess_left - 1
            displayed_word = get_guessed_word(secret_word, letters_guessed)
            print("Oops! That is not a valid letter. You have", warning_left ,"warnings left:",displayed_word)
        
        game_completion_status = is_word_guessed(secret_word, letters_guessed)
    
    print("------------------------------")
    if game_completion_status == True:
        total_score = guess_left * len(letters_guessed)
        print("Congratulations, you won!")
        print("Your total score for this game is", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output_status = True
    stripped_word= my_word.replace(" ", "")             # Spaces are removed
    if len(stripped_word) == len(other_word):
        for i1 in range (len(stripped_word)):
            if stripped_word[i1] != "_":
                if (stripped_word[i1] != other_word[i1]):
                    output_status = False               # Rejected as letters do not match
                    #print("1")      
            else:
                list_stripped_word = list(stripped_word)
                del(list_stripped_word[i1])
                stripped_word_stripped = "".join(list_stripped_word)
                if other_word[i1] in stripped_word_stripped:
                    output_status = False               
                    #print("2")                      
    else:
        output_status = False                           # Rejected as spaces are not correct
        #print("3")
    
    return output_status



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    accepted_list = []
    num_accepted = 0
    for i1 in range (len(wordlist)):
        match_status = match_with_gaps(my_word, wordlist[i1])
        if match_status == True:
            accepted_list.append(wordlist[i1]) # Appends list with accepted value        
            num_accepted = num_accepted + 1
    
    if num_accepted == 0:
        print("No matches found")
        return
    else:
        accepted_words = " ".join(accepted_list)
        print(accepted_words)
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_length = len(secret_word)
    letters_guessed = []
    guess_left = 6
    warning_left = 3
    letter_vowel = ("aeiou")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", word_length, "long.")
    
    game_completion_status = is_word_guessed(secret_word, letters_guessed)
    
    while game_completion_status == False and guess_left > 0:
        missing_letters = get_available_letters(letters_guessed)
        print("------------------------------")
        print("You have", guess_left,"guesses left.")
        print("Available letters:", missing_letters)
        current_guess = input("Please guess a letter: ")
    
        if str.isalpha(current_guess) == True:
            current_guess = str.lower(current_guess)
        
            if current_guess not in letters_guessed:
                letters_guessed.append(current_guess)                        # Append list of guessed letters
        
                if current_guess in secret_word:
                    displayed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", displayed_word)
                else:
                    displayed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Oops! That letter is not in my word:", displayed_word)
                    
                    if current_guess in letter_vowel:
                        guess_left = guess_left - 2
                    else:
                        guess_left = guess_left - 1
                        
            else:
                if warning_left > 0:
                    warning_left = warning_left - 1
                    print("Oops! You've already guessed that letter. you now have", warning_left, "warnings:", displayed_word)
                else:
                    guess_left = guess_left - 1
                    print("Oops! You've already guessed that letter. you have no warnings left so you lose one guess: ", displayed_word)
                
        else: 
            if current_guess == '*':
                displayed_word = get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(displayed_word)
            else:
                if warning_left > 0:
                    warning_left = warning_left - 1
                else:
                    guess_left = guess_left - 1
                    displayed_word = get_guessed_word(secret_word, letters_guessed)
                print("Oops! That is not a valid letter. You have", warning_left ,"warnings left:",displayed_word)
        
        game_completion_status = is_word_guessed(secret_word, letters_guessed)
    
    print("------------------------------")
    if game_completion_status == True:
        total_score = guess_left * len(letters_guessed)
        print("Congratulations, you won!")
        print("Your total score for this game is", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
