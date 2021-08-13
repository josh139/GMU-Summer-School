import random

HANGMANPICS = ['''



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

phrases = ['better luck next time',
         'the early bird gets the worm',
         'may the force be with you',
         'beam me up scotty']

def display_board(hangman_pics, missed_letters, correct_letters, secret_phrase):
  print(hangman_pics[len(missed_letters)])
  print()

  print('Missed letters:', end = ' ')
 
  for letter in missed_letters:
    print(letter, end = ' ')
  print()
  print()

  print('Secret Phrase:', end = ' ')

  for word in secret_phrase:
    blanks = '_' * len(word)
  
    for i in range(len(word)):
      if word[i] in correct_letters or word[i] == ' ':
        blanks = blanks[:i] + word[i] + blanks[i + 1:]
   
    for letter in blanks:
      print(letter, end = ' ')
    
  print()
  print()

def get_guess(already_guessed):
  while True:
    print('Guess a letter:', end = ' ')
    guess = input()
    guess = guess.lower()

    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in already_guessed:
      print('You have already guessed that letter. Please choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print('Please enter a letter.')
    else:
      return guess

def playAgain():
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

missed_letters = ''
correct_letters = ''
secret_phrase = random.choice(phrases)
game_is_done = False

while True:
  display_board(HANGMANPICS, missed_letters, correct_letters, secret_phrase)

  guess = get_guess(missed_letters + correct_letters)

  if guess in secret_phrase:
    correct_letters = correct_letters + guess

    found_all_letters = True
    for letter in secret_phrase:
      if letter not in correct_letters and letter != ' ':
        found_all_letters = False
        break
    if found_all_letters:
      print('You have won!!! The secret phrase is "' + secret_phrase + '"')
      game_is_done = True
  else:
    missed_letters = missed_letters + guess

    if len(missed_letters) == len(HANGMANPICS) - 1:
      display_board(HANGMANPICS, missed_letters, correct_letters, secret_phrase)
      print('You have run out of guesses and lose! The secret phrase was: "' + secret_phrase + '"')
      game_is_done = True

  if game_is_done:
    if playAgain():
      missed_letters = ''
      correct_letters = ''
      game_is_done = False
      secret_phrase = random.choice(phrases)
    else:
      break
