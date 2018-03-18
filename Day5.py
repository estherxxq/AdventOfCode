"""Solve Day 5 (works)."""

from general import get_puzzle_input, print_answers


def solve_part1(puzzle_input):
    """Get answer for part 1 (works)."""
    instructions = [int(i) for i in puzzle_input]
    position = 0
    step_count = 0

    while 1:
        try:
            step = instructions[position]
            instructions[position] += 1

            position += step

            step_count += 1
        except IndexError:
            break

    return step_count


def solve_part2(puzzle_input):
    """Get answer for part 2 (works)."""
    instructions = [int(i) for i in puzzle_input]
    position = 0
    step_count = 0

    while 1:
        try:
            step = instructions[position]
            if step < 3:
                instructions[position] += 1
            else:
                instructions[position] -= 1

            position += step

            step_count += 1
        except IndexError:
            break

    return step_count


if __name__ == '__main__':
    test_inputs = [0, 3, 0, 1, -3]
    print_answers(test_inputs, solve_part1, solve_part2, test=True)

    path = 'data/Day5input.txt'
    print_answers(get_puzzle_input(path), solve_part1, solve_part2)
