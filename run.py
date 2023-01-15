import gspread
from google.oauth2.service_account import Credentials
import random


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('word_library')

words = SHEET.worksheet('words')
data = words.get_all_values()
print(words)

def hangman():
	hangman1 = [
	"""
+----+
     |
     |
     |
     |
     |
     ===""", """
+----+
  |  |
  O  |
     |
     |
     |
     ===""", """
+----+
  |  | 
  O  |
 /   |
     |
     |
     ===""", """
+----+
  |  |
  O  |
 /|  |
     |
     |
     ===""", """
+----+
  |  |
  O  |
 /|\ |
     |
     |
     ===""", """

+----+
  |  |
  O  |
 /|\ |
  |  |
     | 
     ===""", """
+----+
  |  |
  O  |
 /|\ |
  |  |
 /   | 
     ===""", """
+----+
  |  |
  O  |
 /|\ |
  |  | 
 / \ | 
     ===""", """
     
"""
	]
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
			
if __name__ == "__main__":
    hangman()