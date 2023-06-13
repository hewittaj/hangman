import random
import requests

# Initialize Variables
display = []
end_of_game = False
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words_link = "https://www.mit.edu/~ecprice/wordlist.10000"
"""
Get word from MIT site and randomly select one.
"""
word_list = requests.get(words_link).text.split("\n")
chosen_word = random.choice(word_list)
print(chosen_word)  #TODO Delete
split_word = list(chosen_word)
word_length = len(split_word)

# Append blanks to the display variable
for _ in range(len(split_word)):
    display.append("_")

while not end_of_game:
    print(' '.join(display))
    guess = input("Please guess a letter! ").lower()
    if len(guess) > 1:
        print("***Guess can only contain one letter!***\n")
        continue
    elif len(guess) < 1:
        print("***Guess must contain at least one letter!***\n")
        continue
        
    if not guess.isalpha():
        print("***Guess must only contain letters***\n")
        continue
    """
    Determine if the user's guess equal's any of the letters in   
    the word and fill in the 'display' variable.
    """
    if guess.lower() not in split_word:
        lives -= 1
    else:
        for i in range(word_length):      
            if split_word[i] == guess:
                display[i] = guess
        
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if lives == 0:
        end_of_game = True
        print("You lose!")
    