class Item:
    """ Group Shapes to play game with """

    def __init__(self):
        self.types = {
            1: 'RGBADEFHI',  # Letters
            2: '❤💚💙💛💜🤍🤎🖤🧡',  # Hearts
            3: '123456789',  # Chest
        }

    def select_items(self) -> int:
        print("\nAvailable Types to fill tubes with:")
        for i, item in self.types.items():
            print(i, ') ', '-'.join(item))

        choice = int(input(f'select a set (1-{len(self.types)}): '))
        print('\n')
        print('The Group which you selected is:\n', ' '.join(self.types[choice]))
        return choice
