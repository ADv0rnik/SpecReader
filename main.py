"""
version 0.2
by Aliaksandr Dvornik
"""

import os
import time
import argparse

from reader.core import DataInterface
from reader.log_writer import write_logs


FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample.spe')


def parse_arguments():
    parser = argparse.ArgumentParser(description="List of commands for SpecReader",
                                     epilog="Report about all bugs to aadvornik@gmail.com",
                                     exit_on_error=False)
    parser.add_argument(
        "-v",
        "--version",
        help="Show this application's version and exit",
        action="version",
        version="SpecReader v.0.2"
    )
    parser.add_argument(
        "Path",
        metavar='path',
        type=str,
        help='The path to spectrum file'
    )


def runner():
    pass


if __name__ == "__main__":
    print("[+] Run programme")
    write_logs("Start programme")
    time.sleep(1)
    data_int = DataInterface()
    cleaned_data = data_int.process_data(FILE_PATH)
    data_int.spec_to_dataframe(cleaned_data)
    time.sleep(1)
    print("[+] Converting complete")
