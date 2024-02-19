import random

word_list = ['aswdnamd', 'ahdfjsn', 'jdjdne']
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
print(display)

end_of_Game = False

while not end_of_Game:
  guess = input("Guess a random letter: ").lower()
  
  for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position} \n Current letter: {letter}\n \
    Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

    print(display)

    if "_" not in display:
      end_of_Game = True
      print("You Win!!!")
