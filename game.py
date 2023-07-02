import copy
from items import Item
from random import shuffle
from queue import Queue, PriorityQueue


class CustomPriorityQueue(PriorityQueue):
    def _put(self, item):
        return super().put((self._get_priority(item), item))

    def _get(self):
        return super()._get()[1]

    def _get_priority(self, item):
        return item[0]


class Game:
    items = Item()

    item_type = items.select_items()

    visited = []

    goal = None

    def __init__(self):

        self.tubes = list()
        self.temp_tubes = list()
        self.capacity = 4  # int(input('Enter number of items of each tube: '))
        self.totalTubes = int(input('Enter number of total tubes (5-12): '))
        self.empty_tubes = int(input('Enter number of empty tubes (1-2): '))
        self.nstates = []

        self.count = 0

    def get_top(self, tube):
        return tube[-1]

    def same_color(self, s, d):
        return self.get_top(self.tubes[s]) == self.get_top(self.tubes[d])

    def display_tubes(self):
        """ Show Tubes as Columns """
        print()

        for i in range(self.capacity - 1, -1, -1):
            for j in range(len(self.tubes)):
                if len(self.tubes[j]) < i + 1:  # if the tube is empty
                    print('   -', end=' ')
                else:
                    tube = int(self.tubes[j][i])
                    print('  |' + self.items.types[self.item_type][tube], end='|')
            print()

        # print ------
        for tube in range(len(self.tubes)):
            print(f'   -', end=' ')

        print()

        # print number of tube
        for tube in range(len(self.tubes)):
            print(f'   {tube + 1}', end=' ')

        print()

    def check_status(self, tubes) -> bool:
        """ Checking Game Status """
        completed = True
        for tube in tubes:
            if not (len(set(tube)) < 2 and len(tube) in [0, self.capacity]):
                completed = False
                break
        return completed

    def new_game(self):
        """
            Initialize Tubes and Fill it
            with items for New Game
        """

        # Make a list of number
        listOfItems = list(''.join(
            [
                str(i) * self.capacity
                for i in range(self.totalTubes - self.empty_tubes)
            ]
        ))

        # rearrange the items
        shuffle(listOfItems)

        # 5 full - 2 empty
        listOfItems = ['0', '2', '0', '1', '0', '2', '2', '2', '1', '1', '0', '1']
        # 7 full - 2 empty
        # listOfItems = ['0', '2', '3', '0', '1', '0', '3', '2', '2', '2', '1', '3', '1', '0', '1', '3']

        self.tubes = [
            listOfItems[x * self.capacity: x * self.capacity + self.capacity]
            for x in range(self.totalTubes)
        ]

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
        s -= 1
        d -= 1
        if self.can_move(s, d):
            self.tubes[d].append(self.tubes[s].pop())

    def next_state(self, state):
        self.nstates.clear()

        for i in range(len(state.tubes)):
            for j in range(len(state.tubes)):
                new_state = copy.deepcopy(state)
                new_state.parent = state
                new_state.move(i, j)
                new_state.cost = state.cost + 1
                self.nstates.append(new_state)
        return self.nstates

    # def clone(self, state):
    #     return copy.deepcopy(state)

    def dfs(self, state):

        if state in self.visited:
            return 0

        self.count += 1

        if state.goal():
            state.display_tubes()
            # print(state.tubes)
            print(str(self.count) + '\n✌✨😍 You win 😍✨✌')
            return 1

        # print(state.tubes)
        state.display_tubes()

        self.visited.append(state)

        next_states = self.next_state(state)

        for s in next_states:
            if self.dfs(s) == 1:
                return 1

    def bfs(self, node):

        self.visited.append(node)

        queue = list()
        queue.append(node)

        while len(queue) > 0:
            cur_node = queue.pop(0)

            self.count += 1
            if cur_node.goal():
                cur_node.display_tubes()
                self.goal = cur_node
                print(cur_node.cost)
                print(str(self.count) + '\n✌✨😍 You win 😍✨✌')
                break

            for neighbor in self.next_state(cur_node):

                if neighbor not in self.visited:
                    # for v_state in self.visited:
                    #     if neighbor.tubes != v_state.tubes:
                    queue.append(neighbor)
                    neighbor.display_tubes()
                    # print(neighbor.tubes)
                    self.visited.append(neighbor)

                # if neighbor not in self.visited:
                #     queue.append(neighbor)
                #     print(neighbor.tubes)
                #     self.visited.append(neighbor.tubes)

    def ucs(self, node):

        self.visited.append(node)

        helper = 0
        queue = PriorityQueue()
        queue.put((0, helper, node))

        while not queue.empty():
            weight_cur_node, h, cur_node = queue.get()

            if cur_node.goal():
                cur_node.display_tubes()
                self.goal = cur_node
                break

            for state in self.next_state(cur_node):
                if state not in self.visited:
                    queue.put((state.cost, helper, state))
                    helper += 1
                    state.display_tubes()
                    self.visited.append(state)

    def print_path(self):
        """ print path of best solution """
        path = list()
        path_cost = self.goal.cost
        while self.goal.parent:
            path.append(self.goal)
            # self.goal.display_tubes()
            self.goal = self.goal.parent

        path.reverse()
        for x in path:
            x.display_tubes()
        print("\nCost of Solution: {}".format(path_cost))

    # def get_less_state_cost(self, queue):
    #     min_cost = queue[0].cost
    #     idx = 0
    #     for i, state in enumerate(queue):
    #         if state.cost < min_cost:
    #             min_cost = state.cost
    #             idx = i
    #     return queue[idx]

    # def heuristic(self, tubes):
    #     prior = 0  # store the cost of move
    #     cft = 0  # count of full tubes
    #     for idx, tube in enumerate(tubes):
    #         if len(set(tube)) > 1:
    #             if len(set(tube[:3])) == 1:
    #                 if len(tube) == self.capacity:
    #                     prior = prior + 2
    #                 else:
    #                     prior = prior + 1
    #             elif len(set(tube[:2])) == 1:
    #                 if len(tube) == self.capacity:
    #                     prior = prior + 3
    #                 elif len(tube) == self.capacity - 1:
    #                     prior = prior + 2
    #                 else:
    #                     prior = prior + 1
    #             else:
    #                 if len(tube) > 1:
    #                     prior = prior + len(tube)
    #                 elif len(tube) == 1:
    #                     prior = prior + 3
    #                 else:
    #                     prior = prior + self.capacity
    #         if len(tube) != 0:
    #             cft = cft + 1
    #     if cft > 3:
    #         cft = cft - 3
    #         prior = prior + cft
    #     return prior

    def heuristic(self, tubes):
        prior = 0  # store the cost of move
        for idx, tube in enumerate(tubes):
            if len(set(tube)) > 1:
                if len(set(tube[:3])) == 1:
                    if len(tube) == self.capacity:
                        prior = prior + 2
                    else:
                        prior = prior + 1
                elif len(set(tube[:2])) == 1:
                    if len(tube) == self.capacity:
                        prior = prior + 3
                    elif len(tube) == self.capacity - 1:
                        prior = prior + 2
                    else:
                        prior = prior + 1
                else:
                    if len(tube) > 1:
                        prior = prior + len(tube)
                    elif len(tube) == 1:
                        prior = prior + 3
                    else:
                        prior = prior + self.capacity

        return prior

    # def get_most_colored2(self, tube):
    #     prior = [0, '']  # 0
    #     if (len(tube) == self.capacity) and (len(set(tube)) > 1):
    #         if len(set(tube[:3])) == 1:
    #             prior = [1, tube[0]]  # 4
    #             return prior
    #         elif len(set(tube[:2])) == 1:
    #             prior = [2, tube[0]]  # 3
    #             return prior
    #         else:
    #             prior = [3, tube[0]]  # 2
    #             return prior
    #     elif len(set(tube)) == 0:
    #         prior = [0, '']  # 1
    #         return prior
    #     else:
    #         pass
    #         # prior = [0, ''] # 1
    #         # return prior
    #         # prior = [4, tube[0]] # 0
    #
    # def heuristic(self, state):
    #     # for i in range(len(state.tubes)):
    #     # for idx, tube in enumerate(state.tubes):
    #     #     prior = self.get_most_colored(tube)
    #     hhh = 0
    #     i = 0
    #     for idx, tube in enumerate(state.tubes):
    #         prior, dist_idx, color = self.get_most_colored(state.tubes, idx)
    #         # prior, color = self.get_most_colored(state.tubes, idx)
    #         distance = 0
    #         if prior != 0 and color != 0:
    #             xx = tube.index(color)
    #             distance = (3 - xx) + 1
    #             hhh = distance / prior
    #             i = idx
    #     return [i, hhh]

    # def first_dif_in_seq_color(self, tube):
    #     dif = tube[0]
    #     for i in range(len(tube)):
    #         if dif != tube[i]:
    #             return i
    #
    # def heuristic2(self, state):
    #     # for i in range(len(state.tubes)):
    #     # for idx, tube in enumerate(state.tubes):
    #     #     prior = self.get_most_colored(tube)
    #     hhh = 0
    #     i = 0
    #     for idx, tube in enumerate(state.tubes):
    #         # prior, dist_idx, color = self.get_most_colored(state.tubes,idx)
    #         # prior, color = self.get_most_colored(state.tubes, idx)
    #         distance = 0
    #         # if prior != 0 and color != 0:
    #         if len(tube) != 0:
    #             xx = tube.index(tube[self.first_dif_in_seq_color(tube)])
    #             distance = (3 - xx) + 1
    #         # hhh = distance / prior
    #         # i = idx
    #     return distance

    def hill_climbing(self, node):
        self.visited.append(node)

        helper = 0
        queue = PriorityQueue()
        queue.put((0, helper, node))

        while not queue.empty():
            weight_cur_node, h, cur_node = queue.get()

            self.count += 1
            if cur_node.goal():
                cur_node.display_tubes()
                self.goal = cur_node
                print(cur_node.cost)
                print(str(self.count) + '\n✌✨😍 You win 😍✨✌')
                break

            for state in self.next_state(cur_node):
                if state not in self.visited:
                    queue.put((self.heuristic(state.tubes), helper, state))
                    helper += 1
                    state.display_tubes()
                    self.visited.append(state)

    def a_star(self, node):
        self.visited.append(node)

        helper = 0
        queue = PriorityQueue()
        queue.put((0, helper, node))

        while not queue.empty():
            weight_cur_node, h, cur_node = queue.get()

            self.count += 1
            if cur_node.goal():
                cur_node.display_tubes()
                self.goal = cur_node
                print(cur_node.cost)
                print(str(self.count) + '\n✌✨😍 You win 😍✨✌')
                break

            for state in self.next_state(cur_node):
                if state not in self.visited:
                    queue.put((state.cost + self.heuristic(state.tubes), helper, state))
                    helper += 1
                    state.display_tubes()
                    self.visited.append(state)
