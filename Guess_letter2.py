import random

word_list = ['aswdnamd', 'ahdfjsn', 'jdjdne']
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
print(display)
guess = input("Guess a random letter: ").lower()

for position in range(word_length):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter

print(display)
