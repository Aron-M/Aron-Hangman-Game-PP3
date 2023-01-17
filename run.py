import random


def words_from_file_reader(filepath='words.txt'):
    result = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            word = str(line).lower().strip()
            result.append(word)
        return result


def hangman_game():
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
    words = words_from_file_reader()
    word = random.choice(words).lower().strip()

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
            print(f'Hey fantastic, you guessed the word {output} correctly')
            return
        print("Try to guess the correct word: ", output)
        print("You have ", tries, " chances left")
        guess = input().lower()
        if guess in guessed_right or guess in guessed_wrong:
            print("You have already guessed", guess, " ,please try again!")
        elif guess in word:
            print("That was great! Well done, you guessed the right letter!")
            guessed_right.append(guess)
        else:
            print("Sorry, but you have guessed wrong! Please try again.")
            hangman_count = hangman_count + 1
            tries = tries - 1
            guessed_wrong.append(guess)
            print(hangman[hangman_count])

        if tries == 0:
            print(f"GAME OVER, YOU LOST! What you were looking for was:{word}")
            return


if __name__ == '__main__':
    user = ''
    while user == '':
        user = input('Do you wanna play hangman? (y or yes?)').lower().strip()
        if user == 'y' or user == 'yes':
            hangman_game()
            user = ''
        if user == 'n' or user == 'no':
            print('Thanks for playing, see you next time')
            exit()
        else:
            print('Please type y or yes to play, else type n or no to quit.')
            user = ''