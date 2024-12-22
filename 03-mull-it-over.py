import re
import argparse

def main(input_file):
    '''
    --- Day 3: Mull It Over ---
    It does that with instructions like mul(X,Y), where X and Y are each 1-3
    digit numbers.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like
    part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34),
    or mul ( 2 , 4 ) do nothing. Scan the corrupted memory for uncorrupted
    mul instructions. What do you get if you add up all of the results of
    the multiplications?
    '''

    compiler = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    with open(input_file, mode='r', encoding='utf-8') as io_wrapper:
        code = io_wrapper.read().replace('\n', '')
        operations = list(compiler.finditer(code))

    result = sum(int(op[1]) * int(op[2]) for op in operations)
    print('program result:', result)

    '''
    --- Part Two ---
    There are two new instructions you'll need to handle:

    - The do() instruction enables future mul instructions.
    - The don't() instruction disables future mul instructions.
    '''
    
    result = sum(
        int(op[1]) * int(op[2])
        for op in operations
        if code.rfind("don't()", None, op.start()) \
            <= code.rfind("do()", None, op.start())
    )
    print('more accurate program result:', result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate program results',
        epilog='Advent of Code 2024 - Day 3: Mull It Over'
    )
    parser.add_argument('input_file')
    main(**vars(parser.parse_args()))
