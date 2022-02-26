from game import Game

while True:
    choice = input("\nKäytä algoritmia? (y/n): ")
    if choice == "n":
        PLAYER = True
    else:
        PLAYER = False
    Game(PLAYER,stop_when_win=True).play()