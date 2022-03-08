from game.game import Game
from game.ui import UI

ui = True

if ui:
    UI().display()
else:
    while True:
        choice = input("\nKäytä algoritmia? (y/n): ")
        if choice == "n":
            PLAYER = True
        else:
            PLAYER = False
        Game(PLAYER,stop_when_win=True).play()
