from game.game import Game
import json

with open("test_results.json", mode="w+") as file:
    runs = int(input("Kuinka monta peliä pelataan? Yksi peli kestää noin 30 - 120 sekuntia:\n"))
    game = Game(player=False, print_to_terminal=False, stop_when_win=True)

    games = {}

    for i in range(runs):
        info = game.play()
        games[i] = info

    json.dump(games, file, ensure_ascii=False, indent=4)
    print(f"Kirjoitettu tulokset '{file.name}' tiedostoon")