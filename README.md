Hanabi
=====================

This is a program that plays [Hanabi](https://boardgamegeek.com/boardgame/98778/hanabi).

A sample (stupid) AI is provided in the directory `dummy`.


Performance
---------------------

Here are the average scores and win rates for the standard 50-card deck (5 colors) and for the "black" 55-card variant (6 colors, where the 6th color has 1 copy of each card).

**Average scores**



**Win rates**



Requirements
---------------------
* Python >= 3.7
* The `termcolor` Python module (install command: `pip install termcolor`)
* The `blessings` Python module (install command: `pip install blessings`)

Run a new game
---------------------
`python run_game.py`

**Command line options**
* `-n NUM_PLAYERS` set number of players (default is 5)
* `-a AI_DIRECTORY` choose AI (default is `alphahanabi`)
* `-p DIFFICULTY` choose difficulty level for `alphahanabi` (possible values: `moderate`, `hard`, `hardest`; default is `hardest`)
* `-c` run the game without pausing (otherwise, by default, each new turn is played by pressing ENTER)
* `-s` activate the strategy log
* `-t` print a shorter log of turns and status
* `-l FILE_NAME` load the initial deck from the given file (otherwise, by default, the initial deck is shuffled randomly)
* `-d FILE_NAME` dump the initial deck to the given file (default is `deck.txt`)
* `-r SCORE` run many games, until a score <= to the given score is reached
* `-i` run in interactive mode
* `-q` quit immediately after showing the initial cards (not in interactive mode)



Run many games and print statistics
---------------------
`python test.py`

or (much faster)`pypy test.py`

**Command line options**
* `-n NUM_PLAYERS` set number of players (default is 5)
* `-m NUM_GAMES` set number of games (default is 1000)
* `-a AI_DIRECTORY` choose AI (default is `alphahanabi`)
* `-p DIFFICULTY` choose difficulty level for `alphahanabi` (possible values: `moderate`, `hard`, `hardest`; default is `hardest`)
* `-d DECK_TYPE` choose deck type (possible values: `standard` for the standard 50-card deck, `black` for the 55-card deck)



Challenge QuickStart
---------------------
First run, saving the deck and seeing the cards:

`python run_game.py -d FILE_NAME -q`

Second run, loading the deck and running the game without showing cards:

`python run_game.py -l FILE_NAME -p DIFFICULTY -t -i`
