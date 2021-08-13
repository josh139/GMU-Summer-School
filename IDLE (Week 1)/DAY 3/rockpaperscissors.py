import tkinter
import random
 
user_score = 0
comp_score = 0
comp_options = ['rock', 'paper', 'scissors']
human_choices = []
 
tk_window = tkinter.Tk()
tk_window.geometry("400x300")
tk_window.title("Rock-Paper-Scissors Game")

def three_in_row():
    last_human_choice = human_choices[len(human_choices)-1]
    if last_human_choice == 'rock':
        return 'paper'
    if last_human_choice == 'paper':
        return 'scissors'
    else: # last_human_choice == 'scissors'
        return 'rock'

def two_in_row():
    last_human_choice = human_choices[len(human_choices)-1]
    if last_human_choice == 'rock':
        return 'scissors'
    if last_human_choice == 'paper':
        return 'rock'
    else: # last_human_choice == 'scissors'
        return 'paper'
    
def weighted():
    return random.choice(comp_options)

def ai_random():
    return random.choice(['rock', 'paper', 'scissors'])

def top_to_bottom():
    last_human_choice = human_choices[len(human_choices)-1]
    if last_human_choice == 'rock':
        return 'scissors'
    if last_human_choice == 'paper':
        return 'rock'
    else: # last_human_choice == 'scissors':
        return 'paper'

def get_computer_choice():
    if len(human_choices) < 2:
        return ai_random()
    elif human_choices[len(human_choices)-1] == human_choices[len(human_choices)-2] and human_choices[len(human_choices)-1] == human_choices[len(human_choices)-3]:
        return three_in_row()
    elif human_choices[len(human_choices)-1] == human_choices[len(human_choices)-2]:
        return two_in_row()
    elif human_choices[len(human_choices)-1] != human_choices[len(human_choices)-2] and human_choices[len(human_choices)-1] != human_choices[len(human_choices)-3]:
        return top_to_bottom()
    else :
        return weighted()

def determine_game_result(human_choice, comp_choice):
    global user_score
    global comp_score
    
    print("Human: " + human_choice + " | Computer: " + comp_choice)
    if human_choice == comp_choice:
        display_winner = "Result: Tie!"
    elif human_choice == "rock" and comp_choice == "scissors":
        display_winner = "Result: Human Player Wins!"
        user_score += 1
    elif human_choice == "scissors" and comp_choice == "paper":
        display_winner = "Result: Human Player Wins!"
        user_score += 1
    elif human_choice == "paper" and comp_choice == "rock":
        display_winner = "Result: Human Player Wins!"
        user_score += 1
    else:
        display_winner = "Computer Player Wins!"
        comp_score += 1

    human_choices.append(human_choice)
    
    if human_choice == 'rock':
        comp_options.append('paper')
    elif human_choice == 'paper':
        comp_options.append('scissors')
    else:
        comp_options.append('rock')
        
    display_game_result(human_choice, comp_choice, display_winner)
 
def display_game_result(human_choice, comp_choice, display_winner):
    game_result = "Human Player Choice: " + human_choice + "\nComputer Player Choice: " + comp_choice + "\n" + display_winner + "\nHuman Score: " + str(user_score) + "\nComputer Score: " + str(comp_score)

   # if len(human_choices) >= 2 and human_choice == human_choices[-1]: # If the user has 2 choices and they're both the same use stratergy 2
   #     weighted()
   # else:
   #     two_in_row() # Play random as there are no patterns yet

    text_area = tkinter.Text(height = 12, width = 40)
    text_area.grid(column = 0, row = 4)
    text_area.insert('1.0', game_result)
 
text_area = tkinter.Text(height = 12, width = 40)
text_area.grid(column = 0,row = 4)
text_area.insert('1.0', "Ready to Play!")
 
def rock():
    determine_game_result('rock', get_computer_choice())
 
button_rock = tkinter.Button(text = "Rock", command = rock)
button_rock.grid(column = 0,row = 1)
 
def paper():
    determine_game_result('paper', get_computer_choice())
 
button_paper = tkinter.Button(text = "Paper", command = paper, background = 'Blue', foreground = 'White')
button_paper.grid(column = 0, row = 2)
 
def scissors():
    determine_game_result('scissors', get_computer_choice())
 
button_scissors = tkinter.Button(text = "Scissors", command = scissors)
button_scissors.grid(column = 0, row = 3)
