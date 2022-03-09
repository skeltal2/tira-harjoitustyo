from game.game import Game
import json

def run_test():
    runs = int(input("Kuinka monta peliä pelataan? Yksi peli kestää noin 30 - 60 sekuntia:\n"))
    game = Game(player=False, print_to_terminal=False, stop_when_win=True)

    games = {}
    wins = 0
    sq_wins = {}

    for i in range(runs):
        info = game.play()
        games[i] = info
        if info["win"]:
            wins += 1
        sq_wins[i] = wins / (i+1)
        print(f"Peli {i} valmis")

    with open("test_results.json", mode="w+") as file:
        json.dump(games, file, ensure_ascii=False, indent=4)

    with open("sq_wins.json", mode="w+") as file:
        json.dump(sq_wins, file, ensure_ascii=False, indent=4)
    print("Valmis!")

run_test()