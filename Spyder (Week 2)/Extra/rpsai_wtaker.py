import random

#Your class must be called GamePlayer, and it must have these functions
class GamePlayer:
    #Give your AI a name. You can put your name in it or not, depending on whether you want to be anonymous.
    #You can submit multiple AI's with different names for the tournament
    name = "W Taker v2"

    def __init__(self):
        self.isFirstTurn = True
        self.isSecondTurn = True
        self.choice = ""
        self.choices = []
        self.results = []
        self.opponentChoiceAfterMatch = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]] # R,P,S,L,T,W
        self.opponentChoice = ""
        self.opponentChoices = []
        self.opponentChoiceWeight = 1

    def madeUpAI(self):
        if(self.choices[-2] == "rock"):
            if(self.opponentChoice == "rock"):
                self.opponentChoiceAfterMatch[1+self.results[-2]][0] += self.opponentChoiceWeight
            elif(self.opponentChoice == "paper"):
                self.opponentChoiceAfterMatch[1+self.results[-2]][1] += self.opponentChoiceWeight
            else:
                self.opponentChoiceAfterMatch[1+self.results[-2]][2] += self.opponentChoiceWeight
        elif(self.choices[-2] == "paper"):
            if(self.opponentChoice == "rock"):
                self.opponentChoiceAfterMatch[4+self.results[-2]][0] += self.opponentChoiceWeight
            elif(self.opponentChoice == "paper"):
                self.opponentChoiceAfterMatch[4+self.results[-2]][1] += self.opponentChoiceWeight
            else:
                self.opponentChoiceAfterMatch[4+self.results[-2]][2] += self.opponentChoiceWeight
        else:
            if(self.opponentChoice == "rock"):
                self.opponentChoiceAfterMatch[7+self.results[-2]][0] += self.opponentChoiceWeight
            elif(self.opponentChoice == "paper"):
                self.opponentChoiceAfterMatch[7+self.results[-2]][1] += self.opponentChoiceWeight
            else:
                self.opponentChoiceAfterMatch[7+self.results[-2]][2] += self.opponentChoiceWeight

        self.opponentChoiceWeight += 0.1
        
        if(self.choice == "rock"):
            if(self.opponentChoiceAfterMatch[1+self.results[-1]][0] > self.opponentChoiceAfterMatch[1+self.results[-1]][1] and self.opponentChoiceAfterMatch[1+self.results[-1]][0] > self.opponentChoiceAfterMatch[1+self.results[-1]][2]):
                self.choice = "paper"
            elif(self.opponentChoiceAfterMatch[1+self.results[-1]][1] > self.opponentChoiceAfterMatch[1+self.results[-1]][0] and self.opponentChoiceAfterMatch[1+self.results[-1]][1] > self.opponentChoiceAfterMatch[1+self.results[-1]][2]):
                self.choice = "scissors"
            elif(self.opponentChoiceAfterMatch[1+self.results[-1]][2] > self.opponentChoiceAfterMatch[1+self.results[-1]][0] and self.opponentChoiceAfterMatch[1+self.results[-1]][2] > self.opponentChoiceAfterMatch[1+self.results[-1]][1]):
                self.choice = "rock"
            elif(self.opponentChoiceAfterMatch[1+self.results[-1]][0] == self.opponentChoiceAfterMatch[1+self.results[-1]][1] and self.opponentChoiceAfterMatch[1+self.results[-1]][0] == self.opponentChoiceAfterMatch[1+self.results[-1]][2]):
                self.choice = random.choice(["rock", "paper", "scissors"])
            elif(self.opponentChoiceAfterMatch[1+self.results[-1]][0] == self.opponentChoiceAfterMatch[1+self.results[-1]][1]):
                self.choice = random.choice(["paper", "scissors"])
            elif(self.opponentChoiceAfterMatch[1+self.results[-1]][0] == self.opponentChoiceAfterMatch[1+self.results[-1]][2]):
                self.choice = random.choice(["paper", "rock"])
            elif(self.opponentChoiceAfterMatch[1+self.results[-1]][1] == self.opponentChoiceAfterMatch[1+self.results[-1]][2]):
                self.choice = random.choice(["scissors", "rock"])
        
        elif(self.choice == "paper"):
            if(self.opponentChoiceAfterMatch[4+self.results[-1]][0] > self.opponentChoiceAfterMatch[4+self.results[-1]][1] and self.opponentChoiceAfterMatch[4+self.results[-1]][0] > self.opponentChoiceAfterMatch[4+self.results[-1]][2]):
                self.choice = "paper"
            elif(self.opponentChoiceAfterMatch[4+self.results[-1]][1] > self.opponentChoiceAfterMatch[4+self.results[-1]][0] and self.opponentChoiceAfterMatch[4+self.results[-1]][1] > self.opponentChoiceAfterMatch[4+self.results[-1]][2]):
                self.choice = "scissors"
            elif(self.opponentChoiceAfterMatch[4+self.results[-1]][2] > self.opponentChoiceAfterMatch[4+self.results[-1]][0] and self.opponentChoiceAfterMatch[4+self.results[-1]][2] > self.opponentChoiceAfterMatch[4+self.results[-1]][1]):
                self.choice = "rock"
            elif(self.opponentChoiceAfterMatch[4+self.results[-1]][0] == self.opponentChoiceAfterMatch[4+self.results[-1]][1] and self.opponentChoiceAfterMatch[4+self.results[-1]][0] == self.opponentChoiceAfterMatch[4+self.results[-1]][2]):
                self.choice = random.choice(["rock", "paper", "scissors"])
            elif(self.opponentChoiceAfterMatch[4+self.results[-1]][0] == self.opponentChoiceAfterMatch[4+self.results[-1]][1]):
                self.choice = random.choice(["paper", "scissors"])
            elif(self.opponentChoiceAfterMatch[4+self.results[-1]][0] == self.opponentChoiceAfterMatch[4+self.results[-1]][2]):
                self.choice = random.choice(["paper", "rock"])
            elif(self.opponentChoiceAfterMatch[4+self.results[-1]][1] == self.opponentChoiceAfterMatch[4+self.results[-1]][2]):
                self.choice = random.choice(["scissors", "rock"])

        else:
            if(self.opponentChoiceAfterMatch[7+self.results[-1]][0] > self.opponentChoiceAfterMatch[7+self.results[-1]][1] and self.opponentChoiceAfterMatch[7+self.results[-1]][0] > self.opponentChoiceAfterMatch[7+self.results[-1]][2]):
                self.choice = "paper"
            elif(self.opponentChoiceAfterMatch[7+self.results[-1]][1] > self.opponentChoiceAfterMatch[7+self.results[-1]][0] and self.opponentChoiceAfterMatch[7+self.results[-1]][1] > self.opponentChoiceAfterMatch[7+self.results[-1]][2]):
                self.choice = "scissors"
            elif(self.opponentChoiceAfterMatch[7+self.results[-1]][2] > self.opponentChoiceAfterMatch[7+self.results[-1]][0] and self.opponentChoiceAfterMatch[7+self.results[-1]][2] > self.opponentChoiceAfterMatch[7+self.results[-1]][1]):
                self.choice = "rock"
            elif(self.opponentChoiceAfterMatch[7+self.results[-1]][0] == self.opponentChoiceAfterMatch[7+self.results[-1]][1] and self.opponentChoiceAfterMatch[7+self.results[-1]][0] == self.opponentChoiceAfterMatch[7+self.results[-1]][2]):
                self.choice = random.choice(["rock", "paper", "scissors"])
            elif(self.opponentChoiceAfterMatch[7+self.results[-1]][0] == self.opponentChoiceAfterMatch[7+self.results[-1]][1]):
                self.choice = random.choice(["paper", "scissors"])
            elif(self.opponentChoiceAfterMatch[7+self.results[-1]][0] == self.opponentChoiceAfterMatch[7+self.results[-1]][2]):
                self.choice = random.choice(["paper", "rock"])
            elif(self.opponentChoiceAfterMatch[7+self.results[-1]][1] == self.opponentChoiceAfterMatch[7+self.results[-1]][2]):
                self.choice = random.choice(["scissors", "rock"])

        
        return(self.choice)
    
    
    def make_choice(self):
        #This function must return 1 of 3 values, 'rock', 'paper', or 'scissors'
        #If it returns anything else, your AI will forfeit the match
        if(self.isFirstTurn):
            self.isFirstTurn = False
            self.choice = random.choice(['rock', 'paper', 'scissors'])
            self.choices.append(self.choice)
            return(self.choice)

        elif(self.isSecondTurn):
            self.isSecondTurn = False
            if(self.choice == "rock"):
                if(self.results[0] == "0"):
                    self.choice = "scissors"
                elif(self.results[0] == "1"):
                    self.choice = "paper"
                else:
                    self.choice = "paper"
            elif(self.choice == "paper"):
                if(self.results[0] == "0"):
                    self.choice = "rock"
                elif(self.results[0] == "1"):
                    self.choice = "scissors"
                else:
                    self.choice = "scissors"
            else:
                if(self.results[0] == "0"):
                    self.choice = "paper"
                elif(self.results[0] == "1"):
                    self.choice = "rock"
                else:
                    self.choice = "rock"

            self.choices.append(self.choice)
            return self.choice

        
        else:
            ans = GamePlayer.madeUpAI(self)
            # delete triple quotes to switch to lose mode
            '''
            if(ans == "rock"):
                ans = "paper"
            elif(ans == "paper"):
                ans = "scissors"
            else:
                ans = "rock"
            '''

            self.choice = ans

            self.choices.append(self.choice)
            return(self.choice)

    def view_opponent_choice(self, opponent_choice):
        #This function doesn't have to do anything
        #You will be shown your opponent's choice from last round
        #One of 'rock', 'paper', or 'scissors'
        #You are not allowed to access win and loss records from the Tournament code
        #If you want to track your win and loss rate, you will need to compare
        #Your choice to your opponent's choice here.
        self.opponentChoice = opponent_choice
        self.opponentChoices.append(opponent_choice)
        if(self.choice == self.opponentChoice):
            self.results.append(0)
        elif(self.choice == "rock" and self.opponentChoice == "scissors"):
            self.results.append(1)
        elif(self.choice == "paper" and self.opponentChoice == "rock"):
            self.results.append(1)
        elif(self.choice == "scissors" and self.opponentChoice == "paper"):
            self.results.append(1)
        else:
            self.results.append(-1)
        return

    def new_player(self):
        #This function doesn't have to do anything
        #This will be called when you face a new opponent in a new match
        #You might want to use this method to reset your AI's strategy
        self.isFirstTurn = True
        self.isSecondTurn = True
        self.choice = ""
        self.choices = []
        self.results = []
        self.opponentChoiceAfterMatch = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.opponentChoice = ""
        self.opponentChoices = []
        self.opponentChoiceWeight = 1
        return

