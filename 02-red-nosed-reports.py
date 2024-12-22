import argparse
import pandas as pd
import numpy as np

def is_safe_report(report: pd.Series) -> bool:
    ''' check if report is safe '''

    # check if report is steadily increasing or decreasing
    if not report.is_monotonic_increasing \
            and not report.is_monotonic_decreasing:
        return False

    # check if any diff (distances) are outside of 0 < d < 4
    if any(
        not pd.isna(d) and (abs(d) > 3 or abs(d) < 1)
        for d in report.diff()
    ):
        return False

    return True

def main(input_file):
    '''
    --- Day 2: Red-Nosed Reports ---
    The engineers are trying to figure out which reports are safe. The
    Red-Nosed reactor safety systems can only tolerate levels that are
    either gradually increasing or gradually decreasing. So, a report
    only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    '''

    with open(input_file, mode='r', encoding='utf-8') as io_wrapper:
        reports = list(
            pd.Series(line.split(), dtype=pd.Int32Dtype())
            for line in io_wrapper.readlines()
        )

    safe_reports = list(filter(is_safe_report, reports))
    print('Total safe reports:', len(safe_reports))

    '''
    --- Part Two ---
    The Problem Dampener is a reactor-mounted module that lets the reactor
    safety systems tolerate a single bad level in what would otherwise be a
    safe report. It's like the bad level never happened!
    '''

    safe_reports = list(
        report for report in reports
        if any(is_safe_report(report.drop(index)) for index in report.index)
    )
    print('Total safe reports with dampening:', len(safe_reports))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate safe reports',
        epilog='Advent of Code 2024 - Day 2: Red-Nosed Reports'
    )
    parser.add_argument('input_file')
    main(**vars(parser.parse_args()))
