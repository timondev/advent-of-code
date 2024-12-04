""" usage: first-challenge.py [-h] <filename> """

import argparse
import pandas as pd
import numpy as np


def main(filename: str):
    """ read input and generate difference & similarity numbers """

    # load data into pd dataframe
    locations = pd.read_csv(
        filename,
        delimiter='   ',
        names=['first', 'second'],
        dtype={'first': np.int32, 'second': np.int32},
        engine='python')

    # sort columns independently
    for column in locations:
        locations[column] = locations[column].sort_values(ignore_index=True)

    # print sum of combined absolute differences between columns
    differnce = np.sum(np.abs(locations['first'] - locations['second']))
    print('difference:', differnce)

    # get counter for each unique number in second list
    nums = dict(zip(*np.unique(locations['second'], return_counts=True)))

    # print sum of combined similarity score
    similarity = np.sum([num * nums[num]
                        for num in locations['first'] if num in nums])
    print('similarity:', similarity)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Day 1: Historian Hysteria')

    parser.add_argument('filename', help='Input file')

    main(**vars(parser.parse_args()))
