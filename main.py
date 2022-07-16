"""
version 0.2
by Aliaksandr Dvornik
"""

import os
import sys
import time
import argparse

from reader.core import DataInterface
from reader.log_writer import write_logs


def parse_arguments():
    """
    The method determines parser for arguments derived from the CLI.
    Defines all optional and positional arguments such as path, --version and --figure

    :returns: arguments passed on CLI script call

    """
    parser = argparse.ArgumentParser(description="List of commands for SpecReader",
                                     epilog="Report about all bugs to aadvornik@gmail.com")
    parser.add_argument(
        "-v",
        "--version",
        help="Show this application's version and exit",
        action="version",
        version="SpecReader v.0.2"
    )
    parser.add_argument(
        "-f",
        "--figure",
        help="Enable option to represent data in one figure",
        action="store"
    )
    parser.add_argument(
        "Path",
        metavar='path',
        type=str,
        help='The path to spectrum file'
    )
    return parser.parse_args()


def runner():
    """
    The method runs program common functionality starting with checking of CLI arguments.
    It uses DataInterface to get parameters from the spectrum file.

    :returns: None
    """
    try:
        args = parse_arguments()
    except argparse.ArgumentError as err:
        print(f"Wrong argument: {err}")
        write_logs(f"{err}. End program", 'error')
        sys.exit()
    else:
        file = args.Path
        if os.path.isfile(file):
            write_logs("Start program")
            data_int = DataInterface()
            cleaned_data = data_int.process_data(file)
            data_int.spec_to_dataframe(cleaned_data)
        else:
            print("[-] Incorrect path or file doesn't exist")
            write_logs("Incorrect path or file doesn't exist", 'error')
            sys.exit()


if __name__ == "__main__":
    print("[+] Run program")
    time.sleep(1)
    runner()
    time.sleep(1)
    print("[+] End program")
