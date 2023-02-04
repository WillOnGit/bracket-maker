#!/usr/bin/env python3


import sys, random, math


# get players from command line arguments
players = sys.argv[1:]
num_players = len(players)

# need at least two players
if num_players < 2:
    print('Not enough players')
    sys.exit(1)

# helper for placing byes
def byeSequence(rounds, byes):
    if byes >= 2 ** rounds // 2:
        raise RuntimeError('Too many byes for this number of rounds')

    bye_placements = []
    index = 1
    for x in range(byes):
        for y in range(rounds - 1):
            if x % (2 ** y) == 0:
                index = index ^ (2 ** (rounds - y - 1))
        bye_placements.append(index)

    return sorted(bye_placements)

# find how many rounds and byes we need
rounds = math.ceil(math.log2(num_players))
num_pseudoplayers = 2 ** rounds
byes = num_pseudoplayers - len(players)

# make the pairings
# shuffle players and insert byes
random.shuffle(players)
for x in byeSequence(rounds,byes):
    players.insert(x,'bye')

# create match tuples from new player list
matchups = [(players[2*x], players[2*x+1]) for x in range(num_pseudoplayers//2)]

# find display width of first round
width = 0
for x in matchups:
    width = max(width,len(x[0])+len(x[1])+6)

# print tournament
print()
open_lines = [0 for x in range(rounds)]
for x in range(num_pseudoplayers - 1):
    # calculate the indentation
    indent = 0
    while (x + 1) & (2 ** indent) == 0:
        indent += 1

    # check how to draw the match line, if needed
    if indent != rounds - 1:
        if open_lines[indent]:
            end_char = '┘'
            open_lines[indent] ^= 1
        else:
            end_char = '┐'
            open_lines[indent] ^= 1
        # check if we need to draw other lines on this row
        lines = ''
        if any(open_lines[indent + 1:]):
            for y in open_lines[indent + 1:]:
                lines += ' ' * 12
                if y:
                    lines += '│'
                else:
                    lines += ' '
    else:
        end_char = ''
        lines = ''

    # print the match and any parts of the chart
    if indent == 0:
        print(f'{matchups[x//2][0]} vs {matchups[x//2][1]} ─'.ljust(width,'─') + end_char + lines)
    else:
        print(' ' * width + ' ' * (13 * (indent - 1)) + '├──   vs   ──' + end_char + lines)

print()
