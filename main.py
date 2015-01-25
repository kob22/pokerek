from table import *
from player import *

players=[]
a = Table()

#dodaje graczy z id i budzetem
def add_players(id,money):
    a.addPlayer((Player(id,"{0}".format(id), money) ))
    return 0


#zwarca karty na stole
def print_board():
    return a.board().__str__()

#gra, jesli zwroci 0 koniec gry, jest wygrany, jesli 1 gramy dalej
#kolejne etapy w grze, po kazdym trzeba wywolwac print board i players oraz auction
def game():
    a.start()
    return 1

def flop():
    a.play_flop()
    return 1

def turn():
    a.play_turn()
    return 1

def river():
    a.play_river()
    return 1

#obsluga gracza zwraca wszystko, konkretne akcje dodam pozniej
def player(id):
    for x in a.game.players:
        if x.id == id:
            return x
    return -1


add_players(1,1500)
add_players(2,1500)
add_players(3,1500)
add_players(4,1500)


game()



a.auction(1,"raise",100)
a.auction(2,"call",100)
a.auction(3,"call",100)
a.auction(4,"call",100)

print (a.is_winner())
flop()

print(print_board())
a.auction(1,"bet",100)
a.auction(2,"fold",0)
a.auction(3,"fold",0)
a.auction(4,"fold",0)
a.auction(4,"fold",0)

print (a.is_winner())

for player in a.players:
    print (player.isFold)
