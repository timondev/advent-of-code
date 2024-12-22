import argparse
import pandas as pd
import numpy as np

def main(input_file):
    '''
    --- Day 1: Historian Hysteria ---
    Pair up the smallest number in the left list with the smallest number
    in the right list, then the second-smallest left number with the
    second-smallest right number, and so on.

    Within each pair, figure out how far apart the two numbers are.
    you'll need to add up all of those distances.
    '''

    with open(input_file, mode='r', encoding='utf-8') as io_wrapper:
        df = pd.read_csv(
            io_wrapper.buffer,
            sep='   ',
            names=['first', 'second'],
            engine='python'
        )

        # sort input data in ascending order
        for column in df:
            df[column] = df[column].sort_values(ignore_index=True)

    total_distance = np.sum(np.abs(df['first'] - df['second']))
    print('Total distance between lists:', total_distance)

    '''
    --- Part Two ---
    This time, you'll need to figure out exactly how often each number from
    the left list appears in the right list. Calculate a total similarity
    score by adding up each number in the left list after multiplying it by
    the number of times that number appears in the right list.
    '''

    total_similarity = sum(n * np.sum(df['second'] == n) for n in df['first'])
    print('Total similarity between lists:', total_similarity)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate total & similarity distance of numbered lists',
        epilog='Advent of Code 2024 - Day 1: Historian Hysteria'
    )
    parser.add_argument('input_file')
    main(**vars(parser.parse_args()))
