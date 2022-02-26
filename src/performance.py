from game import Game

runs = int(input("Kuinka monta peliä pelataan? Yksi peli kestää noin 20 - 60 sekuntia:\n"))

game = Game(player=False, print_to_terminal=False, stop_when_win=False)
WINS = 0

for i in range(runs):
    info = game.play()
    if info[3] >= 2048:
        WINS += 1
    print(f"""{i} - Siirrot: {info[0]
                }, Pisteet: {info[1]
                }, Aika: {info[2]
                }, Suurin Laatta: {info[3]
                }""")

print(f"Voitot: {WINS} ({100*(WINS/runs)} %)")
