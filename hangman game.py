import random

word_list = ['america', 'oneworldtradecenter', 'camel']
chosen_word = random.choice(word_list)
print(f'the chosen word is: {chosen_word}!')
lives = 6
hang = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
end_of_game = False
display = []
for x in chosen_word:
    display.append('_')
print(display)

while not end_of_game:
    user_choice = str(input('insert a letter:')).lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_choice:
            display[position] = letter
    print(display)

    if user_choice not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('you lose')
    print(hang[lives])

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(lives)
