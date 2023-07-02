def h(mylist, sidx):
	dist=0
	for idx, item in enumerate(mylist):
		if idx != sidx:
			xx = item.index(idx)
			dist = (3 - xx) + 1
	return dist
			


def get_most_colored(list, cap=4):
    prior = 0
    if len(set(list)) > 1:
        if len(set(list[:3])) == 1:
            prior = [3, list[0]]
        elif len(set(list[:2])) == 1:
            prior = [2, list[0]]
        else:
            prior = [1, list[0]]
    return prior


if __name__ == '__main__':

    my_list = [
        ['G', 'G', 'G', 'R'],
        ['B', 'G', 'B', 'R'],
        ['R', 'R', 'B', 'B'],
        [],
        []
    ]

    print(my_list[:3])

    # print(set(my_list[:3]))

    # print(len(set(['B'])))
    print(len(set(my_list[1][:3])))
    for item in my_list:
      print(set(item))

    for item in my_list:
        prior = get_most_colored(item)

        distance = 0

        if prior != 0:
            xx = item.index(prior[1])
            distance = (3 - xx) + 1
        # for li in my_list:
        #     if 'G' in li:

        if prior != 0:
            print('-' * 40)
            print(prior[0] / distance)

    # x = prior / distance
    # if state.x > cur_state.x:

# if (len(set(tube)) < capacity):
