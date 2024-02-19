import random

word_list = ['aswdnamd', 'ahdfjsn', 'jdjdne']
chosen_word = random.choice(word_list)
guess = input("Guess a random letter: ").lower()
for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
