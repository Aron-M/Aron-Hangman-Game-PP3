import random


def hangman():
    hangman = [
"""
+---+
    |
    |
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    |
    |
    ===""", """
+---+
  | |
  O |
 /  |
    |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    |
    |
    ===""", """
+---+
  | |
  O |
 /|\|
    |
    | 
    ===""", """

+---+
  | |
  O |
 /|\|
  | | 
    | 
    ===""", """
+---+
  | |
  O |
 /|\|
  | | 
 /  | 
    ===""", """
+---+
  | |
  O |
 /|\|
  | | 
 / \| 
    ===""", """
"""
]

words = ['balloon', 'aeroplane', 'computer', 'corridor', 'television', 'university', 'paraglide', 'submarine', 'ferriswheel']

word = random.choice(words).lower()


guessed_right = []
guessed_wrong = []
tries = 8
hangman_count = -1

while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_right:
            output += letter
        else:
            output += '_'
    if output == word:
        break
    print("Try to guess the correct word: ",output)
    print("You have ", tries," chances left")
    guess = input().lower()
    if guess in guessed_right or guess in guessed_wrong:
        print("You have already guessed", guess, " ,please try again!")
    elif guess in word:
        print("That was great! Well done, you guessed the right letter!")
        guessed_right.append(guess)
    else:
        print("Sorry, but you have guessed a wrong letter! Please try again.")
        hangman_count = hangman_count + 1
        tries = tries-1
        guessed_wrong.append(guess)
        print(hangman1[hangman_count])
    
    if tries == 0:
        print("GAME OVER, YOU LOST!")
    
    if __name__ == "__main__":
        hangman()