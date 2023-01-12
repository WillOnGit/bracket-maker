import sys, random, math


players = sys.argv[1:]
num_players = len(players)

# need at least two players
if num_players < 2:
    print("Not enough players")
    sys.exit(1)

# find how many rounds we need
rounds = math.ceil(math.log2(num_players))

num_pseudoplayers = 2 ** rounds

byes = num_pseudoplayers - len(players) 

print("------------")
for x in range(num_players):
    chosen_player = random.choice(players)
    players.remove(chosen_player)
    print(chosen_player)

for x in range(byes):
    print("bye")
print("------------")
