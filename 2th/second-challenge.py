""" usage: second-challenge.py [-h] <filename> """

from typing import List
import argparse

def safe_report(levels: List):
    """ return True when either asc or desc with 1 <= diff <= 3 """

    mode = levels[1] > levels[0]
    last_level = levels[0]
    for level in levels[1:]:
        diff = abs(level - last_level)
        if diff == 0 or diff > 3 or \
            (mode and level < last_level) or \
            (not mode and level > last_level):
            
            return False

        last_level = level

    return True

def safe_report_with_dampener(levels: List):
    """ return True when either asc or desc with 1 <= diff <= 3 """

    for i in range(len(levels)):
        new_levels = levels.copy()
        new_levels.pop(i)

        if safe_report(new_levels):
            return True
    
    return safe_report(levels)

def main(filename: str):
    """ read input and calculate how many reports are safe """

    # load data into pd dataframe
    with open(filename, mode='r') as file:
        reports = list(list(int(level) for level in report.split(' '))
                       for report in file.readlines())
    
    safe_reports = list(report for report in reports if safe_report(report))
    print('safe reports:', len(safe_reports))

    safe_reports = list(report for report in reports if safe_report_with_dampener(report))
    print('safe reports (with dampener):', len(safe_reports))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Day 2: Red-Nosed Reports')

    parser.add_argument('filename', help='Input file')

    main(**vars(parser.parse_args()))
