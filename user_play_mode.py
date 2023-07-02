import sys  # for exit game

from game import Game

if __name__ == '__main__':
    print('\n' + '-' * 19)
    print('| Ball Sort Puzzle |')
    print('-' * 19)

    game = Game()
    game.new_game()
    game.display_tubes()

    while True:
        try:
            sTube = int(input('* Choose a tube to move from (Source)   : '))

            # game.get_possible_moves(sTube - 1)

            dTube = int(input('* Choose a tube to move to (Destination): '))

            game.move(sTube, dTube)

            # print('-' * 40)
        except Exception or ValueError:
            option = input('(R) for restart / (Q) for quit? ')
            while not option.lower() in ['r', 'q']:
                option = input('Try again!\n(R) for restart / (Q) for quit? ')
            if option == 'r':
                print('Restarting the game 😴')
                game.tubes = list(game.temp_tubes)
            elif option == 'q':
                print('\nGoodbye 👋,\nsee you soon...')
                print('Developed by Ashraf Ⓒ')
                sys.exit(0)

        # clear_screen
        game.display_tubes()

        if game.check_status(game.tubes):
            print('\n✌✨😍 You win 😍✨✌')
            break
