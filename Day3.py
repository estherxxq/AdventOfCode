"""Solve Day 3 of Advent of Code (it works)."""


def solve_part2(puzzle_input=361527):
    """Get answer for part 2 of the puzzle."""
    first_num = 1
    first_coordinates = (0, 0)

    existing = {}
    cardinals = {'east': (1, 0, 'north'),
                 'north': (0, 1, 'west'),
                 'west': (-1, 0, 'south'),
                 'south': (0, -1, 'east')
                 }

    current_num = first_num
    current_coordinates = first_coordinates
    current_direction = 'east'

    def find_turn(step):
        """Find whether it's time to make a turn."""
        check_point = 0
        current = 1
        while check_point <= step:
            for i in range(2):
                check_point += current
                if check_point == step:
                    return True
            current += 1
        return False

    existing[current_coordinates] = current_num

    while current_num < puzzle_input:
        # get new coordinates
        new_coordinates = (current_coordinates[0] +
                           cardinals[current_direction][0],
                           current_coordinates[1] +
                           cardinals[current_direction][1])
        # get neighbours
        neighbours = []
        for coordinates, num in existing.items():
            if abs(coordinates[0]-new_coordinates[0]) <= 1 and \
               abs(coordinates[1]-new_coordinates[1]) <= 1:
                neighbours.append(num)

        # get new numbers
        new_num = sum(neighbours)

        # save new number and coordinates
        existing[new_coordinates] = new_num

        # determine if we are turning
        turn = find_turn(len(existing)-1)
        print(new_num, new_coordinates, 'neighbours:',
              neighbours, 'turn:', turn)

        # change direction if turning
        if turn:
            current_direction = cardinals[current_direction][2]

        # update current number and coordinates
        current_num = new_num
        current_coordinates = new_coordinates

    print(current_num)


if __name__ == '__main__':
    solve_part2(361527)  # answer is 363010
