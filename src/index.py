from game import Game

while True:
    choice = input("\nKäytä algoritmia? (y/n): ")
    if choice == "n":
        player = True
    else:
        player = False
    Game(player).play()
