import words_fetcher
import random


def congratulate_user():
    print(f"Congratulations, you won! your words: {guesses}")

def has_word_been_guessed(word):
  return word in guesses

def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
  guess = input("Your next take: ")
  if has_word_been_guessed(guess):
    print("You've already used that word. Try again.")
  elif guess in full_list:
    guessed += 1
    guesses.append(guess)
    if guessed == WORDS_TO_WIN:
        congratulate_user()
        exit()
        print(f"That's right! {WORDS_TO_WIN - guessed} to go")
  else:
    errors += 1
    if errors == ERRORS_TO_LOSE:
      print(f'\033[31mYo have reached the maximum number of attempts. I am sorry to inform you, but You have lost!\nYour word was {word}\033[0m')
      exit()
    print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
