# bracket-maker
This is a simple tool to pair any number of players into a bracket tournament and show the pairings.
Byes are inserted if the number of players isn't a power of two.

## Usage
Download `knockout.py` and run `./knockout.py player1 player2 player3 player4`.
You may need to change `python3` in line 1 to whatever command you use to run Python.

## Example
```
someone@computer ~ $ ./knockout.py player1 player2 player3 player4

player1 vs player4 ─┐
                    ├──   vs   ──
player2 vs player3 ─┘

```
