"""Some Helper Functions."""


def get_puzzle_input(path):
    """Get the puzzle input."""
    with open(path) as f:
        puzzle_input = f.read().splitlines()

    return puzzle_input


def print_answers(puzzle_input, solve_part1, solve_part2, test=False):
    """Get answers for both parts of the puzzle."""
    answer1 = solve_part1(puzzle_input)
    answer2 = solve_part2(puzzle_input)
    if test:
        print('Test:')
    print('Part 1:', answer1, 'Part 2:', answer2)
