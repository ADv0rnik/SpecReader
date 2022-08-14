"""
version 0.3
by Aliaksandr Dvornik
"""

import os
import sys
import time
import argparse

from reader.reader_core import DataInterface
from reader.reader_logger import write_logs
from reader.reader_plot import Plot


DEFAULT_DATA_DIR = os.path.dirname(__file__) + "/data"


def parse_arguments():
    """
    The method determines parser for arguments derived from the CLI.
    Defines all optional and positional arguments such as path, --version and --plot

    :returns: arguments passed on CLI script call

    """
    parser = argparse.ArgumentParser(prog='spec-reader',
                                     description="List of commands for SpecReader",
                                     epilog="Report about all bugs to aadvornik@gmail.com")
    parser.add_argument(
        "-v",
        "--version",
        help="Show this application's version and exit",
        action="version",
        version="SpecReader v.0.1.7"
    )
    parser.add_argument(
        "-p",
        "--plot",
        help="Enable this option to show data on plot. The default directory is {}".format(DEFAULT_DATA_DIR),
        action="store_true",
        default=''
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
            print("[+] Run program")
            time.sleep(1)
            write_logs("Start program")
            data_int = DataInterface()
            cleaned_data = data_int.process_data(file)
            data_int.spec_to_dataframe(cleaned_data)
            if args.plot:
                plot = Plot()
                plot.make_plot()
                answer = input(f"The default directory is {DEFAULT_DATA_DIR}. Do you want to specify another one (y/n)? ")
                plot.save_plot(answer=answer)
            print("[+] End program")
        else:
            print("[-] Incorrect path or file doesn't exist")
            write_logs("Incorrect path or file doesn't exist", 'error')
            sys.exit()


if __name__ == "__main__":
    runner()
