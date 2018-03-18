"""Solve Day4 (it works)."""


from general import get_puzzle_input, print_answers


def check_repetitive(pass_phrase):
    """
    Check if a pass phrase contains repetitive words.

    Input(string):
    A pass_phrase

    Output(boolean):
    True if it doesn't contain repetitive words, False otherwise
    """
    is_valid = False

    words = pass_phrase.split(' ')
    if len(words) == len(set(words)):
        is_valid = True

    return is_valid


def check_anagram(pass_phrase):
    """
    Check whether a word is the anagram of another word in a pass phrase.

    This is done by converting each word in a phrase into a
    sorted list of letters, then back into one string,
    and then checking for repetition within the phrase.

    Input(string):
    A pass phrase

    Output(boolean):
    True if it doesn't contain anagrams, False otherwise
    """
    no_anagram = False

    words = pass_phrase.split(' ')
    sorted_words = [''.join(sorted(list(word))) for word in words]

    if len(sorted_words) == len(set(sorted_words)):
        no_anagram = True

    return no_anagram


def solve_part1(puzzle_input):
    """Solve part 1 (works)."""
    valid_phrases = []

    for pass_phrase in puzzle_input:
        if check_repetitive(pass_phrase):
            valid_phrases.append(pass_phrase)

    return len(valid_phrases)


def solve_part2(puzzle_input):
    """Solve part 2 (works)."""
    valid_phrases = []

    for pass_phrase in puzzle_input:
        if check_anagram(pass_phrase):
            valid_phrases.append(pass_phrase)

    return len(valid_phrases)


if __name__ == '__main__':
    path = 'data/Day4input.txt'
    print_answers(get_puzzle_input(path), solve_part1, solve_part2)
