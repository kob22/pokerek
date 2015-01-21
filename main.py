from table import *
from player import *

players = []


a = Table()
for id in range(3):
    players.append(Player(id,"{0}".format(id*100), 1500))

for id in players:
    a.addPlayer(id)
a.start()