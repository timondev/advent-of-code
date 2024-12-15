""" usage: third-challenge.py [-h] <filename> """

import re
import argparse

is_enabled = True
mul_regex = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
op_regex = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't|do")

def evaluate_instruction(instruction: str) -> int:
    """ evaluate instructions like mul, do & don't """
    global is_enabled

    if instruction == "don't":
        is_enabled = False
    elif instruction == 'do':
        is_enabled = True
    elif is_enabled:
        f, s = mul_regex.match(instruction).groups()
        return int(f) * int(s)

    return 0

def main(filename: str):
    """ read input and sum valid enabled instructions """

    # load data into pd dataframe
    with open(filename, mode='r') as file:
        print('result:', sum(
            evaluate_instruction(instruction) 
            for instruction 
            in op_regex.findall(file.read())))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Day 3: Mull It Over')

    parser.add_argument('filename', help='Input file')

    main(**vars(parser.parse_args()))
