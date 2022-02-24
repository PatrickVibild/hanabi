from __future__ import absolute_import
from __future__ import print_function
import sys

from game.game import Game
from six.moves import input


if __name__ == "__main__":
    # default values
    ai = "dummy"
    ai_params = {}
    wait_key = True
    num_players = 5
    log = True
    strategy_log = False
    dump_deck_to = "deck.txt"
    load_deck_from = None
    short_log = False
    interactive = False
    quit_immediately = False
    
    repeat = None  # repeat until a bad result is reached
    
    # read options
    if '-a' in sys.argv[1:]:
        # select AI to be used
        i = sys.argv.index('-a')
        assert len(sys.argv) >= i+2
        ai = sys.argv[i+1]
    
    if '-c' in sys.argv[1:]:
        wait_key = False
    
    if '-s' in sys.argv[1:]:
        strategy_log = True
    
    if '-t' in sys.argv[1:]:
        short_log = True
    
    if '-l' in sys.argv[1:]:
        # load deck from file
        i = sys.argv.index('-l')
        assert len(sys.argv) >= i+2
        load_deck_from = sys.argv[i+1]
    
    if '-d' in sys.argv[1:]:
        # dump deck to file
        i = sys.argv.index('-d')
        assert len(sys.argv) >= i+2
        dump_deck_to = sys.argv[i+1]
    
    if '-n' in sys.argv[1:]:
        # read number of players
        i = sys.argv.index('-n')
        assert len(sys.argv) >= i+2
        num_players = int(sys.argv[i+1])
    
    if '-r' in sys.argv[1:]:
        # repeat until a bad score is reached
        i = sys.argv.index('-r')
        assert len(sys.argv) >= i+2
        repeat = int(sys.argv[i+1])
    
    if '-i' in sys.argv[1:]:
        # run in interactive mode
        interactive = True
    
    if '-p' in sys.argv[1:]:
        # set difficulty parameter
        i = sys.argv.index('-p')
        assert len(sys.argv) >= i+2
        ai_params['difficulty'] = sys.argv[i+1]
    
    if '-q' in sys.argv[1:]:
        # quit immediately after showing the initial cards
        quit_immediately = True
    
    counter = 0
    while True:
        # run game
        print("Starting game with %d players..." % num_players)
        print()
        game = Game(
                num_players=num_players,
                ai=ai,
                ai_params=ai_params,
                strategy_log=strategy_log,
                dump_deck_to=dump_deck_to,
                load_deck_from=load_deck_from
        )

        game.setup()
        
        if interactive:
            # run in interactive mode
            from blessings import Terminal
            
            def print_main(term, num_players, ai, ai_params, short_log, turn=None, current_player=None, statistics=None):
                """
                Print main view.
                """
                CURSOR_Y = term.height - 15
                
                # clear everything
                print(term.clear())
                
                # move cursor
                print(term.move_y(CURSOR_Y))
                
                with term.location(y=0):
                    print(term.bold("Hanabi game"))
                
                with term.location(y=2):
                    print("Number of players: %d" % num_players)
                    print("AI: %s" % ai)
                    if "difficulty" in ai_params:
                        print("Difficulty: %s" % ai_params["difficulty"])
                    if load_deck_from is not None:
                        print("Deck file: %s" % load_deck_from)
                
                if turn is not None:
                    # log turn
                    with term.location(y=7):
                        if short_log:
                            game.log_turn_short(turn, current_player)
                        else:
                            game.log_turn(turn, current_player)
                    
                    # log status
                    with term.location(y=9):
                        if short_log:
                            game.log_status_short()
                        else:
                            game.log_status()
                
                if statistics is not None:
                    # game ended
                    with term.location(y=9+10):
                        print(term.bold("Game ended"))
                        print(statistics)
            
            
            term = Terminal()
            with term.fullscreen():
                print_main(term, num_players, ai, ai_params, short_log)
                
                for current_player, turn in game.run_game():
                    if wait_key:
                        cmd = input(":")
                        if cmd in ["c", "continue"]:
                            wait_key = False
                    
                    print_main(term, num_players, ai, ai_params, short_log, turn=turn, current_player=current_player)
                    
                
                statistics = game.statistics
                print_main(term, num_players, ai, ai_params, short_log, turn=turn, current_player=current_player, statistics=statistics)
                
                while True:
                    cmd = input(":")
                    print_main(term, num_players, ai, ai_params, short_log, turn=turn, current_player=current_player, statistics=statistics)
                    
                    if cmd in ["q", "quit"]:
                        break
                    
                    else:
                        with term.location(y = term.height - 4):
                            # print "Unknown command \"%s\"" % cmd
                            pass
        
        
        else:
            # non-interactive mode
            if dump_deck_to is not None:
                print("Dumping initial deck to %s" % dump_deck_to)
            
            if not short_log:
                game.log_deck()
                game.log_status()
            
            if quit_immediately:
                break
            
            # now run the game
            for current_player, turn in game.run_game():
                if wait_key:
                    input()
                
                if short_log:
                    game.log_turn_short(turn, current_player)
                    game.log_status_short()
                else:
                    game.log_turn(turn, current_player)
                    game.log_status()
            
            statistics = game.statistics
            print(statistics)
        
        
        counter += 1
        
        if repeat is None:
            break
        
        elif statistics.score <= repeat:
            print("Reached score <= %d after %d games" % (repeat, counter))
            break
        
        else:
            print()
            print("==========================")
            print()


