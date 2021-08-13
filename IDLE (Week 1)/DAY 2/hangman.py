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

nouns = ("dog", "cat", "sofa", "computer", "table")
verbs = ("jumps", "runs", "rubs", "scratch", "barks") 
adv = ("violently", "stupidly", "aggressively", "furiously", "nonchalantly")
adj = ("cute", "beautiful", "adorable", "strange", "broken")
num = random.randrange(0,5)
word1 = nouns[num]
word2 = verbs[num]
word3 = adv[num]
word4 = adj[num]
words =  word1 + ' ' + word2 + ' ' + word3 + ' ' + word4

def get_random_word(words):
  return words

def display_board(hangman_pics, missed_letters, correct_letters, secret_word, score):
  print('Score : ' + str(score) + hangman_pics[len(missed_letters)]) # Add score and parse to String
  print()

  for letter in missed_letters:
    print(letter, end = ' ')
  print()
  print()

  blanks = '_' * len(word1) + ' ' + '_' * len(word2) + ' ' + '_' * len(word3) + ' ' + '_' * len(word4)
  
  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    if secret_word[i] == ' ':
      blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

  print('Secret Word:', end = ' ')
 
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
    print()
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('hangman')
 
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words) # no spaces
print(secret_word)
game_is_done = False
score = 0

while True:
  display_board(HANGMANPICS, missed_letters, correct_letters, secret_word, score)

  guess = get_guess(missed_letters + correct_letters)

  if guess in secret_word:
    correct_letters = correct_letters + guess

    found_all_letters = True
    for letter in secret_word:
      if letter not in correct_letters and letter != ' ':
        found_all_letters = Falsej
        
        break
    if found_all_letters:
      print('You have won!!! The secret word is ' + words)
      score = score + 1 # Add a point when the user wins
      game_is_done = True
      
  else:
    missed_letters = missed_letters + guess

    if len(missed_letters) == len(HANGMANPICS) - 1:
      display_board(HANGMANPICS, missed_letters, correct_letters, secret_word, score)
      print('You have run out of guesses and lose! The secret word was: ' + words)
      game_is_done = True

  if game_is_done:
    if playAgain():
      missed_letters = ''
      correct_letters = ''
      game_is_done = False
      secret_word = get_random_word(words)
    else:
      break
  
