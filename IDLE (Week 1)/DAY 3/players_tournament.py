import random

class Player:
    def __init__(self, name, rank, extra):
        self.name = name
        self.rank = rank
        self.extra = extra

class Tournament:
    def game(self, Player):
        if self.rank < Player.rank:
            print(self.name + ' beats ' + Player.name)
        elif self.rank == Player.rank:
            Tournament.tie(self, Player)
        else:
            print(self.name + ' losses to ' + Player.name)

    def tie(self, Player):
        if self.extra > Player.extra:
            print(self.name + ' beats ' + Player.name + ' via extra')
        elif self.extra == Player.extra:
            print(self.name + ' drew with ' + Player.name + ' via extra')
        else:
            print(self.name + ' losses to ' + Player.name + ' via extra')
    

player1 = Player('player1',1,random.randint(0,1))
player2 = Player('player2',13,random.randint(0,1))
player3 = Player('player3',3,random.randint(0,1))
player4 = Player('player4',4,random.randint(0,1))
player5 = Player('player5',3,random.randint(0,1))

players = (player1, player2, player3, player4, player5)

for i in range(len(players)):
    for j in range(len(players)):
        if i is not j:
            Tournament.game(players[i],players[j])
