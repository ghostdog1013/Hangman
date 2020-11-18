# Student Name: Yilun Liu
# Course Name: CS111 Intro to Programming
# Course Instructor: Aaron Bauer
# Date: 2019/10/17
# HW4 Debugging Exercise

import random

# a list of text-based pictures to illustrate the number of remaining guesses
hangman_pics = ["""






         """, """






=========""", """



      |
      |
      |
=========""", """
      +
      |
      |
      |
      |
      |
=========""", """
   ---+
      |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""]


# a function to get the next letter from the user
# repeatedly prompts the user until valid input is entered
# requires that the input be a single letter, and not be a previously guessed letter
# the parameter guessed is a list of previously guessed letters
# returns the user's next guess
def get_guess(guessed):
    guess = input("Guess a letter: ").lower()
    # keep asking until we get a letter that hasn't been guessed
    while guess in guessed or guess.isalpha()==False or len(guess) > 1:         # 1st: while instead of if

        if guess in guessed:
             msg = "You've already guessed that letter. "
        elif guess.isalpha()==False:                                            # 2nd: ==False
             msg = "That's not a letter. "
        elif len(guess) > 1:
             msg = "That is more than one letter. "
        guess = input(msg + "Guess a letter: ").lower()

    guessed.append(guess)                                                       # 3rd:append

    return guess


# a function to play a game of hangman
def play():
    # make a random choice from a file with one word per line
    word_file = open("words.txt")
    word_1 = random.choice(word_file.readlines())
                                                                                #print(word_1)
    word = word_1.replace("\n","")                                              # 4th: the last line is read accidentlly.
    #print(word_1)
    word_file.close()

    current = [] # list of the user's current progress
    for c in word: # starts with no letters guessed, so a blank ("_") for each letter
        current.append("_")
    guessed = [] # list of previously guessed letters

    guesses = 10 # current number of guesses
    #guess = get_guess(guessed)
    # while the user hasn't guessed the word and has guesses remaining
    while "".join(current) != word and guesses != 0:                            # 5th: make sure it never goes down to negative
        # display the current status of the game
        print("--------------------------------------------------")
        print(guesses, "guesses left")
        print(hangman_pics[10 - guesses])
        print(" ".join(current))
        print("Letters you've already guessed:", " ".join(sorted(guessed)))
        print()

        # get the user's next guess, passing in the list of already guessed letters
        guess = get_guess(guessed)

        if guess in word: # correct guess
            # replace the corresponding blanks in current with the guessed letter
            for i in range(len(word)):
                if guess == word[i]: # this location matches the guessed letter
                    current[i] = guess
                #else:                                                          # 6th:delete
                #    current[i] = "_"


        else:
            guesses = guesses - 1



    # we've left the while loop, so the game is over
    # check whether the user won or lost
    if "".join(current) == word:
        print(" ".join(current))
        print("You win!")
    elif guesses == 0:
        print("You lose. The word was", word)
        return(print(hangman_pics[-1]))



play()
