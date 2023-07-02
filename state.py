import game


class States:
    capacity = 4

    def __init__(self, tubes, parent, cost):
        self.tubes = tubes
        self.parent = parent
        self.cost = cost

    def can_move(self, s, d):
        # Check if movement in range of tubes numbers
        if s > len(self.tubes) or d > len(self.tubes):
            return False

        # if you are not move from an empty tube or move to a full tube
        elif len(self.tubes[s]) > 0 and len(self.tubes[d]) < self.capacity:
            # Destination: empty tube
            if len(self.tubes[d]) == 0:
                return True
            # if Destination have same color on top
            elif self.tubes[s][-1] == self.tubes[d][-1]:
                return True
            else:
                return False
        else:
            return False

    def move(self, s, d):
        if self.can_move(s, d):
            self.tubes[d].append(self.tubes[s].pop())
            return True
        return False

    def goal(self) -> bool:
        """ Checking Game Status """
        completed = True
        for tube in self.tubes:
            if not (len(set(tube)) < 2 and len(tube) in [0, States.capacity]):
                completed = False
                break
        return completed

    def __eq__(self, other):
        return self.tubes == other.tubes

    def display_tubes(self):
        """ Show Tubes as Columns """
        print()

        for i in range(self.capacity - 1, -1, -1):
            for j in range(len(self.tubes)):
                if len(self.tubes[j]) < i + 1:  # if the tube is empty
                    print('   -', end=' ')
                else:
                    tube = int(self.tubes[j][i])
                    print('  |' + game.Game.items.types[game.Game.item_type][tube], end='|')
            print()

        # print ------
        for tube in range(len(self.tubes)):
            print(f'   -', end=' ')

        print()

        # print number of tube
        for tube in range(len(self.tubes)):
            print(f'   {tube + 1}', end=' ')

        print()
