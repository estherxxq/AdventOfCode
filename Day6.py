"""Solve Day 6."""

from general import get_puzzle_input, print_answers


def update_banks(banks):
    """
    Update storage situation in banks (works).

    Input (list of int):
        current state of banks.

    Output (list of int):
        updated state of banks.
    """
    # Find the max storage, and the first bank with it
    current_max = max(banks)
    max_index = banks.index(current_max)

    # Hold its storage outside, so now it has 0
    hold = current_max
    new_banks = banks
    new_banks[max_index] = 0

    while hold > 0:
        for i in range(max_index+1, len(new_banks)):
            if hold == 0:
                break
            else:
                new_banks[i] += 1
                hold -= 1

        for i in range(0, max_index+1):
            if hold == 0:
                break
            else:
                new_banks[i] += 1
                hold -= 1

    return new_banks


def make_pattern(current_pattern):
    """
    Convert list of banks pattern into a string.

    Input (a list of int): a pattern of banks, formatted as [0, 1, 2]
    Output (a string): a pattern of banks, formatted as '012'
    """
    pattern = ''.join([str(b) for b in current_pattern])
    return pattern


def solve_part1(puzzle_input):
    """Get answer for part 1."""
    try:
        banks = [int(bank) for bank in puzzle_input[0].split('\t')]
    except:
        banks = puzzle_input

    existing_patterns = []
    current_pattern = banks
    existing_patterns.append(make_pattern(current_pattern))

    cont = True

    print('start here')
    while cont:
        next_pattern = update_banks(current_pattern)
        cp = make_pattern(next_pattern)

        if cp in existing_patterns:
            cont = False
        else:
            existing_patterns.append(cp)

        current_pattern = next_pattern

    return len(existing_patterns)


def solve_part2(puzzle_input):
    """Get answer for part 2."""
    try:
        banks = [int(bank) for bank in puzzle_input[0].split('\t')]
    except:
        banks = puzzle_input

    existing_patterns = []
    current_pattern = banks
    existing_patterns.append(make_pattern(current_pattern))

    cont = True

    while cont:
        next_pattern = update_banks(current_pattern)
        cp = make_pattern(next_pattern)

        if cp in existing_patterns:
            cont = False
            first = existing_patterns.index(cp)
            print(first)
        else:
            existing_patterns.append(cp)

        current_pattern = next_pattern

    return len(existing_patterns) - first


if __name__ == '__main__':
    test_inputs = [0, 2, 7, 0]
    print_answers(test_inputs, solve_part1, solve_part2, test=True)

    path = 'data/Day6input.txt'
    print_answers(get_puzzle_input(path), solve_part1, solve_part2)
