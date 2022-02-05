from game import Game

runs = 10
game = Game(player=False, print_to_terminal=False)
wins = 0

for i in range(runs):
    info = game.play()
    if info[3] >= 2048:
        wins += 1
    print(f"{i} - Siirrot: {info[0]}, Pisteet: {info[1]}, Aika: {info[2]}, Suurin Laatta: {info[3]}")

print(f"Voitot: {wins} ({100*(wins/runs)} %)")