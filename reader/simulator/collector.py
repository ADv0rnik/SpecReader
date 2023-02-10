import os
from typing import List

from typing import TextIO

DIR_NAME = 'sample_dir/'
SAMPLE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), DIR_NAME)


def find_files(path: str) -> List[str]:
    return [file for file in os.listdir(path) if file.endswith('spe')]


def get_cps(file: TextIO) -> int:
    for index, line in enumerate(file):
        if '$CPS:' in line:
            return int(float(file.readline().strip()))


def parse_values(list_of_files: List[str]) -> List[int]:
    list_of_values = []
    for file in list_of_files:
        try:
            with open(SAMPLE_DIR + file, 'r') as infile:
                list_of_values.append(get_cps(infile))
        except FileNotFoundError as err:
            print('{}'.format(err))
    return list_of_values


def main():
    lst = find_files(SAMPLE_DIR)
    print(lst)
    print(parse_values(lst))


if __name__ == '__main__':
    main()
