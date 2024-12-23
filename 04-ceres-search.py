from itertools import product
import argparse
import numpy as np

def count_pattern(input_array, pattern):
    ''' counts how many times pattern appears, initial code by Jundiaius '''

    count = 0
    is_wildcard = pattern == '?'

    shape_difference = [i_s - p_s for i_s, p_s in zip(input_array.shape, pattern.shape)]
    dimension_iterators = [range(0, s_diff + 1) for s_diff in shape_difference]

    # This loop will iterate over every possible "window" given the shape of the pattern
    for start_indexes in product(*dimension_iterators):
        range_indexes = list(
            slice(start_i, start_i + p_s)
            for start_i, p_s in zip(start_indexes, pattern.shape)
        )
        
        input_match_candidate = input_array[*range_indexes]

        # This checks that for the current "window" - the candidate - every element is equal 
        #  to the pattern OR the element in the pattern is a wildcard
        if np.all(
            np.logical_or(
                is_wildcard, input_match_candidate == pattern
            )
        ):
            count += 1

    return count

def main(input_file):
    '''
    --- Day 4: Ceres Search ---
    As the search for the Chief continues, a small Elf who lives on the
    station tugs on your shirt; she'd like to know if you could help her
    with her word search (your puzzle input). She only has to find one
    word: XMAS.

    This word search allows words to be horizontal, vertical, diagonal,
    written backwards, or even overlapping other words. It's a little
    unusual, though, as you don't merely need to find one instance of
    XMAS - you need to find all of them. 
    '''

    with open(input_file, mode='r', encoding='utf-8') as io_wrapper:
        df = np.array(list(list(line.strip()) for line in io_wrapper.readlines()))

    patterns = [
        [['X', 'M', 'A', 'S']],
        [['S', 'A', 'M', 'X']],
        [['X'], ['M'], ['A'], ['S']],
        [['S'], ['A'], ['M'], ['X']],
        [['X', '?', '?', '?'], ['?', 'M', '?', '?'], ['?', '?', 'A', '?'], ['?', '?', '?', 'S']],
        [['S', '?', '?', '?'], ['?', 'A', '?', '?'], ['?', '?', 'M', '?'], ['?', '?', '?', 'X']],
        [['?', '?', '?', 'X'], ['?', '?', 'M', '?'], ['?', 'A', '?', '?'], ['S', '?', '?', '?']],
        [['?', '?', '?', 'S'], ['?', '?', 'A', '?'], ['?', 'M', '?', '?'], ['X', '?', '?', '?']],
    ]

    xmas = sum(count_pattern(df, np.array(pattern))for pattern in patterns)
    print('XMAS appeared:', xmas)

    '''
    --- Part Two ---
    Looking for the instructions, you flip over the word search to find that
    this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're
    supposed to find two MAS in the shape of an X.
    '''

    patterns = [
        [['M', '?', 'M'], ['?', 'A', '?'], ['S', '?', 'S']],
        [['M', '?', 'S'], ['?', 'A', '?'], ['M', '?', 'S']],
        [['S', '?', 'M'], ['?', 'A', '?'], ['S', '?', 'M']],
        [['S', '?', 'S'], ['?', 'A', '?'], ['M', '?', 'M']],
    ]

    xmas = sum(count_pattern(df, np.array(pattern))for pattern in patterns)
    print('X-MAS appeared:', xmas)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate xmas',
        epilog='Advent of Code 2024 - Day 4: Ceres Searchs'
    )
    parser.add_argument('input_file')
    main(**vars(parser.parse_args()))
